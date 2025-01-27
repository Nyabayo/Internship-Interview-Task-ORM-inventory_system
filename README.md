

---

# **Inventory Management System**

This project provides a backend API for managing products in an inventory. It allows users to list, add, update, and delete products using a RESTful API.

---

## **Project Setup Instructions**

### **1. Prerequisites**
Ensure you have the following installed:
- **Python**
- **MySQL**
- **Git**
- **Postman** (for testing)

---

### **2. Clone the Repository**
Run the following command:
```bash
git clone https://github.com/Nyabayo/Internship-Interview-Task-ORM-inventory_system.git
```

---

### **3. Set Up a Virtual Environment**
Create and activate a virtual environment:
```bash
python3 -m venv my_venv
source my_venv/bin/activate
```

---

### **4. Install Dependencies**
Install the required dependencies using:
```bash
pip install -r requirements.txt
```

---

### **5. Configure the MySQL Database**
1. **Create a database in MySQL**:
   ```sql
   CREATE DATABASE inventory_db;
   ```
2. **Update `settings.py`**:
   ```
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'inventory_db',
           'USER': 'root',
           'PASSWORD': '',  
           'HOST': 'localhost',
           'PORT': '3306'
       }
   }
   ```

---

### **6. Apply Migrations**
Run the following commands:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

---

### **7. Start the Development Server**
Start the server:
```bash
python3 manage.py runserver
```

---

## **API Endpoints**

### **1. List All Products**
- **Method**: `GET`
- **Endpoint**: `/api/products/`
- **Response**:
   ```json
   [
       {
           "id": 1,
           "name": "Laptop",
           "description": "Programming laptop.",
           "price": 3500.50,
           "stock": 10
       },
       {
           "id": 2,
           "name": "Mouse",
           "description": "Wireless mouse.",
           "price": 600.00,
           "stock": 50
       }
   ]
   ```
- **Postman Screenshot**:  
  ![List Products](https://github.com/Nyabayo/Internship-Interview-Task-ORM-inventory_system/blob/main/Screenshots/GET1.png?raw=true)

---

### **2. Add a New Product**
- **Method**: `POST`
- **Endpoint**: `/api/products/add/`
- **Request Body**:
   ```json
   {
       "name": "Laptop",
       "description": "A high-performance laptop.",
       "price": 1200.50,
       "stock": 10
   }
   ```
- **Response**:
   ```json
   {
       "message": "Product added successfully!",
       "product_id": 1
   }
   ```
- **Postman Screenshot**:  
  ![Add Product](https://github.com/Nyabayo/Internship-Interview-Task-ORM-inventory_system/blob/main/Screenshots/add_POST.png?raw=true)

---

### **3. Update an Existing Product**
- **Method**: `PUT`
- **Endpoint**: `/api/products/<id>/update/`  
  *(Replace `<id>` with the product ID, e.g., `/api/products/1/update/`)*
- **Request Body**:
   ```json
   {
       "name": "Updated Coding Laptop",
       "price": 1100.00
   }
   ```
- **Response**:
   ```json
   {
       "message": "Product updated successfully!"
   }
   ```
- **Postman Screenshot**:  
  ![Update Product](https://github.com/Nyabayo/Internship-Interview-Task-ORM-inventory_system/blob/main/Screenshots/update_PUT.png?raw=true)

---

### **4. Delete a Product**
- **Method**: `DELETE`
- **Endpoint**: `/api/products/<id>/delete/`  
  *(Replace `<id>` with the product ID, e.g., `/api/products/1/delete/`)*
- **Response**:
   ```json
   {
       "message": "Product deleted successfully!"
   }
   ```
- **Postman Screenshot**:  
  ![Delete Product](https://github.com/Nyabayo/Internship-Interview-Task-ORM-inventory_system/blob/main/Screenshots/DELETE1.png?raw=true)

---

## **Database View (phpMyAdmin Screenshot)**

Here’s the database view after adding products:  
![Database View](https://github.com/Nyabayo/Internship-Interview-Task-ORM-inventory_system/blob/main/Screenshots/mysql.png?raw=true)

---

Thank you 😊
