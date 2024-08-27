# Django Food Trucks #

## Project Setup ##

1) Clone the repository.

2) Open terminal and cd into the root project directory (where manage.py and requirements.txt file exists).

3) Create a new virtual environment with command: `python -m venv venv`

4) Activate the virtual environment using command(for Windows): `.\venv\Scripts\activate`

5) Install required python packages (including django) using requirements.txt file with command: `pip install -r requirements.txt`

6) Set up a database: Create a PostgresSQL database/schema with the name "django_food_trucks".
Update the database credentials (user and password) in settings.py file.

7) Run following commands for applying database migrations:
`python manage.py makemigrations`
`python manage.py migrate`

8) (**IMPORTANT**) Then import the csv file provided on the original assignment repository (I have also provided it in my repository as well in root folder having name as 'food-truck-data.csv'), in the newly created table 'api_foodtruck'. This will be needed for data.

9) Start the server with the command: `python manage.py runserver`


## Testing ##

1) Once the server is running, you should be able to view the application on http://127.0.0.1:8000/.
2) On the homepage, you will see the Google Map displayed.
3) Click on any location on the map, and then it will show the nearest 5 trucks available along with some information.


