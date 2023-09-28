from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save, sender=Profile)
def add_user_to_student_group(sender, instance, created, **kwargs):
    if created:
        try:
            students = Group.objects.get(name='Estudiantes')
        except Group.DoesNotExist:
            students = Group.objects.create(name='Estudiantes')
            students = Group.objects.create(name='Profesores')
            students = Group.objects.create(name='Bedel')
            students = Group.objects.create(name='Administrativo')
        instance.user.groups.add(students)

