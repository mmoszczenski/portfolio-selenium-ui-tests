import requests

class APIHelperUser:
    def __init__(self, base_url="https://automationexercise.com/api"):
        self.base_url = base_url.rstrip("/")
        
    def create_user(
        self,
        name,
        email,
        password,
        title=None,
        birth_date=None,
        birth_month=None,
        birth_year=None,
        firstname=None,
        lastname=None,
        company=None,
        address1=None,
        address2=None,
        country=None,
        zipcode=None,
        state=None,
        city=None,
        mobile_number=None
    ):
        
        payload = {
            "name": name,
            "email": email,
            "password": password,
        }