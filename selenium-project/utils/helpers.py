import uuid

def generate_random_email(domain="example.com"):
    return f"user_{uuid.uuid4().hex[:8]}@{domain}"

