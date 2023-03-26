from users.models import User, Gender, UserEdit
from fastapi import FastAPI, HTTPException
from uuid import UUID, uuid4

# Initialise FastAPI 
app = FastAPI()


# Simple list for represent my fake data on db list
users: list[User] = [
  User(user_id=uuid4(),
    name="kadiatou Sow", 
    email="kadia@gmail.com", 
    age=29, 
    gender=Gender.female),
  User(
    user_id=uuid4(),
    name="Rougui Sow", 
    email="rougui@gmail.com", 
    age=19, 
    gender=Gender.female
  )
]



# Fetch all users
@app.get("/api/v1/users")
async def get_users():
  return users

# Create a new users
@app.post("/api/v1/users")
async def register_user(user: User):
  if user is not None:
    users.append(user)
    return HTTPException(
      status_code=201,
      detail=f"New user added with id: {user.user_id}"
    )
  return HTTPException(
    status_code=400,
    detail=f"Error to add user"
  )

# Get user By id
@app.get("/api/v1/users/{user_id}")
async def get_user(user_id: UUID):
  for user in users:
    if user.user_id == user_id:
      return user;
    return

# Delete user By Id
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
  for user in users:
    if user.user_id == user_id:
      users.remove(user)
      return
      

# Edit user fiels 
@app.put("/api/v1/users/{user_id}")
async def edit_user(user_id: UUID, userEdit: UserEdit):
  for user in users:
    if user.user_id == user_id:
      if user.name is not None:
        user.name = userEdit.name
      if user.email is not None:
        user.email = userEdit.email
      if user.age is not None:
        user.age = userEdit.age
      if user.gender is not None:
        user.gender = userEdit.gender
      
      