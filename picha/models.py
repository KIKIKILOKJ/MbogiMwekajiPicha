from django.db import models

# Create your models here.

class Location(models.Model):
    id
    picha_location = models.CharField(max_length=30)

    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()
    
    def update_location(self, update):
        self.photo_location = update
        self.save()
        
    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate

    def __str__(self):
        return self.photo_location
    
class Category(models.Model):
    picha_category = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    
    def update_category(self, update):
        self.photo_category = update
        self.save()
        
    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category

    def __str__(self):
        return self.photo_category

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    class Meta:
        ordering = ('-id',)
        
    def save_image(self):
            self.save()
    
    def delete_image(self):
        self.delete()
    
    def __str__(self):
        return self.name