# Django REST Movie Website

Welcome to the Django REST watchlist Website! This project is a web application built using Django and Django REST Framework, designed to provide a platform for managing and browsing movie information through a RESTful API.

## Features

- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on movie entries.
- **RESTful API**: Expose movie data through a RESTful API for seamless integration with other applications.
- **Authentication and Authorization**: Secure endpoints using token-based authentication and restrict access based on user permissions.
- **Search and Filtering**: Search and filter movies based on various criteria such as title, genre, release year, etc.
- **Pagination**: Paginate large sets of movie data for improved performance and user experience.
- **Customizable**: Easily extend or customize functionality to suit specific requirements.

## Requirements

- Python (3.x recommended)
- Django (3.x recommended)
- Django REST Framework (3.x recommended)
- Database ( SQLite,)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/fionamokua/watchlist.git

2. Navigate to project repository:

   cd watchlist

3. Install dependancies:

 pipenv shell

4. Run database migrations:

python manage.py migrate

5. Start the development server:

python manage.py 

6. runserver
Access the application at http://localhost:8000.