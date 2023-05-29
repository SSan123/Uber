from django.db import models

# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length=18 , null=True , blank=True)
    last_name  = models.CharField(max_length=15 , null=True , blank=True)
    date_of_birth = models.DateField(max_length=8 , null=True , blank=True)
    mobile_number = models.IntegerField(max_length=10 , null=True , blank=True)

    GENDER_TYPES = (
        (1,'Male'),
        (2,'Female'),
        (3,'Other'),
    )
    gender_types = models.IntegerField(
        choices =  GENDER_TYPES
    
    )

    def __str__(self):
        return str(self.first_name)


class Orders(models.Model):
    
    order_name = models.CharField ( max_length=18 , null=True , blank=True)
    order_price = models.IntegerField ( max_length = 6 , null=True , blank=True)
    order_discount = models.IntegerField ( max_length= 2  , null=True , blank=True)
    order_quantity = models.IntegerField ( max_length = 2 , null=True , blank=True)
    order_address = models.TextField ( max_length = 18 , null=True , blank=True)
    order_at = models.DateField (  null=True , blank=True)

    def __str__(self):
        return str(self.order_name)


class StudentsAddress(models.Model):

    students = models.ForeignKey(Students,on_delete=models.CASCADE,null=True)
    street_name = models.CharField ( max_length=10 , null=True , blank=True )
    house_no = models.IntegerField ( max_length=2 , null=True , blank=True )
    city = models.CharField ( max_length=15 , null=True , blank=True )
    state = models.CharField ( max_length=15 , null=True , blank=True )
    country = models.CharField( max_length=12 , null=True , blank=True )
    pincode = models.IntegerField( max_length=6 , null=True , blank=True )

    def __str__(self):
        return str(self.street_name)