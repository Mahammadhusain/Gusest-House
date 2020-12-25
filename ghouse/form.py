from django import forms
from .models import roomnumber,roomtype,roomprice,roomcondition,addnewroom,cregister,checkinmodel,payment,gstmodel,roomnumber, gstmodel, roomtype, gappconfig, paymentmode
# Only Room Number Add
class onlyroomno(forms.ModelForm):
    class Meta:
        model = roomnumber
        fields = ['rnumber']
        widgets = {
            'rnumber':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Room Number'}),
        }
        labels = {'rnumber':''}
        error_messages = {
            'rnumber':{
                'unique':'Room Number Already Exist',
                'required':'Enter Room Number',
                
                },
        }

# Only Room Categories
class onlyroomcate(forms.ModelForm):
    class Meta:
        model = roomtype
        fields = ['rtype']
        widgets = {
            'rtype':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Room Category Name'}),
        }
        labels = {'rtype':''}
        error_messages = {
            'rtype':{
                'unique':'Room Category Already Exist',
                'required':'Enter Room Category Name',
                
                },
        }
    # Validate Category If Exist (Display Error)
    def clean_rtype(self):
        rcate = self.cleaned_data['rtype']
        if roomtype.objects.filter(rtype=rcate).exists():
            raise forms.ValidationError('Category Already Exist') 
        return rcate 

# Only Room Categories
class onlyroomprice(forms.ModelForm):
    class Meta:
        model = roomprice
        fields = ['rprice']
        widgets = {
            'rprice':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Room Price'}),
        }
        labels = {'rprice':''}
        error_messages = {
            'rprice':{
                'unique':'Room Price Already Exist',
                'required':'Enter Room Price',
                
                },
        }
    # Validate Category If Exist (Display Error)
    def clean_rprice(self):
        rpri = self.cleaned_data['rprice']
        if roomprice.objects.filter(rprice=rpri).exists():
            raise forms.ValidationError('Price Already Exist') 
        return rpri 

# GST Form
class gstform(forms.ModelForm):
    class Meta:
        model = gstmodel
        fields = ['gst']
        widgets = {
            'gst':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter GST Ex: (8.5)'}),
        }
        labels = {'gst':''}
        error_messages = {
            'gst':{
                'unique':'Gst Already Exist',
                'required':'Enter Gst in (%)',
                
                },
        }
    # Validate GST If Exist (Display Error)
    def clean_gst(self):
        rgst = self.cleaned_data['gst']
        if gstmodel.objects.filter(gst=rgst).exists():
            raise forms.ValidationError('Gst Already Exist') 
        return rgst







# Room Adding Form
roomno = roomnumber.objects.values_list('rnumber','rnumber').order_by('rnumber')
roomty = roomtype.objects.values_list('rtype','rtype')
roompr = roomprice.objects.values_list('rprice','rprice')
roomcond = roomcondition.objects.values_list('rcondition','rcondition')

class AddRoomForm(forms.ModelForm):
    class Meta:
        model = addnewroom
        fields = ['rno','rtype','rprice','rcondition',]

        widgets={
            'rno':forms.Select(choices=roomno,attrs={'class':'form-select'}),
            'rtype':forms.Select(choices=roomty,attrs={'class':'form-select'}),
            'rprice':forms.Select(choices=roompr,attrs={'class':'form-select'}),
            'rcondition':forms.Select(choices=roomcond,attrs={'class':'form-select'}),
        }
        error_messages ={
            'rno':{'unique':'Room Already Exist'}
        }



id_1 = [('PAN CARD', 'PAN CARD'),]
id_2 = [('ELECTION CARD', 'ELECTION CARD'),]
id_3 = [('AADHAR CARD', 'AADHAR CARD'),]  



# Customer Registration Form
class CustomerRegister(forms.ModelForm):
    class Meta:
        model = cregister
        fields = ['fullname','companyname','designation','mobile','emailid','city','state','country','customer_id_type_1','proof_id_1','customer_id_type_2','proof_id_2','customer_id_type_3','proof_id_3','fulladdress',]

        widgets={
            'fullname':forms.TextInput(attrs={'class':'form-control','placeholder':'Fullname',}),
            'companyname':forms.TextInput(attrs={'class':'form-control','placeholder':'Companyname'}),
            'designation':forms.TextInput(attrs={'class':'form-control','placeholder':'Designation'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobile'}),
            'emailid':forms.EmailInput(attrs={'class':'form-control','placeholder':'E-Mail'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),
            'state':forms.TextInput(attrs={'class':'form-control','placeholder':'State'}),
            'country':forms.TextInput(attrs={'class':'form-control','placeholder':'Country'}),
            'customer_id_type_1':forms.Select(choices=id_1,attrs={'class':'form-select'}),
            # 'proof_id_1':forms.FileInput(attrs={'type':'file','class':'form-control',}),
            'customer_id_type_2':forms.Select(choices=id_2,attrs={'class':'form-select'}),
            # 'proof_id_2':forms.FileInput(attrs={'type':'file','class':'form-control',}),
            'customer_id_type_3':forms.Select(choices=id_3,attrs={'class':'form-select'}),
            # 'proof_id_3':forms.FileInput(attrs={'type':'file','class':'form-control',}),
            'fulladdress':forms.Textarea(attrs={'style':'height: 80px','class':'form-control','placeholder':'Full Address'}),
        }

# Room Choices
chrno = addnewroom.objects.values_list('rno','rno')
chrtype = addnewroom.objects.values_list('rtype','rtype')
chrprice = addnewroom.objects.values_list('rprice','rprice')

# Customer Choices
chfullname = cregister.objects.values_list('fullname','fullname')[::-1]
chcompanyname = cregister.objects.values_list('companyname','companyname')[::-1]
chdesignation = cregister.objects.values_list('designation','designation')[::-1]
chmobile = cregister.objects.values_list('mobile','mobile')[::-1]
chemailid = cregister.objects.values_list('emailid','emailid')[::-1]
chcity = cregister.objects.values_list('city','city')[::-1]
chstate = cregister.objects.values_list('state','state')[::-1]
chcountry = cregister.objects.values_list('country','country')[::-1]
chfulladdress = cregister.objects.values_list('fulladdress','fulladdress')[::-1]

# Payment Choices
chperson = payment.objects.values_list('person','person')
chactualamount = payment.objects.values_list('actualamount','actualamount')
chroundamount = payment.objects.values_list('roundamount','roundamount')

# Gst Details
chgst = gstmodel.objects.values_list('gst','gst')
# chdiscount = payment.objects.values_list('discount','discount')

# Pay Mode
chpaymode = paymentmode.objects.values_list('paymethod','paymethod')[::-1]

# Check-In Form
class CheckinForm(forms.ModelForm):
    class Meta:
        model = checkinmodel
        fields = [
            'chno',
            'chindate',
            'chintime',
            'choutdate',
            'chouttime',

            # Room Details
            'rno',
            'rtype',
            'rprice',

            # Customer Details
            'fullname',
            'companyname',
            'designation',
            'mobile',
            'emailid',
            'city',
            'state',
            'country',
            'fulladdress',

            # Payment
            'person',
            'totalamount',
            'actualamount',
            'finalamount',
            'roundamount',
            'chtotaldays',
            'extraperson',
            'extrarate',
            'totalextrarate',
            # 'extradays',

            # Other Bills & Chargers
            'advancepaidamount',
            'paybleamount',
            'totalroomtarif',
            'roomamount',
            'gstamount',
            'foodbillamount',
            'laundybill',
            'phonebill',
            'Internetcharge',  
            'otherchargelable', 
            'othercharge',

            # Gst Deatils
            'gst',
            'gstshow',
            'discount',
            'discountamount',
            'paymethod',



            
        ]
        error_messages = {
            'choutdate':{'required':'Please Enter Check-Out Date'},
            'chouttime':{'required':'Please Enter Check-Out Time'}
        }

        widgets = {
            # Check-In Details
            'chno':forms.NumberInput(attrs={'class':'form-control','readonly':'',}),
            'chindate':forms.DateInput(attrs={'class':'form-control','type': 'date','readonly':''}),
            'chintime':forms.TimeInput(attrs={'class':'form-control','type': 'time','readonly':''},),
            'choutdate':forms.DateInput(attrs={'class':'form-control','type': 'date'},),
            'chouttime':forms.TimeInput(attrs={'class':'form-control','type': 'time','step':'1'},),

            # Room Details
            'rno':forms.Select(choices=chrno,attrs={'class':'form-control','readonly':''},),
            'rtype':forms.Select(choices=chrtype,attrs={'class':'form-control','readonly':''}),
            'rprice':forms.Select(choices=chrprice,attrs={'class':'form-control','readonly':''}),

            # Customer Details
            'fullname':forms.Select(choices=chfullname,attrs={'class':'form-select','readonly':True}),
            'companyname':forms.Select(choices=chcompanyname,attrs={'class':'form-select',}),
            'designation':forms.Select(choices=chdesignation,attrs={'class':'form-select',}),
            'mobile':forms.Select(choices=chmobile,attrs={'class':'form-select',}),
            'emailid':forms.Select(choices=chemailid,attrs={'class':'form-select',}),
            'city':forms.Select(choices=chcity,attrs={'class':'form-select',}),
            'state':forms.Select(choices=chstate,attrs={'class':'form-select',}),
            'country':forms.Select(choices=chcountry,attrs={'class':'form-select',}),
            'fulladdress':forms.Select(choices=chfulladdress,attrs={'class':'form-select',}),

            # Payment Details
            'person':forms.Select(choices=chperson,attrs={'class':'form-control','readonly':''}),
            'totalamount':forms.NumberInput(attrs={'class':'form-control',}),
            'actualamount':forms.Select(choices=chactualamount,attrs={'class':'form-control',}),
            'finalamount':forms.NumberInput(attrs={'class':'form-control',}),
            'roundamount':forms.Select(choices=chroundamount,attrs={'class':'form-control',}),
            'extraperson':forms.NumberInput(attrs={'class':'form-control',}),
            'totalextrarate':forms.NumberInput(attrs={'class':'form-control',}),
            'extrarate':forms.NumberInput(attrs={'class':'form-control','placeholder':' Per Person Rate (Ex:-1 Person = ₹ 300)'}),
            # 'extradays':forms.NumberInput(attrs={'class':'form-control',}),

            # Other Bills & Charges
            'advancepaidamount':forms.NumberInput(attrs={'class':'form-control',}),
            'paybleamount':forms.NumberInput(attrs={'class':'form-control',}),
            'totalroomtarif':forms.NumberInput(attrs={'class':'form-control',}),
            'roomamount':forms.NumberInput(attrs={'class':'form-control',}),
            'gstamount':forms.NumberInput(attrs={'class':'form-control',}),
            'foodbillamount':forms.NumberInput(attrs={'class':'form-control',}),
            'laundybill':forms.NumberInput(attrs={'class':'form-control',}),
            'phonebill':forms.NumberInput(attrs={'class':'form-control',}),
            'Internetcharge':forms.NumberInput(attrs={'class':'form-control',}),  
            'otherchargelable':forms.TextInput(attrs={'class':'form-control',}), 
            'othercharge':forms.NumberInput(attrs={'class':'form-control',}),
            
            # Gst Details
            'gst':forms.Select(choices=chgst,attrs={'class':'form-control',}),
            'gstshow':forms.NumberInput(attrs={'class':'form-control',}),
            'discount':forms.NumberInput(attrs={'class':'form-control',}),
            'discountamount':forms.NumberInput(attrs={'class':'form-control',}),
            'paymethod':forms.Select(choices=chpaymode,attrs={'class':'form-control',}),



        }
    def clean_choutdate(self):
        # self.cleaned_data = super().clean()
        chindate = self.cleaned_data['chindate']
        choutdate = self.cleaned_data['choutdate']
        if choutdate <= chindate:
            raise forms.ValidationError(f'Enter Check-Out Date ({choutdate}) Must be Grater Then Check-In Date ({chindate})')
        return choutdate


class appconfigform(forms.ModelForm):
    class Meta:
        model = gappconfig
        fields = ['appname','checkouttime','address','phone','email','applogo',]
        labels = {
            'appname':'',
            'checkouttime':'',
            'address':'',
            'phone':'',
            'email':'',
            'applogo':''}
        widgets = {
            'appname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Application Name'}),
            'checkouttime':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Time Ex:- (10:00:00 AM / PM)'}),
            'address':forms.Textarea(attrs={'style':'height: 113px','class':'form-control mt-3','placeholder':'Enter full adderss of your guest house'}),
            'phone':forms.NumberInput(attrs={'class':'form-control mt-3','placeholder': 'Enter phone number'}),
            'email':forms.EmailInput(attrs={'class':'form-control mt-3','placeholder': 'Enter E-Mail'}),
            'applogo':forms.FileInput(attrs={'class':'form-control mt-3'}),
        }
       

class paymethodform(forms.ModelForm):
    class Meta:
        model = paymentmode
        fields = ['paymethod']
        widgets = {
            'paymethod':forms.TextInput(attrs={'class':'form-control'})
        }

        labels = {'paymethod':''}
        error_messages = {
            'rtype':{
                'unique':'Room Category Already Exist',
                
                },
        }
    # Validate Paymode If Exist (Display Error)
    def clean_paymethod(self):
        pay = self.cleaned_data['paymethod']
        if paymentmode.objects.filter(paymethod=pay).exists():
            raise forms.ValidationError('Payment Mode Already Exist') 
        return pay 