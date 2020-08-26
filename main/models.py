from django.db import models

# Create your models here.
# 학생 정보(이름, 학과, 입학년도, 학번, 평균 학점)
class Students(models.Model):
    name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    classof = models.CharField(max_length=50)
    average = models.CharField(max_length=50)

    def __str__(self):
        return self.name