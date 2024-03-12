import factory
from factory import post_generation
import random
from .models import Student, Contact, Status, School_Cycle, Career, Syllabus
from studenthistory.models import Section, GradePeriod, Course

#from .factories import CourseFactory

class CourseFactory(factory.Factory):
    class Meta:
        model = Course

    school_cycle = factory.LazyAttribute(lambda _: School_Cycle.objects.get(year=2023, cycle_period='B'))
    grade = factory.Faker('random_int', min=50, max=100)
    grade_period = factory.LazyAttribute(lambda _: GradePeriod.objects.get(code_name='OE'))
    upload_date = factory.Faker('date_this_year')


class StudentFactory(factory.Factory):
    class Meta:
        model = Student
    
    code = factory.Faker('random_int', min=210000000, max=300000000)
    name = factory.Faker('name')
    first_last_name = factory.Faker('last_name')
    second_last_name = factory.Faker('last_name')
    status = factory.LazyAttribute(lambda _: Status.objects.get(code_name='AC'))
    exchange = factory.Faker('boolean', chance_of_getting_true=0)
    admission_cycle = factory.LazyAttribute(lambda _: School_Cycle.objects.get(year=2023, cycle_period='B'))
    last_cycle = factory.LazyAttribute(lambda _: School_Cycle.objects.get(year=2023, cycle_period='B'))
    idCareer = factory.LazyAttribute(lambda _: Career.objects.get(code_name='INCO'))
    syllabus = factory.LazyAttribute(lambda _: Syllabus.objects.get(name='2016'))


class ContactFactory(factory.Factory):
    class Meta:
        model = Contact

    phone = factory.Faker('phone_number')
    email = factory.Faker('email')
    udg_email = factory.Faker('email')
    emergency_phone = factory.Faker('phone_number')
    url_socialnet = factory.Faker('url')