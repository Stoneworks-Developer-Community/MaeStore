# Maestore
*A Project to Collect and Preserve*
## What is Maestore?
Maestore is a project in simmilar scope as [Civbooks](https://civbooks.github.io/). Maestore aims to collect and preserve books from the Stoneworks worldbuilding server which are either...

A. No longer available due to a World Shutdown

B. Not widely available, and no longer produced (Copies of Copies) by the Author or sellers
## Installation
Ensure you have an instance of Python 3.11.1 or Newer installed on your machine 
1. Clone this repo
2. Navigate to the downloaded repository `cd maestore`
3. Create a virtual environment
   - Install poetry `pip install poetry`
   - Install dependancies `poetry install`
4. Run the following lines. 
   ```cmd
   py manage.py makemigrations
   py manage.py migrate
   ```
6. Create your first admin user
   - run `py manage.py createsuperuser` and follow the instructions in your terminal
7. Run the django application. `py manage.py runserver`
8. You can now find Maestore open on your localhost!
