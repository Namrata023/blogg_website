 # Blog Web Application using Django


## Description

Blogger’s Haven is a platform aiming to simplify blogging for individuals and businesses.The platform's mission is to enable content creators to write, manage, and share their blogs effortlessly while engaging with their audience through comments and likes.
## Screenshots 
Home page:![alt text](<Screenshot (76).png>)








## Features

- Light/dark mode toggle
- Secure user registration and login
- CRUD Operation: Create,edit, and delete blog posts
- Interact with posts through comments and likes


## Requirements and Technologies Used

- Python 3.9 & up
- Virtual Environment
- Git & Github
- Frontend:  HTML, CSS, JavaScript
- Backend:Django (Python) 
- Database: SQLite

## Setup/Installation

- Step 1: Clone The Repository
Open a terminal or command prompt and run:
```bash
git clone https://github.com/Namrata023/blogg_website.git
cd bloggers-haven
 
```
- Step 2: Set Up a Virtual Environment
```bash
python -m venv .venv
# On Windows use: .venv\Scripts\activate or source .venv/bin/activate  

```
- Step 3: Install Dependencies
```
pip install -r requirements.txt

```
- Step 4: Set Up Environment Variables
Create a .env file in the project root and add necessary configurations:
```
SECRET_KEY=your_secret_key
DEBUG=True
```
- Step 5: Apply Database Migrations
```
python manage.py makemigrations
python manage.py migrate
```
- Step 6: Create a Superuser
```
python manage.py createsuperuser
```
- Step 7: Run Project 
```
python manage.py runserver
```


## Status
Project is Done
## Contact
Created by https://www.linkedin.com/in/namrata-adhikari-04a117324/ - feel free to contact me!