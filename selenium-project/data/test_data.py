from utils.helpers import generate_random_email


SIGNUP_DATA = {
"valid_user": {
    "username": "test_user", 
     "email": generate_random_email(),
     "password": "passwordtest",
     
     },

"invalid_email_user": {
    "username": "test_user",
    "email": "invalidemail.com",
    "password": "passwordtest"
},

}