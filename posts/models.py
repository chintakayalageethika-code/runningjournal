from django.db import models

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('training', 'Training Log'),
        ('race', 'Race Day'),
        ('community', 'Community'),
        ('volunteering', 'Volunteering'),
    ]

    title = models.CharField(max_length=200)
    story = models.TextField()
    distance = models.FloatField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    date = models.DateField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='training')
    bib_number = models.CharField(max_length=20, blank=True, null=True)
    finish_time = models.CharField(max_length=20, blank=True, null=True)
    volunteer_event = models.CharField(max_length=200, blank=True, null=True)
    volunteer_role = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title