# Coupon Engine API

A simple backend service built using **Django REST Framework** to manage and apply coupon codes during checkout.

---

## Features

* Create coupons
* List all coupons
* Apply coupon to cart value
* Disable coupons
* Supports:

  * Flat discount
  * Percentage discount
* Business rules enforced:

  * Minimum cart value
  * Active/inactive coupons
  * Final amount never below 0

---

## Bonus Features Implemented

* Coupon expiry date
* Maximum discount cap for percentage coupons
* Basic request validation
* Clean separation of logic (views + services)

---

## Tech Stack

* Python
* Django
* Django REST Framework
* SQLite (default DB)

---

## Project Structure

```
coupon-engine/
 ├── config/
 ├── coupons/
 │    ├── models.py
 │    ├── serializers.py
 │    ├── views.py
 │    ├── services.py
 │    ├── urls.py
 ├── manage.py
```

---

## Setup Instructions

1. Clone the repository

```
git clone <your-repo-link>
cd coupon-engine
```

2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3. Install dependencies

```
pip install django djangorestframework
```

4. Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

5. Start server

```
python manage.py runserver
```

---

## API Endpoints

### 1. Create Coupon

**POST** `/coupons`

```
{
  "code": "SAVE100",
  "discountType": "FLAT",
  "discountValue": 100,
  "minCartValue": 500
}
```

---

### 2. List Coupons

**GET** `/coupons`

---

### 3. Apply Coupon

**POST** `/coupons/apply`

```
{
  "code": "SAVE100",
  "cartValue": 800
}
```

---

### 4. Disable Coupon

**PATCH** `/coupons/{code}/disable`

---

## Example Test Cases

### Valid Flat Coupon

* Cart: ₹800
* Discount: ₹100
* Final: ₹700

---

### Below Minimum Cart Value

* Cart: ₹300
* Error: Cart value should be at least required amount

---

### Percentage Coupon

* 10% of ₹1000 → ₹100
* Final: ₹900

---

### Max Discount Case

* 50% of ₹1000 = ₹500
* Max allowed = ₹200
* Final discount = ₹200





## 👨‍💻 Author

Built as part of a backend internship assignment to demonstrate API design, business logic handling, and clean code structure.

---
