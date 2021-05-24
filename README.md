#  Insta-Clone Web App

#### This is a Clone of the popular app Instagram, 21/05/2021

#### By **Eston Kagwima**

## Description

This WebApp that mimics the functiionalty of the popular instagram app such as uploading image liking and commenting on it.

This project was generated with [Django](https://docs.djangoproject.com/en/3.2/) version 3.2.3


### User stories Specification
- Sign in to the application to start using.
- Upload my pictures to the application.
- See my profile with all my pictures.
- Follow other users and see their pictures on my timeline.
- Like a picture and leave a comment on it.
## Setup/Installation Requirements
- install Python3.9
- Clone this repository `git clone https://github.com/kagus-code/instagram-clone`
- Change directory to the project directory using  the `cd` command
- Open project on VSCode
- If you want to use virtualenv: `virtualenv ENV && source ENV/bin/activate`
####  Create the Database
    - psql
    - CREATE DATABASE <name>;
####  .env file
Create .env file and paste paste the following and fill  required fields:

    SECRET_KEY = '<Secret_key>'
    DBNAME = '<name>'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
#### Run initial Migration
    python3.9 manage.py makemigrations <name of the app>
    python3.9 manage.py migrate
#### Run the app
    python3.9 manage.py runserver
    Open terminal on localhost:8000


## Technologies Used

- Django version 3.2.3
- Python
- JavaScript
- HTML
- CSS
- Bootstrap
- Postgressql

## link to live site on GitHub Pages

https://kagusinstagram.herokuapp.com/


## Support and contact details

| Eston | ekagwima745@gmail.com |
| ----- | --------------------- |

### License

License
[MIT License](https://choosealicense.com/licenses/mit/)
Copyright (c) 2021 Eston Kagwima
