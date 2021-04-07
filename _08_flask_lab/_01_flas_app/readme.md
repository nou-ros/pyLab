#DevSynop
The synopsis of deshi devloper stories 

DevSynop is a Bangladeshi Online publisher focusing on the stories of techies/developers around the Bangladesh. Join with the community to know more... 

# workings
1. install flask - pip3 install flask (within a venv)
2. setup quick flask app build from official site and add debug true.
3. to run the file - python3 devsynop.py
4. templates setup:
-create a separate directory for templates
-template structures will be same as django template structure.
5. we can use flask forms to make forms. - pip3 install flask-wtf
6. We will require secret keys for forms. We can create secret keys by built in secrets module for simplicity.
- run python3 in terminal
- import secrets
- secrets.token_hex(16) # it is better to make secret keys environment variable.
We might need to install email validator for forms with - pip3 install email_validator

7. We use sqlite for development and switch to postgres later. pip3 install flask-sqlalchemy.
8. We made our project as a package. Install tree to see the package structure with: sudo apt install tree.
9. User authentication:
    > we used bcrypt to hash our auth data. To inatll bcrypt: pip3 install flask-bcrypt
    >from flask_bcrypt import Bcrypt
    >bcrypt = Bcrypt()
    >bcrypt.generate_password_hash('testing') will be in binary
    >bcrypt.generate_password_hash('testing').decode('utf-8') will be in string
    >hash password will be always different
    to check the password is correct we can use
    >bcrypt.check_password_hash(hash_pw, 'password'), if right password then return true
    > we used flask-login extension for login form check. pip3 install flask-login




