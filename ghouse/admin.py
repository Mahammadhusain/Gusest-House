from django.contrib import admin
from .models import roomnumber,roomtype,roomprice,roomcondition,addnewroom,cregister,checkinmodel,payment,gstmodel, gappconfig, paymentmode

@admin.register(roomnumber)
class RoomNumberAdmin(admin.ModelAdmin):
    
    list_display = ['rnumber']

@admin.register(roomtype)
class RoomTypeAdmin(admin.ModelAdmin):
    
    list_display = ['rtype']

@admin.register(roomprice)
class RoomPriceAdmin(admin.ModelAdmin):
    
    list_display = ['rprice']

@admin.register(roomcondition)
class RoomConditionAdmin(admin.ModelAdmin):
    
    list_display = ['rcondition']

@admin.register(addnewroom)
class AddRoomAdmin(admin.ModelAdmin):
    
    list_display = ['rno','rtype','rprice','rcondition','rstatus']

@admin.register(cregister)
class CustomerRegisterAdmin(admin.ModelAdmin):
    
    list_display = ['registerno','fullname','companyname','designation','mobile','emailid','city','state','country','customer_id_type_1','proof_id_1','customer_id_type_2','proof_id_2','customer_id_type_3','proof_id_3','fulladdress','fullname',
            'companyname',
            'designation',
            'mobile',
            'emailid',
            'city',
            'state',
            'country',
            'fulladdress',
           
            
            
            ]

@admin.register(checkinmodel)
class CheckinRoomAdmin(admin.ModelAdmin):
    
    list_display = ['chno','chindate','chintime','choutdate','chouttime','chtotaldays','rno','rtype','rprice','person',
    'actualamount','roundamount','discount','gst',
    'extraperson','extrarate','totalextrarate','gstamount','totalamount','totalroomtarif','roomamount','foodbillamount',
    'laundybill',
    'phonebill',
    'Internetcharge',  
    'otherchargelable', 
    'othercharge',
    'discountamount',
    'advancepaidamount',
    'paybleamount',
     'fullname',
     'paymethod',
     'rstatus',
     
     
    
    
    ]

@admin.register(payment)
class PaymentAdmin(admin.ModelAdmin):
    
    list_display = ['person','actualamount','roundamount',]

@admin.register(gstmodel)
class GstAdmin(admin.ModelAdmin):
    
    list_display = ['gst',]

@admin.register(gappconfig)
class gappconfigAdmin(admin.ModelAdmin):
    
    list_display = ['appname','checkouttime','address','phone','email','applogo',]


@admin.register(paymentmode)
class paymentmodeAdmin(admin.ModelAdmin):
    
    list_display = ['paymethod']

    