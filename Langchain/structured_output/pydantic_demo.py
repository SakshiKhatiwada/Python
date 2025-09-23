from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'sak'
    age: Optional[int] = None
    email: EmailStr
    cgpa: int = Field(gt=0, lt=10, default=5, description='CGPA of a student')
    
# new_st = {'age': "20"} # this will be implicitly converted as we gave it a type, called Type Coercing
# new_st = {'name': 'sakshi'}
new_st = {'age': 32, 'email': 'abc@gmail.com', 'cgpa': 1} # not even 10
student = Student(**new_st)
print(student)
# print(type(student))
print(student.name)
print(student.model_dump()) # to dict
print(student.model_dump_json()) # to json