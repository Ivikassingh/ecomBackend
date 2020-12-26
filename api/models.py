from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    price=models.IntegerField()
    description = models.CharField(max_length=400, blank=True, null=True)
    link = models.CharField(max_length=100,blank=True, null=True)
    category = models.ForeignKey('Category', related_name='Category', on_delete=models.CASCADE)
    source = models.CharField(max_length=100,blank=True, null=True)
    linkId=models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)


class LinkMapper(models.Model):
    id=models.IntegerField(primary_key = True)
    original = models.CharField(max_length=200,blank=True, null=True)
    generated = models.CharField(max_length=200,blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.generated


class LinkStats(models.Model):
    linkname = models.ForeignKey('LinkMapper', related_name='LinkDetails', on_delete=models.CASCADE)
    visitCount= models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True) 
