from django.db import models



GENDER_FIELD = (
    ("M", "MALE"),
    ("F", "FEMALE")
)



class Course(models.Model):
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=50, default="3 months")
    about_course = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()


    def __str__(self):
        return self.title
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_FIELD, max_length=2)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name
    

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course_teaching = models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__ (self):
        return self.name


class Admission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} registered"
