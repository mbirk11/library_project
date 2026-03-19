# Library Project

A modern Django-based library management system that allows readers to explore a collection of books, register for an account, and manage their personal reading profile.

## Features

- **User Authentication**: Secure, session-based login and registration for readers.
- **Book Catalog**: A comprehensive list of available books with detailed information for each.
- **Personal Profile**: Readers can create a personal profile and keep track of books they are interested in.
- **Dynamic Content**: Seamless navigation between the book directory and personal reading lists.

## Project Structure

The project is divided into two main Django applications:

- **`book`**: Manages the core book catalog, index landing page, and book detail views.
- **`reader`**: Handles reader profiles, registration forms, and the "My Books" collection functionality.

## Requirements

- Python 3.10+
- Django 6.0.3

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd library_project
   ```

2. **Set up a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install django==6.0.3
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **Landing Page**: Log in with your email and password. If you don't have an account, you will be redirected to the registration page.
- **Book List**: Browse all available books. Click on a book to see its full details.
- **Add to Profile**: From a book's detail page or list, you can add it to your personal profile.
- **Profile View**: View your curated collection of books in your personal profile.

## License

This project is licensed under the MIT License.
