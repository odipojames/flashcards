from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import card_save
 

# Create your models here.

class Card(models.Model): 
    id = models.primary_key=True
    title = models.CharField(max_length=50,blank=True)
    Description= models.CharField(max_length=250,blank=True)
    subject = models.CharField(max_length=250,blank=True)
    user=models.ManyToManyField(User,related_name='card')
    image = models.ImageField(upload_to='cards')
    postedon = models.DateTimeField(auto_now_add=True)
        

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
    
    @classmethod
    def save_card(self):
        self.save()
    @classmethod
    def get_cards(cls):
         cards = cls.objects.all()
         return cards
    @classmethod
    def delete_card(self):
        self.delete()
    
    def save_image(self):
        self.save()

    @classmethod
    def delete_image_by_id(cls, id):
        pictures = cls.objects.filter(pk=id)
        pictures.delete()

    @classmethod
    def get_image_by_id(cls, id):
        pictures = cls.objects.get(pk=id)
        return pictures