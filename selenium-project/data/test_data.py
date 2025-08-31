from utils.helpers import generate_random_email


SIGNUP_DATA = {
"valid_user": {
    "username": "test_user", 
     "email": generate_random_email(),
     "title": "Mr",
     "password": "passwordtest",
     "day": "18",
     "month": "May",
     "year": "1990"
     },

"invalid_email_user": {
    "username": "test_user",
    "email": "invalidemail.com",
    "password": "passwordtest"
},

}