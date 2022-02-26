from django.db import models
print("models.py")
# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    Is_active = models.BooleanField(default=True)


    class Meta:
        db_table = "book"

    def __str__(self):
        return f"{self.name}"    

 
 
class Employee(models.Model):  
    first_name = models.CharField(max_length=50)  
    last_name = models.CharField(max_length=50)  
    mobile = models.CharField(max_length=10)  
    email = models.EmailField()  
 
    
    class Meta:  
        db_table = "employee"  

    def __str__(self):
        return f"{self.first_name}"    
