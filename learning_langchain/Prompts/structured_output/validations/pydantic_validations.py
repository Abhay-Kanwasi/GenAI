from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class User(BaseModel):
    name: str # here you can also give default value | name: str  = 'abhay'
    age: Optional[int] = None # optional fields
    email: EmailStr # validation for email in pydantic (pydantic[email] install this module)
    performance_scale: float = Field(gt=0, lt=10, default=3, description='A decimal value representing the performance scale of the user') # limit constraints using Field it's greater than 0 and less than 10 default value is 3, description will tell about performance scale, we can also use regex

user_input = {
        "name" : 'John',
        "age" : 27, # even you give age in string '27' it will convert it into 27 as integer it's called Coerce
        "email" : 'abhay@gmail.com',
        "performance_scale" : 9
    }
new_user = User(**user_input)

print(new_user) # Returns pydantic object that can be converted in dictionary or json
print(dict(new_user)) # converted to dictionary
print(new_user.model_dump_json()) # converted to json

