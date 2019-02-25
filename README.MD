# oddaj_rzeczy - portfolio_lab project <br>
Portfolio lab project - description in progress...

#### 25.02.2019 - what is working:
- project first configuration
- main page
- login, logut, authentication,
- activation via email
- change password for user
- password reset via email
- user profile view
- user-profile edit
- user Donates view
- Donate details - in progress
- password verification
- customizable admin panel
- Add Donates by User - full View (with fields remember)


#### To-Do-List:
 - Finish Donate Details
 - change donate status : delivered/undelivered
 - sites administrators management
 
#### Known issues:
- Donates Validation
- probably much more than that...

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
   