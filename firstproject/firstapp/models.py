from django.db import models

# Create your models here.


class Login(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return 'Login by {0}'.format(self.name)
#__init__
#__new__
#__dict_
# login.save()


class Company(models.Model):
    company_name = models.CharField(max_length=40)
    company_location = models.CharField(max_length=100)
    company_city = models.CharField(max_length=20)

    def __str__(self):
        return self.company_name


class Employee(models.Model):
    employee_name = models.CharField(max_length=20)
    employee_salary = models.IntegerField()
    employee_company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='employee')
    employee_manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,related_name='team_member')

    def __str__(self):
        return self.employee_name

