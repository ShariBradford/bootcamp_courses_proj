from django.db import models

# Create your models here.
# Create your models here.
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

class CourseManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        
        if not postData['name']:
            errors['name'] = "Course name is required."
        elif len(postData['name']) <= 5:
            errors['name'] = "Course name should be at least 5 characters."
        elif len(self.filter(name__iexact = postData['name'])) > 0:
            errors['name'] = "Course name must be unique."

        #send the description field from the form to the Description validator
        descriptionErrors = Description.objects.basic_validator(postData)
        if descriptionErrors:
            #if the Description validator returned any errors, qdd them to our errors object
            for k,v in descriptionErrors.items():
                errors[k] = v

        return errors

class Course(models.Model):
    # id INT
    name = models.CharField(max_length=255)
    desc = models.OneToOneField(
        Description,
        on_delete=models.CASCADE,
        primary_key=False,
    )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

    def __repr__(self):
        return f"<Course object: {self.name} ({self.id})>"

class CommentManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        
        if not postData['content']:
            errors['content'] = "Comment is required."
        if not postData['course']:
            errors['course'] = "Course is required."

        return errors

class Comment(models.Model):
    # id INT
    course = models.ForeignKey(Course, related_name="comments", on_delete = models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CommentManager()

    def __repr__(self):
        return f"<Comment object: {self.content} ({self.id})>"
