from django.db import models

# Create your models here.
# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        
        if not postData['name']:
            errors['name'] = "Course name is required."
        elif len(postData['name']) <= 5:
            errors['name'] = "Course name should be at least 5 characters."

        return errors


class Course(models.Model):
    # id INT
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

    def __repr__(self):
        return f"<Course object: {self.name} ({self.id})>"

class DescriptionManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        
        if not postData['desc']:
            errors['desc'] = "Course description is required."
        elif len(postData['desc']) <= 15:
            errors['desc'] = "Course name should be at least 15 characters."

        return errors

class Description(models.Model):
    # id INT
    desc = models.TextField()
    objects = DescriptionManager()

    def __repr__(self):
        return f"<Description object: {self.desc} ({self.id})>"

