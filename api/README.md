# Meal Recommendation Service

This api provides you personalized meal recommendations based on preferences. Users will receive a new meal recommendation every `n` minutes, and the recommendation is generated either randomly or based on the ingredients, category, or area of the most liked meals.

## Stack

- Django
- Django Rest Framework
- SQLite

## External API

This service leverages [TheMealDB API](https://www.themealdb.com/api.php) to fetch information about meals.

## Endpoints

### Get Auth User Meals

- **Endpoint:** `/meals`
- **Method:** GET
- **Description:** Retrieve all meals associated with the user.

### Update Meal State

- **Endpoint:** `/meals/:id`
- **Method:** PUT
- **Parameters:**
  - `id`: User Meal ID
- **Request Body:**
  - `state`: Update the state of the meal (liked, disliked, ignored)

## Recommendations

The recommendation system should consider preferences and suggests meals based on the most liked ingredients, category, or area. Note that currently, the system selects a random preference when assigning meals, without considering likes. This is an area for improvement.

## Instructions to Run

### Prerequisites

- Python 3.11 (or later)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)

### Setup Virtual Environment

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # For Linux/Mac
.\venv\Scripts\activate  # For Windows

# Install project dependencies
pip install -r requirements.txt

# Run Django Development Server
python manage.py runserver
# The service will be accessible at http://127.0.0.1:8000/.

# To assign new meals to users, run the following command:
python manage.py assign_new_meals
# This command fetches new meal recommendations and assigns them to users based on their preferences.

