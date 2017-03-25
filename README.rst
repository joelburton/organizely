Organizely
==========

A simple sample Django app.

To install / play with:

1. Clone this repo and go into your clone::

    $ git clone https://github.com/joelburton/organizely.git
    $ cd organizely

2. Create and activate a virtual environment::

    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt

3. Create the PostgreSQL database::

    $ createdb organizely

4. Ask Django to run all migrations. This will create all needed
   tables for all applications::

    $ python manage.py migrate

   Now, if you'd like, you can look at the database (``psql organizely``)
   and examine the tables created.

5. Create a superuser account::

    $ python manage.py createsuperuser

6. Load some sample data I created (you can see this in `todos/fixtures`,
   if you'd like to look at it)::

    $ python manage.py loaddata initial

7. Run the tests (there's only one, but this is how you run tests)::

    $ python manage.py test

8. Start the server::

    $ python manage.py runserver

Playing with the Application Admin
----------------------------------

1. Visit http://localhost:8000/admin. You should be able to log in as your
   superuser.

2. You can look at/add/edit/delete task lists or tasks.

Playing with the Public View
----------------------------

1. Visit http://localhost:8000. You can do this either in the same browser
   where you were logged in as the admin (in which case you'll be able
   to add/edit tasks), or anonymously (in which case you can't).

2. You can see the task-list list and detail pages, and the task list and
   detail pages. There's a nice through-the-web interface for adding
   and editing tasks.


