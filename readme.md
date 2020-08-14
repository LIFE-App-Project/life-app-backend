install requirements into your virtual environment with the command 'pip install -r requirements.txt'


Admin Log In Details
USERNAME = admin
PASSWORD = admin

Please Ignore my env folder and create your own virtual environment on windows and install packages with the instruction above. (the env folder is linux based virtual environment)

URLs
    ACCOUNT URLs
        register = 127.0.0.1:8000/account/register
        login = 127.0.0.1:8000/account/login
        logout = 127.0.0.1:8000/account/logout
        change_password = 127.0.0.1:8000/account/password_change
        reset_password = 127.0.0.1:8000/account/password_reset
        edit_account = 127.0.0.1:8000/account/edit (admin can only be edited from the admin dashboard. You can create a new user and edit)
    
    COURSE URLs
        view course list = 127.0.0.1:8000/course/mine
        create a course = 127.0.0.1:8000/course/create (there are anchor tags to dynamically create and update modules.)