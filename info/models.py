from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField

class Home(models.Model):
    full_name = models.CharField(max_length=50, blank=True, null=True)
    # img = models.ImageField(upload_to="portrait/", blank=True, null=True)
    short_bio = models.TextField(blank=True, null=True)

    # Social Network
    github    = models.URLField(blank=True, null=True)
    # linkedin  = models.URLField(blank=True, null=True)
    facebook  = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter   = models.URLField(blank=True, null=True)
    # youtube   = models.URLField(blank=True, null=True)
    # discord   = models.URLField(blank=True, null=True)

    # show_on_page = ChoiceField()

    def __str__(self):
        return self.full_name


class About(models.Model):
    about = models.TextField(blank=True, null=True)
    time_since = models.DateField(blank=False, null=False)
    time_to = models.DateField(blank=True, null=True)
    work_place = models.CharField(blank=False, null=False, max_length=100)
    job = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False, max_length=5000)


class Project(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    img = CloudinaryField('image')
    # img = models.ImageField(upload_to="projects/", blank=False, null=False)
    demo = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    # show_on_page = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Contact(models.Model):
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
