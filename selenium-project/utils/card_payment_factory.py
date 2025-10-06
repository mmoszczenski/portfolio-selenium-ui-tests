from dataclasses import dataclass, replace
from faker import Faker

fake = Faker()

@dataclass(frozen=True)
class PaymentCard:
    name: str
    card_number: str
    cvc_number: int
    expiration_month: int
    expiration_year: int
    
    
def make_payment_card(**overrides) -> PaymentCard:
    base= PaymentCard(
        name = fake.first_name(),
        card_number = fake.credit_card_number(),
        cvc_number = fake.credit_card_security_code(),
        expiration_month = fake.credit_card_expire(date_format = '%m'),
        expiration_year = fake.credit_card_expire(date_format = '%Y')
    )

    return replace(base, **overrides)