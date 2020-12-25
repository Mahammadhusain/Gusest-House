from django.db import models
from datetime import datetime,date,time

# Room Number.
class roomnumber(models.Model):
    rnumber = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.rnumber)

# Room Type
class roomtype(models.Model):
    rtype = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return str(self.rtype)

# Room Price
class roomprice(models.Model):
    rprice = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return str(self.rprice)

# Room Condition
class roomcondition(models.Model):
    rcondition = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return str(self.rcondition)

# Adding New Room
class addnewroom(models.Model):
    rno = models.IntegerField(primary_key=True)
    rtype = models.CharField(max_length=100)
    rprice = models.IntegerField()
    rcondition = models.CharField(max_length=100)
    rstatus = models.BooleanField(default=False)
    
    objects = models.Manager()

    def __str__(self):
        return str(self.rno)


# Customer Register
class cregister(models.Model):
    registerno = models.IntegerField(primary_key=True,blank=True)
    fullname = models.CharField(max_length=500)
    companyname = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    mobile = models.PositiveIntegerField()
    emailid = models.EmailField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100,default='India')
    customer_id_type_1 = models.CharField(max_length=200,null=True,blank=True)
    proof_id_1 = models.ImageField(upload_to='photo/%Y/%m/%d',null=True,blank=True)
    customer_id_type_2 = models.CharField(max_length=200,null=True,blank=True)
    proof_id_2 = models.ImageField(upload_to='photo/%Y/%m/%d',null=True,blank=True)
    customer_id_type_3 = models.CharField(max_length=200,null=True,blank=True)
    proof_id_3 = models.ImageField(upload_to='photo/%Y/%m/%d',null=True,blank=True)
    fulladdress = models.TextField(max_length=500)
    in_date = models.DateField(auto_now_add=True)
    in_time = models.DateTimeField(auto_now_add=True)
    
    
    objects = models.Manager()

    def __str__(self):
        return str(self.fullname)


# Check-In 
class checkinmodel(models.Model):
   
    # Check-In Details
    chno = models.IntegerField(primary_key=True,blank=True,serialize=True,)
    chindate = models.DateField(default=datetime.now().strftime('%Y-%m-%d'),)
    chintime = models.TimeField(default=datetime.now().strftime('%H:%M:%S'),)
    choutdate = models.DateField()
    chouttime = models.TimeField()
    # he = models.CharField(max_length=10)

    # Room Details
    rno = models.IntegerField()
    rtype = models.CharField(max_length=100)
    rprice = models.IntegerField()
    rstatus = models.BooleanField(default=False)

    # Customer Details
    fullname = models.CharField(max_length=500)
    companyname = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    mobile = models.PositiveIntegerField()
    emailid = models.EmailField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100,default='India')
    fulladdress = models.TextField(max_length=500)

    # Payment details
    chtotaldays = models.CharField(max_length=100,blank=True)
    person = models.IntegerField()
    extraperson = models.IntegerField(default=0)
    extrarate = models.IntegerField(default=0)
    totalextrarate = models.IntegerField(default=0,null=True,blank=True)
    extradays = models.IntegerField(default=1)
    totalamount = models.FloatField(null=True,blank=True)
    actualamount = models.FloatField(null=True,blank=True)
    finalamount = models.DecimalField(default=0,blank=True,decimal_places=2,max_digits=6)
    roundamount = models.IntegerField(null=True,blank=True)
    advancepaidamount = models.IntegerField(default=0,null=True)
    paybleamount = models.IntegerField(null=True,blank=True)
    
    # Other Bills & Charges
    totalroomtarif = models.IntegerField(default=0,blank=True)
    roomamount = models.IntegerField(default=0,blank=True)
    gstamount = models.DecimalField(default=0,blank=True,decimal_places=2,max_digits=6)
    foodbillamount = models.IntegerField(default=0)
    laundybill = models.IntegerField(default=0)
    phonebill = models.IntegerField(default=0)
    Internetcharge = models.IntegerField(default=0)
    otherchargelable = models.CharField(blank=True,max_length=100)
    othercharge = models.IntegerField(default=0,null=True,blank=True)

    # Gst Details
    gst = models.FloatField(null=True,blank=True)
    gstshow = models.FloatField(null=True,blank=True)
    discount = models.IntegerField(default=0,blank=True)
    discountamount = models.FloatField(null=True,blank=True)
    paymethod = models.CharField(max_length=200,default='Cash')


    objects = models.Manager()

    def __str__(self):
        return str(self.chno)


   



class payment(models.Model):
    person = models.IntegerField()
    actualamount = models.DecimalField(null=True,blank=True,decimal_places=4,max_digits=9)
    roundamount = models.DecimalField(null=True,blank=True,decimal_places=1,max_digits=9)
    
    
    objects = models.Manager()

    def __str__(self):
        return str(self.person)

class gstmodel(models.Model):
    gst = models.DecimalField(max_digits=5,decimal_places=1)
    
    objects = models.Manager()

    def __str__(self):
        return str(self.gst)


class gappconfig(models.Model):
    appname = models.CharField(max_length=200,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    phone = models.IntegerField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    applogo = models.ImageField(blank=True,null=True)
    checkouttime = models.CharField(max_length=200)
    objects = models.Manager()

    objects = models.Manager()

    def __str__(self):
        return str(self.appname)

class paymentmode(models.Model):
    paymethod = models.CharField(max_length=200,default='Cash')

    objects = models.Manager()

    def __str__(self):
        return str(self.paymethod)