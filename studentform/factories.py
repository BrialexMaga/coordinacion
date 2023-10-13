import factory
import random
from .models import Student, Contact

class StudentFactory(factory.Factory):
    class Meta:
        model = Student
    
    code = factory.Faker('random_int', min=210000000, max=300000000)
    name = factory.Faker('name')
    status = factory.Faker('random_element', elements=['activo', 'inactivo', 'art 34', 'art 35'])
    
    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        min_num = 2010
        max_num = 2023
        random_num = random.randint(min_num, max_num)
        elements = ['A', 'B']
        random_element = random.choice(elements)
        admission_cycle = f'{random_num}{random_element}'

        kwargs['admission_cycle'] = admission_cycle

        return super(StudentFactory, cls)._create(model_class, *args, **kwargs)
    
class ContactFactory(factory.Factory):
    class Meta:
        model = Contact

    phone = factory.Faker('phone_number')
    email = factory.Faker('email')
    udg_email = factory.Faker('email')
    emergency_phone = factory.Faker('phone_number')