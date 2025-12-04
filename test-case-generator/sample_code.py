def divide(a, b):
    return a / b

def is_valid_age(age):
    return age >= 18

def greet(name):
    if not name:
        raise ValueError("Missing name")
    return f"Hello {name}"
