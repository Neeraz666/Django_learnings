from django.db import models

# Create your models here.
class Product(models.Model):

    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")   
    price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=300)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")


    def __str__(self):
        return self.product_name
    


    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=10, default="")
    desc = models.CharField(max_length=500, default="")   

    def __str__(self):
        return self.name
    


    
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    address_2= models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name + "'s Order"
    