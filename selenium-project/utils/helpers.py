import uuid

def generate_random_email(domain: str = "example.com") -> str:
    return f"user_{uuid.uuid4().hex[:12]}@{domain}"

