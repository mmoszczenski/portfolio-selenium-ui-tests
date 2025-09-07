from utils.helpers import generate_random_email


SIGNUP_DATA = {

"valid_user": {
    "username": "test_user", 
     "email": generate_random_email(),
     "title": "Mr",
     "password": "passwordtest",
     "day": "18",
     "month": "May",
     "year": "1990",
     "first_name": "John",
     "last_name": "Doe",
     "company": "Apple Inc",
     "address": "Magazynowa 5",
     "address2": "80-200 Sopot",
     "country": "United States",
     "state": "Texas",
     "city": "Arizona",
     "zipcode": "81-377",
     "mobile_number": "512530800"
     },

"invalid_user_bad_email": {
    "username": "test_user",
    "email": "invalidemail.com",
    "password": "passwordtest",
    "day": "18",
    "month": "May",
    "year": "1990",
    "first_name": "John",
    "last_name": "Doe",
    "address": "Magazynowa5",
    "country": "United States",
    "state": "Texas",
    "city": "Arizona",
    "zipcode": "81-377",
    "mobile_number": "512530800"
},

"invalid_user_no_password": {
    "username": "test_user",
    "email": generate_random_email(),
    "password": "",
    "day": "18",
    "month": "May",
    "year": "1990",
    "first_name": "John",
    "last_name": "Doe",
    "address": "Magazynowa5",
    "country": "United States",
    "state": "Texas",
    "city": "Arizona",
    "zipcode": "81-377",
    "mobile_number": "512530800"
}, 

"invalid_user_empty_fields": {
    "username": "",
    "email": "",
    "password": "",
    "day": "",
    "month": "",
    "year": "",
    "first_name": "",
    "last_name": "",
    "address": "",
    "country": "",
    "state": "",
    "city": "",
    "zipcode": "",
    "mobile_number": ""
}

}