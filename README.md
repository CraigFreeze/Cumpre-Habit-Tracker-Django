# Overview

Cumpre is a Habit Tracking App. The name comes from portuguese and means "Accomplish." The app is designed to visually help users see their progress. This is my first program in Django, and just starts my experience with the MVT work flow. It has added functionality to report on your endeavors through journaling.

The Web App allows users to indicate whether the individual successfully accomplished the habit in a day, did not do the habit or chooses not to report for any given day. 

The web app has four main features:
* Managing Habits
* Reporting on Habit Progress
* Habit Creation
* Journaling

{Opening the Project:}
* To run a test server on the computer you must first enter the virtual machine (command: source venv/bin/activate). Then iniate the server (command: python manage.py runserver).
* The first page to open will be the homescreen, "habit_index.html." That being said, the navigation bar will get you anywhere from any template.

{Purpose of Project:}
The purpose is based on the following quote: "President Monson has also taught: “When performance is measured, performance improves. When performance is measured and reported, the rate of improvement accelerates” (in Conference Report, Oct. 1970, 107)." As such, I seek to learn how to track progress, and incorporate progress into my talents and abilites as a programmer. 

[Software Demo Video](https://youtu.be/VP4-b9oGAKg)

# Web Pages

(Each page has a navigation bar that will take you anywhere in the app)
* Home Page - A card structure that shows each habit, and a brief description with a navigation button to see habit progress. There is functionality to delete habits from the database on this page. Each of the habits are dynamically created. And the habits will remain in their column, row structure even when added or removed from the database.
* View Habit - This gives a detailed breakdown of when you accomplished or did not accomplish your habit. You can add response days, and view the progress of any given habit. You can navigate back to any page using the navbar. Each of the habit report boxes (habitresponses) is dynamically created. 
* Add Habit - This is where titles and descriptions can be made for habits. When you submit a new habit, it takes you to view all of the habits on the home screen.
* Journaling - This page has a form for writing a report on your habits. The page dynamically displays all of the Journal entries. They are displated vertically and will scroll as more are added. With functionality to remove them. The Navbar allows navigation to each of the pages. 


# Development Environment

{Tools:}
* Django - 4.1.5 (command: python -c "import django; print(django.get_version())")
* VS Code - Apple Silicon 2022
* Abstracted sqlite3 

{Programming Language}
* Python - Version 3.10.5 - A language for fast development it is a highlevel programming language [Dowload] (https://www.python.org/downloads/)

{Styling and Markup:}
* HTML5
* CSS - Bootstrap [Bootstrap](https://getbootstrap.com)

# Useful Websites

* [Real Python](https://realpython.com/get-started-with-django-1/)
* [Django Documentation](https://docs.djangoproject.com/en/4.1/)
* [Django Documentation - FORMS](https://docs.djangoproject.com/en/4.1/topics/forms/)
* [Django Documentation - POLL TUTORIAL](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)
* [Stack Overflow - Form Validations](https://stackoverflow.com/questions/5516437/django-form-has-no-errors-but-form-is-valid-doesnt-validate)
* [Stack Overflow - Default Values](https://stackoverflow.com/questions/604266/django-set-default-form-values)
* [Programiz.com - Datetime in Python ](https://www.programiz.com/python-programming/datetime/current-datetime)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* A calendar organization for each of the habits.
* Make it so that each day, a habit response is added, so that they do not have to keep track of what day they are on
* I would add hover styling on each of the habit responses that displays the datetime of each response.
* I would add dates to the journal functionality.
* A way to remove habit responses.