from dataclasses import dataclass, replace
from faker import Faker
from utils.helpers import generate_random_email

fake = Faker()


@dataclass(frozen=True)
class User:
    username: str
    email: str
    title: str | None = None 
    password: str | None = None
    day: int | None = None
    month: str | None = None
    year: int | None = None
    first_name: str | None = None
    last_name: str | None = None
    company: str | None = None
    address: str | None = None
    address2: str | None = None
    country: str | None = None
    state: str | None = None
    city: str  | None = None
    zipcode: str | None = None
    mobile_number: str | None = None
    newsletter: bool = False
    special_offers: bool = False

def make_user(**overrides) -> User:
    base = User(
        username = fake.user_name(),
        email = generate_random_email(),
        title = fake.random_element(elements=("Mr", "Mrs")),
        password = fake.password(),
        day = fake.random_int(min=1, max=30),
        month = fake.month_name(),
        year = fake.random_int(min=1950, max=2010),
        first_name = fake.first_name(),
        last_name = fake.last_name(),
        company = fake.company(),
        address = fake.street_address(),
        address2 = fake.secondary_address(),
        country = fake.random_element(elements=("United States", "India", "Canada", "Australia", "Israel", "New Zealand", "Singapore")),
        state = fake.state(),
        city = fake.city(),
        zipcode = fake.zipcode(),
        mobile_number = fake.phone_number(),
    )
    return replace(base, **overrides)

