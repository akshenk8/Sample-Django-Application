## Setup

1. Install Python 3.9
2. Create a virtual environment using `virtualenv` or `conda`. Then install the requirements mentioned in
   the `requirements.txt`.
3. This project uses sqlite DB and doesn't require any additional databases.
4. For quick setup and user creation, run `bash setup.sh`. This script will run migrations and create a super user
   named `root` with the password `root@123`. (not ideal for production usage)

## Running the server

1. Execute the following command `python manage.py runserver`. (not ideal for production. for deployment
   refer [this](https://docs.djangoproject.com/en/4.0/howto/deployment/) and NGINX or Apache for deploying static files)
   .
2. Go to `http://127.0.0.1:8000/admin/` and login with the username and password. As I haven't created the login &
   logout pages for user accounts.
3. Then go to `http://127.0.0.1:8000/` for testing the Team management application.