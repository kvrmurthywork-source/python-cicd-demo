from app import welcome, add

def test_welcome():
    assert welcome() == "Welcome to GitHub CI/CD Pipeline!"

def test_add():
    assert add(10, 20) == 30

def test_add_negative():
    assert add(-5, 5) == 0
