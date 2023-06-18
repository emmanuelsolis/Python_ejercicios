from fastapi import APIRouter

user = APIRouter()

@user.get('/users')
def find_all_users():
    return "Helo cuate!"

@user.post('/users')
def create_user():
    return "Helo cuate!"

@user.get('/users/{id}')
def find_user():
    return "Helo cuate!"

@user.put('/users/{id}')
def update_user():
    return "Helo cuate!"

@user.delete('/users/{id}')
def delete_user():
    return "Helo cuate!"
