from django.db import models

class Subject(models.Model):
    code = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name


class Lecture(models.Model):
    day = models.IntegerField()
    duration = models.IntegerField()
    lecturer = models.CharField(max_length=100)
    time = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject.code} - {self.lecturer}"


class Practice(models.Model):
    day = models.IntegerField()
    duration = models.IntegerField()
    practice_teacher = models.CharField(max_length=100)
    time = models.IntegerField()
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    def __str__(self):
        return self.practice_teacher
    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
