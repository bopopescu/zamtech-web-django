from django.db import models
from django.utils import timezone

# Create your models here.
gender_choices = (
    (('M', 'Male'), ('F', 'Female'), ('P', 'Parody'))
)
# users profile models
class users(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=128, null=True)
    username = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=128, null=True, unique=True)
    gender = models.CharField(choices=gender_choices, max_length=1, null=True)
    create_date = models.DateTimeField(default=timezone.now)