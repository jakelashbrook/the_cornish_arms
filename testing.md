<h1>Testing through production</h1>

## Login, Logout and Register 
Using allauth and settings.py I initially made use of a variety of settings to control the authentication 
processes.
 - ### From allauth settings 
    - #### login with email or username only
        ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
    - #### email address required
        ACCOUNT_EMAIL_REQUIRED = True
    - #### verifying email mandatory
        ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
    - #### enter email twice to register
        ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
    - #### password must be entered twice on sign up
        ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
    - #### minimum 4 characters for username
        ACCOUNT_USERNAME_MIN_LENGTH = 4
    - #### usernames not accepted on signup
        ACCOUNT_USERNAME_BLACKLIST = ['admin', 'owner']
    - #### amount of login attempts allowed before timeout
        ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
    - #### amount of secs to wait before next login allowed
        ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
    - #### asks the user if they wish to be remembered
        ACCOUNT_SESSION_REMEMBER = None
    - #### login url
        LOGIN_URL = '/accounts/login/'
    - #### redirects to  homepage after login
        LOGIN_REDIRECT_URL = '/'
        - to test this was working i initially changed the path to success and then ran the server with
        the accounts/login path. This returned an error 404 but /success was displayed in the browser.