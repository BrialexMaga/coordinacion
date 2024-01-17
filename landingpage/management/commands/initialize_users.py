from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps

class Command(BaseCommand):
    help = 'Inicializa grupos y permisos para usuarios'

    def handle(self, *args, **options):
        admin_group, created_admin = Group.objects.get_or_create(name='Administradores')
        common_user_group, created_common = Group.objects.get_or_create(name='Usuarios')

        if created_admin  or admin_group.permissions.exists():
            admin_group.permissions.clear()

            for model in apps.get_models():
                content_type = ContentType.objects.get_for_model(model)
                permissions = Permission.objects.filter(content_type=content_type)
                for permission in permissions:
                    admin_group.permissions.add(permission)

        if created_common or common_user_group.permissions.exists():
            common_user_group.permissions.clear()
            
            contact_model = apps.get_model('studentform', 'Contact')
            contact_content_type = ContentType.objects.get_for_model(contact_model)
            contact_permissions = Permission.objects.filter(content_type=contact_content_type, codename__in=['add_contact', 'view_contact', 'change_contact'])
            for permission in contact_permissions:
                common_user_group.permissions.add(permission)
            
            for model in apps.get_models():
                if model != contact_model:
                    content_type = ContentType.objects.get_for_model(model)
                    view_permission = Permission.objects.get(content_type=content_type, codename='view_' + model.__name__.lower())
                    common_user_group.permissions.add(view_permission)

        self.stdout.write(self.style.SUCCESS('Grupos y permisos inicializados con éxito'))