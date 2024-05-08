from django.db import models


class Student(models.Model):
    st_no = models.PositiveBigIntegerField()
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=20)
    gpa = models.FloatField()

    def __str__(self):
        return f'Student: {self.fname} {self.lname}'
