# mine
from collections import namedtuple
student = namedtuple('Student', ['name', 'age', 'department'])
students = [student('Alina', '22', 'linguistics'),
            student('Alex', '25', 'programming'),
            student('Kate', '19', 'art')]

print(*students, sep='\n')
# Hyperskill user posted solution
from typing import NamedTuple
class Student(NamedTuple):
    name: str
    age: str
    department: str
    
print(Student('Alina', '22', 'linguistics'))
print(Student('Alex', '25', 'programming'))
print(Student('Kate', '19', 'art'))
