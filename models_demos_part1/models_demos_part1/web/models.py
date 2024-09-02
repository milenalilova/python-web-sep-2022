from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email_address = models.EmailField()
    works_full_time = models.BooleanField()
    job_level = models.CharField(max_length=20)
    # photo = models.URLField()
    birth_date = models.DateField()

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    # @property
    # def year_of_employment(self):
    #     return date.today() - self.start_date

    def __str__(self):
        # self.id == self.pk
        return f'Id: {self.pk}; Name: {self.fullname}'
