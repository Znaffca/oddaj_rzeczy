# oddaj_rzeczy - portfolio_lab project <br>
Portfolio lab project - description in progress...

#### 12.02.2019 - what is working:
- project first configuration
- main page
- login, logut, authentication,
- change password for user
- user profile view
- user-profile edit
- customizable admin panel
- add Donate form view - working 1st, 2nd form views, 3rd in progress


#### To-Do-List:
 - in progress
 
#### Known issues:
- user redirection after login
- 

### Download and use it in your local environment:
- Fork repository
- Clone it into your computer
- Create virtualenv for the project, install requirements using: 
    ```sh
    $ pip install -r requirements.txt
    ```
- create file `local_settings.py` with your local configuration:
 ```python
DATABASES = {
        'default': {
            'HOST': 'localhost',
            'NAME': 'your_db_name',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'username',
            'PASSWORD': 'password',
        }
    }
    
EMAIL_HOST_USER = 'your_gmail_account'
    
EMAIL_HOST_PASSWORD = 'gmail_password'
    
E_MAIL_ADDRESS_USER = "address where you want to send messages"
    
    # Project e_mail variables in `settings.py` are configured 
    # to work with gmail by-default. If you want to use an another account,
    # you should read django documentation first :)
```
- create empty database in psql
- run `python manage.py makemigrations``python manage.py migrate`
- start test server.
### Enjoy :)
   