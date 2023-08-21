from django.db import models

# Create your models here.
STATE_CHOICE = ((
    ('Bihar', 'Bihar'),
    ('Up', 'Up'),
    ('Goa', 'Goa')
))
GENDER = ((
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
))

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(auto_now=False)
    state = models.CharField(choices=STATE_CHOICE, max_length=150)
    gender = models.CharField(choices=GENDER, max_length=150)
    location = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to='pimages', blank=True)
    rdoc = models.FileField(upload_to='rdocs', blank = True)

    def __str__(self):
        return f"profile: {self.name}"