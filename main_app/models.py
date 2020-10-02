from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name



# Ways to create data:
# 1. Through forms in the app
# 2. Through the Django/Python shell (python3 manage.py shell)
# 3. Through the psql shell
# 4. Through the admin panel at /admin