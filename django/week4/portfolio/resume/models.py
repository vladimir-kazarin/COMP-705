from django.db import models


class Resume(models.Model):
    first_name = models.CharField(max_length=64)
    last_name =models.CharField(max_length=64)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def last_name_first(self):
        return "{}, {}".format(self.last_name, self.first_name)

    def get_education(self):
        return self.education_set.all()

    def get_experience(self):
        return self.experience_set.all()

class Experience(models.Model):
    parent_resume = models.ForeignKey(
        'Resume',
        on_delete=models.CASCADE, 
        default=1
    )
    title = models.CharField(max_length=64)
    company = models.CharField(max_length=64)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    parent_resume = models.ForeignKey(
        'Resume',
        on_delete=models.CASCADE, 
        default=1
    )
    institution_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    gpa = models.FloatField()

    def __str__(self):
        return self.institution_name