# Web Application Structure

## Application Directory Structure  (Template)

- `app/` - Main application directory.
  - `__init__.py` - Initializes the application.
  - `models.py` - Defines database models.
  - `routes.py` - Contains routes/endpoints for the application.
  - `templates/` - HTML templates for the application. Example: `add_task.html`
  - `static/` - Static files (CSS, JS, images).
- tests/ - Contains test cases.
  - `__init__.py`
  - `test_models.py` - Tests for database models.
  - `test_routes.py` - Tests for application routes. Example: Tests for CRUD operations on tasks.
  - `config.py` - Configuration settings for the application.
  - `requirements.txt` - List of Python package dependencies.
  - `run.py` - Entry point to run the application.

## Sample Code

1. **Basic Flask Application:**

- Initialize Flask app in `app/__init__.py`.
- Define a simple route in `app/routes.py`. Example: Adding a new tasks (`/add-task`)
- Create a basic HTML template in `app/templates`.
  
2. **Database Models (Optional):**

- Define a simple model in `app/models.py` if using a database.

## Testing with PyTest

- **Initial Test Setup:**
  - Setup PyTest in the `tests/` directory.
  - Write basic tests for the route in `test_routes.py`. Example `test_tasks_operations.py`
  - If using models, write tests in `test_models.py`.

## Running the Application

- **Execution:**

  - Run the application using `run.py`.
  - Execute tests using PyTest.

## Dependencies

- **Requirements:**
  - List Flask, PyTest, and other dependencies in `requirements.txt`.

This template provides a basic structure for a Flask web application and its tests. The actual implementation will vary based on the specific requirements of your project. The focus should be on creating simple, testable components, gradually building complexity as you become more comfortable with Flask and PyTest.
