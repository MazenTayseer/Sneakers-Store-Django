# SneakerHub: A Sneaker Selling Website 

## Overview

SneakerHub is a modern web application built with Django for backend logic, Bootstrap for responsive design, and jQuery for dynamic user interactions. It provides a platform for sneaker enthusiasts to browse, buy, and even sell some of the most sought-after sneakers in the market.

📌 **Note**: This project was built in just 2 days as a demonstration of rapid web development with Django.

## Features

- **User Accounts**: Register, login, and manage profile details.
- **Product Listings**: Detailed pages for each sneaker with images, sizes, descriptions, and pricing.
- **Search and Filter**: Search for sneakers by brand, model, or color and filter results by size or price range.
- **Shopping Cart**: Add sneakers to your cart and manage your orders.
- **Seller Dashboard**: For users interested in selling their sneakers, they can manage their listings and track sales.
- **Responsive Design**: Whether you're on a desktop, tablet, or mobile device, SneakerHub looks great and functions flawlessly.

## Installation

### Prerequisites

- Python 3.8 or newer
- pip (Python package manager)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/MazenTayseer/SneakerHub.git
   cd SneakerHub
   ```

2. **Set up Virtual Environment (recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Database Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

Now, open a web browser and navigate to `http://127.0.0.1:8000/` to see the application in action.


## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JS, Bootstrap and jQuery
- **Database**: SQLite (default) but can be configured for other databases.


## Support

If you encounter any issues or have suggestions, please file an issue on the GitHub page. If you like this project, don't forget to star ⭐ the repository!

---

Happy sneaker shopping & selling!
