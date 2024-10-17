# Django Custom User model & Admin Optimization


## Description
The Musical instruments store with products ordered in categories. The project has several pages: one for categories, 
one for products, one for product detail, one for order data and one for order detail data in json. 
Uses HTML templates for store app and has a simple design. It also provides basic 
statistical analysis per category.
The Project uses Django and sqlite3 database.

### Error მაქვს ერთი რომლის დეტალებიც user/admin.py-ში მიწერია </3 

## What's new this week?
* **Custom User model** and **Custom User manager** was added. Now you can only log in on admin panel via an email.
* **Custom ModelAdmins** are created on every app for more personalized views in admin panel.
* **UserCart** model is added to Order app which uses OneToOne relationship.
* **Signal** is added in the User app for when the user is created to create the user's cart automatically as well.


Project Structure:
```
custom_user_and_admin/
├── media
├── order
│   ├── admin.py
│   ├──migrations
│   ├──models.py
│   ├──views.py
│   └──urls.py
├── custom_user_and_admin
│   ├── settings.py
│   ├── urls.py
├── store
│   ├── admin.py
│   ├── migrations
│   ├── static
│   │   ├── store
│   │   │   ├── style.css
│   ├── templates
│   │   ├── category.html
│   │   ├── detail.html
│   │   ├── index.html
├── user
│   ├──admin.py
│   ├──apps.py
│   ├──migrations
│   ├──models.py
│   ├──signals.py
│   └──tests.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```


Database name: `db` <br>
Tables created: `store_category`, `store_product`, `store_product_product_category`(association table), `order_order`, `order_usercart`, `user_user`(and other automatically generated user tables)<br>

`store_product` uses many-to-many relationship and is connected to `store_category` on **product_category**<br>
`store_category` uses recursive (many-to-one relationship to itself) for **parent**<br>
`order_order` uses many-to-one relationship and is connected to `store_product` on **product**<br>
`order_usercart` uses one-to-one relationship and is connected to `user_user` on **user**<br>
`user_user` custom user model

For testing purposes there are 23 product, 19 category, 3 user and 3 usercart records in the database <3

## **Components** ##
* **store** - This app contains the models(Product and Category) and 3 views for the store.
* **order** - This app contains the models(Order and UserCart) and 2 views for the order.
* **user** - This app contains Custom user model which requires you to login via email. Also uses Custom UserManager
* **media** - All user uploaded images go to the media folder.
* **store/static** - for static files: CSS
* **templates** - 3 HTML templates for rendering are stored here.
* **db.sqlite3** - Database file.


## **Features** ##
* **Category** - Can be accessed at `/` or `/category/` Displays the 6 root categories and its products count with links to each category page. 
  * CategoryAdmin inherits from DraggableMPTTAdmin and admin.ModelAdmin and provides customization.
* **Category Products Page** - Can be accessed at `/category/{category_id}/products`. Displays all the products in that category or in its subcategories with statistics about the category and total sum of the product price including its quantity. Uses **Pagination** and Only 6 products are displayed in one page with their prices and images and each product is linked to its detail page. 
  * ProductAdmin inherits from admin.ModelAdmin and adds `get_total_price()` for calculating total sum
  * `PriceRangeFilter()` inherits from **admin.SimpleListFilter** and is a custom class for filtering product_price which is a decimal value.
* **Product Detail Page** - Can be accessed `/category/{category_id}/products/{product_id}` and Displays the information about the individual Product such as id, name, description, price, ancestor categories, image and quantity.
* **User** - Has a custom **User** model with an email as username field, has a custom **UserManager** which has `create_user()` and `create_superuser() `methods. 
  * UserAdmin inherits from admin.ModelAdmin and provides customization.
  * in **signals.py** is a method `create_cart_for_user()` which automatically creates an UserCart object everytime new user is created and assigns the cart to that user.
* **Order** - Can be accessed at /order/ Displays short info of the orders in json.
  * OrderAdmin inherits from admin.ModelAdmin and adds `get_total_price()` for calculating total sum of the order
  * UserCartAdmin inherits from admin.ModelAdmin and provides customization.
* **Order Detail Page** - Can be accessed at /order/{order_id}/ Displays the details of individual order in json.
* **Admin Panel** - Can be accessed at `/admin/`. Default email: `admin@example.com`, password: `admin`.
* **Database** - sqlite3 database is used.

## Dependencies
* **Python 3.X**
* **Django 5.1.1**
* **Pillow 10.4.0** - Python Imaging Library adds image processing capabilities to your Python interpreter.
* **Django-debug-toolbar** - Configurable set of panels that display various debug information about the current request/response.
* **Django-mptt** - Reusable Django app which aims to make it easy for you to use MPTT(a technique for storing hierarchical data in a database).

## Usage
Clone the repository:
```bash
git clone https://github.com/hella753/simple_rendering_with_three_page.git
cd simple_rendering_with_three_page
```
To install the dependencies, use the following command in your terminal:
```bash
pip install -r requirements.txt
```
To run the development server, use the following command in your terminal:
```bash
python manage.py runserver
```
To access the application, open your browser and go to http://127.0.0.1:8000/

