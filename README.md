# Order managment (crud)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
## Test order managment system with API.
- API root endpoint: <a href="http://cafe.hub10.ru/api/orders/">cafe.hub10.ru/api/orders/</a>
- api/admin/
- api/orders/
- api/orders/id/
- api/orders/create/
- api/orders/<int:pk>/update/
- api/orders/<int:pk>/delete/
- api/revenue/
### Functional description.
- Create, Read, Update and Delete orders: via API-endpoints or web-interface.
- Order is the list of JSON-object. Must be entered in JSON-format.
- User enters the table number and a list of dishes with prices.<br>
The system automatically adds an order with a unique ID, calculated cost, and a “pending” status.

#### Order Deletion:
- The user selects an order by ID through the web interface and deletes it from the system.
#### Order Search:
- Orders can be filtered by table number or status.
#### Order List:
- Order list show all orders: their ID, table number, list of dishes, total cost, and status.
#### Order Status Modification:
- Default status: "cooking"
- Every user can change order status (“cooking”, “ready”, “paid”).
#### Shift Revenue Calculation:
- Separate page for calculating the total revenue of orders with the “paid”-status.
<hr>

#### Installation:
- With pre-installed pip and python:
- Clone repository
- Create virtual environment: python3 -m venv
- Run environment: source venv/bin/activate
- In folder with requierements.txt:
- Install dependencies: pip install -r requierements.txt
- In project folder cafe_main make migrations: 
- python3 manage.py makemigrations
- python3 manage.py migrate
- Collect staticfiles:
- python3 manage.py collectstatic
- Run server on localhost:
- python3 manage.pt runserver
<hr>

#### Screenshots.
![Скриншот](https://raw.githubusercontent.com/zerg959/cafe-crud/main/screenshots/cafe1.PNG)
![Скриншот](https://raw.githubusercontent.com/zerg959/cafe-crud/main/screenshots/cafe2.PNG)
![Скриншот](https://raw.githubusercontent.com/zerg959/cafe-crud/main/screenshots/cafe3.PNG)
![Скриншот](https://raw.githubusercontent.com/zerg959/cafe-crud/main/screenshots/cafe4.PNG)
![Скриншот](https://raw.githubusercontent.com/zerg959/cafe-crud/main/screenshots/cafe5.PNG)
