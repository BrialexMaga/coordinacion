import factory
from .models import Student

class StudentFactory(factory.Factory):
    class Meta:
        model = Student
    
    code = factory.faker('random_int', min=210000000, max=300000000)
    name = factory.faker('name')
    status = factory.Faker('random_element', elements=['activo', 'inactivo', 'art 34', 'art 35'])