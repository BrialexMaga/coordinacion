from django.core.management.base import BaseCommand
from studentform.factories import StudentFactory

class Command(BaseCommand):
    help = 'Crea estudiantes aleatorios'

    def add_arguments(self, parser):
        parser.add_argument('num_students', type=int, help='Indica el numero de estudiantes creados')

    def handle(self, *args, **options):
        num_students = options['num_students']
        students = StudentFactory.create_batch(num_students)
        for student in students:
            student.save()
        self.stdout.write(self.style.SUCCESS(f'{num_students} estudiantes creados exitosamente!'))