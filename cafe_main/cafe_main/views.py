# my_app/views.py
import requests
import json
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from orders.models import Order
from django.conf import settings
import os

API_URL = 'http://127.0.0.1:8000/api/orders/'

def index(request):
    """
    View for main web-page with main menu.
    """
    return render(request, 'cafe_main/index.html')


def order_list(request):
    """
    Display the list of orders with filtering.
    """
    api_url = API_URL
    table_number = request.GET.get('table_number')
    status_order = request.GET.get('status_order')

    params = {}
    if table_number:
      params['table_number'] = table_number
    if status_order:
      params['status_order'] = status_order

    response = requests.get(api_url, params = params)
    orders = response.json()

    return render(
        request,
        'cafe_main/order_list.html',
        {
            'orders': orders,
            'STATUSES_ORDERS': Order.STATUSES_ORDERS
        }
    )  # Add STATUSES_ORDERS to template

def order_detail(request, pk):
    """
    Display details of a specific order.
    """
    api_url = f'{API_URL}{pk}/'
    try:
        response = requests.get(api_url)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        order = response.json()
        return render(request, 'cafe_main/order_detail.html', {'order': order})
    except requests.exceptions.RequestException as e:
        # Handle the exception (e.g., log it, display an error message)
        print(f"Error fetching order details: {e}")
        return render(request,
                      'cafe_main/error.html',
                      {'error_message': f"Could not retrieve order details (Error: {e})"}
                      )

def order_create(request):
    """
    Handle order creation.
    """
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            headers = {'Content-type': 'application/json'}
            cleaned_data = form.cleaned_data
            cleaned_data['dishes'] = json.dumps(cleaned_data['dishes'])
            response = requests.post(
                API_URL,
                json=form.cleaned_data,
                headers=headers
                )
            if response.status_code == 201:
                order = response.json()
                return redirect('order_detail', pk=order['id'])
            else:
                form.add_error(
                    None,
                    f"Failed to create order. \
                        API returned status code: {response.status_code}"
                        )
                return render(
                    request,
                    'cafe_main/order_create.html',
                    {'form': form}
                    )
    else:
        form = OrderForm()
        return render(
            request,
            'cafe_main/order_create.html',
            {'form': form}
            )

def order_update(request, pk):
    """
    Handle order update.
    """
    api_url = f'{API_URL}{pk}/'
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        order = response.json()
        if request.method == 'POST':
            form = OrderForm(request.POST, initial=order)
            if form.is_valid():
                headers = {'Content-type': 'application/json'}
                response = requests.put(
                    api_url,
                    json=form.cleaned_data,
                    headers=headers
                    )
                if response.status_code == 200:
                    return redirect('order_detail', pk=pk)
                else:
                    form.add_error(
                        None,
                        f"Failed to update order.\
                              API returned status code: {response.status_code}"
                              )
                    order['dishes'] = json.dumps(order['dishes'])
                    return render(
                        request,
                        'cafe_main/order_update.html',
                        {'form': form, 'order': order}
                        )
            else:
                order['dishes'] = json.dumps(order['dishes'])
                return render(
                    request,
                    'cafe_main/order_update.html',
                    {'form': form, 'order': order, 'form': form}
                    )
        else:
            order['dishes'] = json.dumps(order['dishes'])
            form = OrderForm(initial=order)
            return render(
                request,
                'cafe_main/order_update.html',
                {'form': form, 'order': order, 'form': form}
                )
    except requests.exceptions.RequestException as e:
        print(f"Error update order: {e}")
        return render(
            request,
            'cafe_main/error.html',
            {'error_message': f"Could not retrieve order for update (Error: {e})"}
            )

def order_delete(request, pk):
    """
    Handle order deletion.
    """
    api_url = f'{API_URL}{pk}/'
    if request.method == 'POST':
        try:
            response = requests.delete(api_url)
            response.raise_for_status()
            if response.status_code == 204: # No Content
                return redirect('index')
            else:
                return render(
                    request,
                    'cafe_main/error.html',
                    {'error_message': f"Could not delete order\
                      (Status code: {response.status_code})"}
                      )
        except requests.exceptions.RequestException as e:
            print(f"Error deleting order: {e}")
            return render(
                request,
                'cafe_main/error.html',
                {'error_message': f"Could not delete order (Error: {e})"}
                )
    else:
        # If user accidentally navigated to the DELETE URL, just redirect them to the order detail page
        return redirect('order_detail', pk=pk)

def revenue(request):
    """
    View for web-page with paid orders total revenue.
    """
    api_url = f'{API_URL}revenue/'  # URL вашего API
    try:
        response = requests.get(api_url)
        revenue_data = response.json()  # Get the JSON
        total_revenue = revenue_data.get('total_revenue', 0)  # Extract
        return render(request, 'cafe_main/revenue.html', {'total_revenue': total_revenue})
    except requests.exceptions.RequestException as e:
        print(f"Error page revenue creation: {e}")
        return render(
            request,
            'cafe_main/error.html',
            {'error_message': f"Could not retrieve revenue (Error: {e})"})
