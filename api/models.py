from rest_framework import serializers
from django.db import models

# Create your models here. 
class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    agenda_slug = models.CharField(max_length=50,default='downtown_vi')
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    
    
    

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ()