from dataclasses import dataclass, replace
from faker import Faker
from pathlib import Path

fake = Faker()

PROJECT_ROOT = Path(__file__).resolve().parent.parent



@dataclass(frozen=True)
class ContactForm:
    name: str
    email: str
    subject: str
    message: str
    attachment: Path | None = None
    
def make_contact_form_data(**overrides) -> ContactForm:
    base = ContactForm(
        name = fake.name(),
        email = fake.email(),
        subject = fake.text(max_nb_chars=30),
        message = fake.text(),
        attachment=PROJECT_ROOT / "assets" / "samplefile.jpg"
    )
    return replace(base, **overrides)