
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Choices for the type field
FIRST_APP_CHOICE = [
    ('ITEM ', 'TEST-1'),
    ('ITEM ', 'TEST-2'),
    ('ITEM ', 'TEST-3'),
    ('ITEM ', 'TEST-4'),
    ('ITEM ', 'TEST-5'),
]


class multipleVarient(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='firstApp/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(
        max_length=10,
        choices=FIRST_APP_CHOICE
    )
    description = models.TextField(default='')

    def __str__(self):
        return self.name


# one to many

class ItemReview(models.Model):
    item = models.ForeignKey(multipleVarient, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.item.name}'

    #many to mnay 

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    item_details = models.ManyToManyField(multipleVarient, related_name='sotres')
    
    def __str__(self):
        return self.name

# One to one

class ItemCertificate(models.Model):
    item = models.OneToOneField(multipleVarient, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(default=timezone.now)
    valid_untill = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.chai}'
