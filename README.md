# 🎵 Musical Instruments Shop 🎸🎹🎷

## 📖 Description  
This **Musical Instruments Shop** project organizes products into categories and includes multiple pages:  
- **Category Page**  
- **Products Page**  
- **Product Detail Page**  
- **Order Data Page**  
- **Order Detail JSON Page**  

The project uses **Django**, **SQLite**, and HTML templates for the store app, offering a simple, functional design with basic statistical analysis per category.

---

## 🏗️ Project Structure  
custom_user_and_admin/
├── media/                      # Stores user-uploaded images
├── order/                      # Order app for orders and carts
│   ├── admin.py                # Admin customizations
│   ├── migrations/             # Database migrations
│   ├── models.py               # Order-related models
│   ├── views.py                # Order-related views
│   └── urls.py                 # URL routing for orders
├── custom_user_and_admin/      # Project-level settings
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Root URL configuration
├── store/                      # Store app for products and categories
│   ├── admin.py                # Admin customizations
│   ├── migrations/             # Database migrations
│   ├── static/                 # Static files (CSS, images)
│   │   └── store/style.css     # Styles for the store
│   ├── templates/              # HTML templates
│   │   ├── category.html       # Category page
│   │   ├── detail.html         # Product detail page
│   │   ├── index.html          # Homepage
├── user/                       # Custom user app
│   ├── admin.py                # Admin customizations
│   ├── apps.py                 # App configuration
│   ├── migrations/             # Database migrations
│   ├── models.py               # Custom user model
│   ├── signals.py              # Signal for user cart creation
│   └── tests.py                # Unit tests
├── db.sqlite3                  # SQLite database
├── manage.py                   # Django CLI
├── requirements.txt            # Project dependencies
└── README.md                   # Documentation


---

## 🛠️ Features  
### **Store**
1. **Category Page**  
   - **URL:** `/` or `/category/`  
   - Displays **6 root categories** with product counts and links to category pages.  
   - Admin: Custom **CategoryAdmin** using `DraggableMPTTAdmin`.  

2. **Category Products Page**  
   - **URL:** `/category/{category_id}/products`  
   - Displays products in the category (or subcategories) with statistics like total price and quantity.  
   - Features **Pagination**: 6 products per page.  
   - Admin: Custom **ProductAdmin** with `get_total_price()` and **PriceRangeFilter** for filtering products by price.

3. **Product Detail Page**  
   - **URL:** `/category/{category_id}/products/{product_id}`  
   - Displays detailed product information: name, description, price, quantity, ancestor categories, and image.

---

### **Order**
1. **Order Data Page**  
   - **URL:** `/order/`  
   - Returns a **JSON** response summarizing orders.  

2. **Order Detail Page**  
   - **URL:** `/order/{order_id}/`  
   - Returns detailed **JSON** of a specific order.  

3. **User Cart**  
   - Automatically created for new users using **signals**.  
   - One-to-One relationship with **User** model.  

---

### **User**  
- Custom **User** model with email-based login.  
- Admin: Custom **UserAdmin** for personalized views.  

---

### **Admin Panel**  
- **URL:** `/admin/`  

---

## 📊 Database Design  
- **Database Name:** `db.sqlite3`  
- **Tables:**  
  - `store_category` (recursive relationship for parent category)  
  - `store_product` (many-to-many with `store_category`)  
  - `order_order` (many-to-one with `store_product`)  
  - `order_usercart` (one-to-one with `user_user`)  
  - `user_user` (custom user model)  

---

## 🔧 Dependencies  
- **Python 3.x**  
- **Django 5.1.1**  
- **Pillow 10.4.0**  
- **Django-debug-toolbar**  
- **Django-mptt**  

---

## 🚀 Usage  
1. Clone the repository:  
   ```bash
   git clone https://github.com/hella753/musical_instruments_shop.git
   cd musical_instruments_shop
