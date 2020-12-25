from django.shortcuts import render, redirect
from .models import addnewroom, checkinmodel, cregister, roomnumber, roomtype, roomprice, gstmodel, gappconfig, paymentmode
from .form import AddRoomForm, CustomerRegister, CheckinForm, onlyroomno, onlyroomcate, onlyroomprice, gstform, appconfigform, paymethodform
from django.contrib import messages
from datetime import date, time, datetime
from .filters import filtercheckinhistory, filtercustomerhistory, monthlysellingrpt
from django.db.models import Sum

# Nevbar App Name


def nevappname(request):
    # Nevbar Appname
    apptitle = gappconfig.objects.all()
    return render(request, 'base.html', apptitle)


# Dashboard
def dashboard(request):
    # Desplay Date & Time

    if request.user.is_authenticated:
        # Check-Out TIme
        couttime = gappconfig.objects.all()

        # For Date & Time
        showtime = datetime.today()

        # Count Customer
        countcustmer = cregister.objects.all().count()

        # Counting Rooms Categoies-wise
        non_ac = addnewroom.objects.filter(rtype='Non-Ac').count()
        ac = addnewroom.objects.filter(rtype='Ac').count()
        pre = addnewroom.objects.filter(rtype='Premium').count()
        todayoccu = checkinmodel.objects.all().order_by(
            'rno').filter(chindate=datetime.today()).count()

        # Dispaly Today's Check-In Details
        checkindata = checkinmodel.objects.all().order_by(
            'rno').filter(chindate=datetime.today())
        context = {'couttime': couttime, 'showtime': showtime, 'checkindata': checkindata,
                   'non_ac': non_ac, 'ac': ac, 'pre': pre, 'todayoccu': todayoccu, 'countcustmer': countcustmer}
        return render(request, 'dashboard.html', context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')


# Make Room Vacant
def vacantroom(request, id):
    if request.user.is_authenticated:
        vacant = addnewroom.objects.get(pk=id)
        vacant.rstatus = False
        vacant.save()
        return redirect('/DisplayAllRooms/')
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')


# Add Room View
def AddRooms(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            RoomData = addnewroom.objects.all().order_by('rno')
            RoomForm = AddRoomForm(request.POST)
            if RoomForm.is_valid():
                RoomForm.save()
                showrno = RoomForm.cleaned_data['rno']
                messages.info(request, 'Room SuccessFully Added')
                context = {'RoomForm': RoomForm,
                           'showrno': showrno, 'RoomData': RoomData}
                return render(request, 'roomcontrol.html', context)
        else:
            RoomData = addnewroom.objects.all().order_by('rno')
            RoomForm = AddRoomForm()
        context = {'RoomForm': RoomForm, 'RoomData': RoomData}
        return render(request, 'roomcontrol.html', context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')


def EditRoom(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = addnewroom.objects.get(pk=id)
            RoomForm = AddRoomForm(request.POST, instance=data)
            if RoomForm.is_valid():
                RoomForm.save()
                # showrno = RoomForm.cleaned_data['rno']
                messages.info(request, 'Room Information SuccessFully Updated')
                # context = {'RoomForm':RoomForm,'RoomData':RoomData,'showrno':showrno}
                return redirect('/AddRooms/')
                # return render(request,'roomcontrol.html',context)
        else:
            RoomData = addnewroom.objects.all().order_by('rno')
            data = addnewroom.objects.get(pk=id)
            RoomForm = AddRoomForm(instance=data)
            context = {'RoomForm': RoomForm, 'RoomData': RoomData}
        return render(request, 'roomcontrol.html', context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')


# Delete Room Details
def DeleteRoom(request, id):
    if request.user.is_authenticated:
        RoomData = addnewroom.objects.get(pk=id)
        p = addnewroom.objects.get(pk=id)
        RoomData.delete()
        messages.info(request, f'{p}Room Successfully Deleted')
        return redirect('/AddRooms/')
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')

# All Rooms-Display For Check-In View


def DisplayAllRooms(request):
    if request.user.is_authenticated:
        DisplayAllData = addnewroom.objects.all()
        return render(request, 'allroomsdisplay.html', {'DisplayAllData': DisplayAllData})
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')


# Customer Register View
def CRegister(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            CustomerRegisterNo = cregister.objects.all().count()
            CustomerRegisterForm = CustomerRegister(
                request.POST, request.FILES)
            if CustomerRegisterForm.is_valid():
                CustomerRegisterForm.save()
                CustomerRegisterForm = CustomerRegister()
                messages.info(request, 'Customer Successfully Registred')
                context = {'CustomerRegisterForm': CustomerRegisterForm,
                           'CustomerRegisterNo': CustomerRegisterNo}
                return render(request, 'cregister.html', context)
        else:
            CustomerRegisterForm = CustomerRegister()
            CustomerRegisterNo = cregister.objects.all().count()
        context = {'CustomerRegisterForm': CustomerRegisterForm,
                   'CustomerRegisterNo': CustomerRegisterNo}
        return render(request, 'cregister.html', context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')


def editcregister(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            CustomerRegisterNo = cregister.objects.get(pk=id)
            CustomerRegisterForm = CustomerRegister(
                request.POST, request.FILES, instance=CustomerRegisterNo)
            if CustomerRegisterForm.is_valid():
                CustomerRegisterForm.save()
                messages.info(request, 'Customer SuccessFully Updated')
                return redirect('/cutomerhistory/')
        else:
            CustomerRegisterNo = cregister.objects.get(pk=id)
            CustomerRegisterForm = CustomerRegister(
                instance=CustomerRegisterNo)
        context = {'CustomerRegisterForm': CustomerRegisterForm}
        return render(request, 'cregister.html', context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')


def deletecregister(request, id):
    if request.user.is_authenticated:
        deletecregister = cregister.objects.get(pk=id)
        deletecregister.delete()
        messages.error(request, 'Customer Successfully Deleted')
        return redirect('/cutomerhistory/')
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')


# Room Check View
def RCheckin(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            RoomData = addnewroom.objects.get(pk=id)
            RoomCheckinForm = CheckinForm(
                request.POST or None, instance=RoomData)

            if RoomCheckinForm.is_valid():

                # Check-In Details
                chno = RoomCheckinForm.cleaned_data['chno']
                chindate = RoomCheckinForm.cleaned_data['chindate']
                chintime = RoomCheckinForm.cleaned_data['chintime']
                choutdate = RoomCheckinForm.cleaned_data['choutdate']
                chouttime = RoomCheckinForm.cleaned_data['chouttime']
                # chtotaldays = RoomCheckinForm.cleaned_data['chtotaldays']
 
                # Count Day Between (Check-In Date) & (Check-Out Date) 
                fdays = choutdate - chindate
                fdays.days

                # Room Details
                rno = RoomCheckinForm.cleaned_data['rno']
                rtype = RoomCheckinForm.cleaned_data['rtype']
                rprice = RoomCheckinForm.cleaned_data['rprice']

                # Customer Details
                fullname = RoomCheckinForm.cleaned_data['fullname']
                companyname = RoomCheckinForm.cleaned_data['companyname']
                designation = RoomCheckinForm.cleaned_data['designation']
                mobile = RoomCheckinForm.cleaned_data['mobile']
                emailid = RoomCheckinForm.cleaned_data['emailid']
                city = RoomCheckinForm.cleaned_data['city']
                state = RoomCheckinForm.cleaned_data['state']
                country = RoomCheckinForm.cleaned_data['country']
                fulladdress = RoomCheckinForm.cleaned_data['fulladdress']

                # Payment Details
                person = RoomCheckinForm.cleaned_data['person']
                extraperson = RoomCheckinForm.cleaned_data['extraperson']
                extrarate = RoomCheckinForm.cleaned_data['extrarate']
                totalextrarate = RoomCheckinForm.cleaned_data['totalextrarate']
                # extradays = RoomCheckinForm.cleaned_data['extradays']
                actualamount = RoomCheckinForm.cleaned_data['actualamount']
                roundamount = RoomCheckinForm.cleaned_data['roundamount']
                paymethod = RoomCheckinForm.cleaned_data['paymethod']

                # Extra Bills & Charges
                advancepaidamount = RoomCheckinForm.cleaned_data['advancepaidamount']
                paybleamount = RoomCheckinForm.cleaned_data['paybleamount']
                amount = RoomCheckinForm.cleaned_data['roomamount']
                roomamount = RoomCheckinForm.cleaned_data['roomamount']
                foodbillamount = RoomCheckinForm.cleaned_data['foodbillamount']
                laundybill = RoomCheckinForm.cleaned_data['laundybill']
                phonebill = RoomCheckinForm.cleaned_data['phonebill']
                Internetcharge = RoomCheckinForm.cleaned_data['Internetcharge']
                otherchargelable = RoomCheckinForm.cleaned_data['otherchargelable']
                othercharge = RoomCheckinForm.cleaned_data['othercharge']

                # Gst Details
                discount = RoomCheckinForm.cleaned_data['discount']
                dubdiscount = RoomCheckinForm.cleaned_data['discount']
                gst = RoomCheckinForm.cleaned_data['gst']

                # ------------------------------------------------------------------------
                        # Calculations
                # ------------------------------------------------------------------------
                
                # Display GST in Bill (%)
                showgst = gst

                # Per Person Rate (Extra Person) * (Extra Rate)
                totalextrarate = ((extraperson)*(extrarate))
                
                

                # Calculate Room Tariff With Deafult Person & Extra Person
                roomamount = ((rprice)*(fdays.days)+((totalextrarate)))


                # Total Room Tarrif
                totalroomtarif = (rprice)*(fdays.days)


                # (Room Total + All Chargers)
                totalamount = ((roomamount) + (foodbillamount)+(laundybill) +
                (phonebill)+(Internetcharge)+(othercharge))
                
                
                # Discount (%) Converted In Rupee Of (Room Total + All Chargers)
                discountamount = (totalamount*discount)/(100)

                # Room Total & All Chargers (Room Total + All Chargers)
                actualamount = ((totalamount)-(discountamount))

                # Calculate GST
                gst = gst/100

                # Convert GST (%) in Rupee
                gstamount = ((actualamount)*(gst))

                # Subtracting (Actual-Amount)
                finalamount = ((actualamount)+(gstamount))

                # Rounding (Final Amount)
                roundamount = round(finalamount)

                # Calculate Payable Amount (Round-Amount) - (Advance-Paid Amount)
                paybleamount = (roundamount)-(advancepaidamount)



                # Saving All Data in Check-In Table  
                finaldata = checkinmodel(

                    # Check-In Details
                    chno=chno,
                    chindate=chindate,
                    chintime=chintime,
                    choutdate=choutdate,
                    chouttime=chouttime,
                    chtotaldays=fdays.days,

                    # Room Details
                    rno=rno,
                    rtype=rtype,
                    rprice=rprice,

                    # Customer Details
                    fullname=fullname,
                    companyname=companyname,
                    designation=designation,
                    mobile=mobile,
                    emailid=emailid,
                    city=city,
                    state=state,
                    country=country,
                    fulladdress=fulladdress,

                    # Payment Details
                    person=person,
                    totalamount=totalamount,
                    actualamount=actualamount,
                    finalamount=finalamount,
                    roundamount=roundamount,
                    paymethod=paymethod,

                    # Extra Details
                    extraperson=extraperson,
                    extrarate=extrarate,
                    totalextrarate=totalextrarate,
                    # extradays=extradays,

                    # Extra Bills & Charges
                    advancepaidamount=advancepaidamount,
                    paybleamount=paybleamount,
                    gstamount=gstamount,
                    totalroomtarif=totalroomtarif,
                    roomamount=roomamount,
                    foodbillamount=foodbillamount,
                    laundybill=laundybill,
                    phonebill=phonebill,
                    Internetcharge=Internetcharge,
                    otherchargelable=otherchargelable,
                    othercharge=othercharge,

                    # Gst Details
                    gst=showgst,
                    gstshow=showgst,
                    discount=discount,
                    discountamount=discountamount,


                )

                finaldata.save()

                # Make Room Occupied
                RoomData.rstatus = True
                RoomData.save()

                # Display Days Between (Check-In Date) & (Check-Out Date)
                showtotaldays = finaldata.chtotaldays

                # Display (Actual Amount)&(Round Amount)
                showactualamount = finaldata.actualamount
                showroundamount = finaldata.roundamount
                # showdiscount = finaldata.discount

                messages.info(request, f'{rno} - Room Successfully Checked-In')
                context = {
                    'RoomCheckinForm': RoomCheckinForm,
                    'rno': rno,
                    'showtotaldays': showtotaldays,
                    'showactualamount': showactualamount,
                    'showroundamount': showroundamount,
                    'amount': amount,
                    'dubdiscount': dubdiscount,

                }
                return render(request, 'checkin.html', context)
        else:

            RoomData = addnewroom.objects.get(pk=id)
            RoomCheckinForm = CheckinForm(instance=RoomData)
        context = {'RoomCheckinForm': RoomCheckinForm, }
        return render(request, 'checkin.html', context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')


def editcheckin(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            RoomData = checkinmodel.objects.get(pk=id)
            RoomCheckinForm = CheckinForm(request.POST, instance=RoomData)
            if RoomCheckinForm.is_valid():
                rno = RoomCheckinForm.cleaned_data['rno']
                chindate = RoomCheckinForm.cleaned_data['chindate']
                choutdate = RoomCheckinForm.cleaned_data['choutdate']
                rprice = RoomCheckinForm.cleaned_data['rprice']
                extraperson = RoomCheckinForm.cleaned_data['extraperson']
                extrarate = RoomCheckinForm.cleaned_data['extrarate']
                totalextrarate = RoomCheckinForm.cleaned_data['totalextrarate']
                # extradays = RoomCheckinForm.cleaned_data['extradays']
                foodbillamount = RoomCheckinForm.cleaned_data['foodbillamount']
                laundybill = RoomCheckinForm.cleaned_data['laundybill']
                phonebill = RoomCheckinForm.cleaned_data['phonebill']
                Internetcharge = RoomCheckinForm.cleaned_data['Internetcharge']
                othercharge = RoomCheckinForm.cleaned_data['othercharge']
                discount = RoomCheckinForm.cleaned_data['discount']
                totalamount = RoomCheckinForm.cleaned_data['totalamount']
                finalamount = RoomCheckinForm.cleaned_data['finalamount']
                paybleamount = RoomCheckinForm.cleaned_data['paybleamount']
                advancepaidamount = RoomCheckinForm.cleaned_data['advancepaidamount']
                paymethod = RoomCheckinForm.cleaned_data['paymethod']
                gst = RoomCheckinForm.cleaned_data['gst']

                # Display GST in Bill (%)
                showgst = gst


                
                # Stop Saving Data
                RoomCheckinForm = RoomCheckinForm.save(commit=False)

                # Cleaning & Count TOTAL DAYS
                fdays = choutdate - chindate
                fdays.days
                RoomCheckinForm.chtotaldays = fdays.days

                totalroomtarif = (rprice)*(fdays.days)


                # Per Person Rate (Extra Person) * (Extra Rate)
                totalextrarate = ((extraperson)*(extrarate))
                
                

                # Update Total Room Amount (Tarrif * Total days)
                RoomCheckinForm.roomamount = ((rprice)*(fdays.days)+((totalextrarate)))

                # Total Amount (Without GST)
                totalamount = ((RoomCheckinForm.roomamount) +
                               (foodbillamount)+(laundybill) +
                               (phonebill)+(Internetcharge)+(othercharge))

                # Discount (%) Converted In Rupee Of (Room Total + All Chargers)
                discountamount = (totalamount*discount)/(100)

                
                # Room Total & All Chargers (Room Total + All Chargers)
                actualamount = ((totalamount)-(discountamount))

                # Calculate GST
                gst = gst/100

                # Convert GST (%) in Rupee
                gstamount = ((actualamount)*(gst))

                # Subtracting (Actual-Amount)
                finalamount = ((actualamount)+(gstamount))

                # Rounding (Final Amount)
                roundamount = round(finalamount)

                # Calculate Payable Amount (Round-Amount) - (Advance-Paid Amount)
                paybleamount = (roundamount)-(advancepaidamount)

                # Cleaning & UPDATE ACTUAL-AMOUNT & ROUND-AMOUNT
                # RoomCheckinForm.extradays = extradays
                RoomCheckinForm.totalroomtarif = totalroomtarif
                RoomCheckinForm.totalextrarate = totalextrarate
                RoomCheckinForm.gstshow = showgst
                RoomCheckinForm.totalamount = totalamount
                RoomCheckinForm.gstamount = gstamount
                RoomCheckinForm.finalamount = finalamount
                RoomCheckinForm.actualamount = actualamount
                RoomCheckinForm.discountamount = discountamount
                RoomCheckinForm.roundamount = roundamount
                RoomCheckinForm.paybleamount = paybleamount
                RoomCheckinForm.paymethod = paymethod
                RoomCheckinForm.save()
                messages.info(request, f'{rno} - SuccessFully Updated')
                return redirect('/dashboard/')
        else:
            RoomData = checkinmodel.objects.get(pk=id)
            RoomCheckinForm = CheckinForm(instance=RoomData)
        context = {'RoomCheckinForm': RoomCheckinForm}
        return render(request, 'checkin.html', context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')


def deletecheckin(request, id):
    if request.user.is_authenticated:
        checkindata = checkinmodel.objects.get(pk=id)
        checkindata.delete()
        messages.error(request, f'{checkindata.rno} - Successfully Deleted')
        return redirect('/checkinhistory/')
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')


# view all Checked-In Room Details
def checkeddetails(request, id):
    if request.user.is_authenticated:
        checkinfullinfo = checkinmodel.objects.filter(pk=id)
        return render(request, 'checkedininfo.html', {'checkinfullinfo': checkinfullinfo})
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')


# Add Only Room Number
def addonlyroom(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            addroom = onlyroomno(request.POST)
            roomdata = roomnumber.objects.all()
            if addroom.is_valid():
                rnum = addroom.cleaned_data['rnumber']
                dat = roomnumber(rnumber=rnum)
                dat.save()
                messages.info(request, 'Room Successfully Added')
                context = {'addroom': addroom,
                           "roomdata": roomdata, "rnum": rnum}
                return render(request, 'onlyroom.html', context)
        else:
            addroom = onlyroomno()
            roomdata = roomnumber.objects.all()
        context = {'addroom': addroom, "roomdata": roomdata, }
        return render(request, 'onlyroom.html', context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')


# Add Only Pay Mode
def addpaymode(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            addpay = paymethodform(request.POST)
            paydata = paymentmode.objects.all()
            if addpay.is_valid():
                pmode = addpay.cleaned_data['paymethod']
                dat = paymentmode(paymethod=pmode)
                dat.save()
                messages.info(request, 'Payment Mode Successfully Added')
                context = {'addpay': addpay,
                           "paydata": paydata, "pmode": pmode}
                return render(request, 'onlyroom.html', context)
        else:
            addpay = paymethodform()
            paydata = paymentmode.objects.all()
        context = {'addpay': addpay, "paydata": paydata, }
        return render(request, 'onlypaymode.html', context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')

# Delete Paymode


def deletePaymode(request, id):
    if request.user.is_authenticated:
        paydata = paymentmode.objects.get(pk=id)
        paydata.delete()
        messages.error(request, 'Successfully Deleted')
        return redirect('/addpaymode/')
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')


# Delete Room Number
def deleteroomnumber(request, id):
    if request.user.is_authenticated:
        roomdata = roomnumber.objects.get(pk=id)
        roomdata.delete()
        messages.error(request, 'Successfully Deleted')
        return redirect('/addonlyroom/')
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')


# Add Only Categories
def addonlyCategories(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            addCategories = onlyroomcate(request.POST)
            roomdata = roomtype.objects.all()
            if addCategories.is_valid():
                rtype = addCategories.cleaned_data['rtype']
                dat = roomtype(rtype=rtype)
                dat.save()
                messages.info(request, 'Room Successfully Added')
                context = {'addCategories': addCategories,
                           "roomdata": roomdata, }
                return render(request, 'onlycategories.html', context)
        else:
            addCategories = onlyroomcate()
            roomdata = roomtype.objects.all()
        context = {'addCategories': addCategories, "roomdata": roomdata, }
        return render(request, 'onlycategories.html', context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')

# Delete Room Categories


def deleteroomCategories(request, id):
    if request.user.is_authenticated:
        roomdata = roomtype.objects.get(pk=id)
        roomdata.delete()
        messages.error(request, 'Successfully Deleted')
        return redirect('/addonlyCategories/')
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')


# Add Only Price
def addonlyPrice(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            addPrice = onlyroomprice(request.POST)
            roomdata = roomprice.objects.all()
            if addPrice.is_valid():
                rprice = addPrice.cleaned_data['rprice']
                dat = roomprice(rprice=rprice)
                dat.save()
                messages.info(request, 'Room Price Successfully Added')
                context = {'addPrice': addPrice, "roomdata": roomdata, }
                return render(request, 'onlyprice.html', context)
        else:
            addPrice = onlyroomprice()
            roomdata = roomprice.objects.all()
        context = {'addPrice': addPrice, "roomdata": roomdata, }
        return render(request, 'onlyprice.html', context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')

# Delete Room Price


def deleteroomPrice(request, id):
    if request.user.is_authenticated:
        roomdata = roomprice.objects.get(pk=id)
        roomdata.delete()
        messages.error(request, 'Successfully Deleted')
        return redirect('/addonlyPrice/')


# Add GST
def addgst(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            addGST = gstform(request.POST)
            roomdata = gstmodel.objects.all()
            if addGST.is_valid():
                rgst = addGST.cleaned_data['gst']
                dat = gstmodel(gst=rgst)
                dat.save()
                messages.info(request, 'GST Successfully Added')
                context = {'addGST': addGST, "roomdata": roomdata, }
                return render(request, 'gst.html', context)
        else:
            addGST = gstform()
            roomdata = gstmodel.objects.all()
        context = {'addGST': addGST, "roomdata": roomdata, }
        return render(request, 'gst.html', context)


# Delete Room Price
def deletegst(request, id):
    if request.user.is_authenticated:
        roomdata = gstmodel.objects.get(pk=id)
        roomdata.delete()
        messages.error(request, 'Successfully Deleted')
        return redirect('/addgst/')


# Set (Address), (Phone no), (G-house Name)
def ghouseconfig(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            configdata = gappconfig.objects.get(pk=id)
            updateconfig = appconfigform(request.POST, instance=configdata)
            configalldata = gappconfig.objects.all()
            if updateconfig.is_valid():
                updateconfig.save()
                messages.info(request, 'Details Updated')
            context = {'updateconfig': updateconfig,
                       'configalldata': configalldata}
            return render(request, 'ghouseconfig.html', context)
        else:
            configdata = gappconfig.objects.get(pk=id)
            updateconfig = appconfigform(instance=configdata)
            configalldata = gappconfig.objects.all()
        context = {'updateconfig': updateconfig,
                   'configalldata': configalldata}
        return render(request, 'ghouseconfig.html', context)


# Billing Details
def billing(request, id):
    if request.user.is_authenticated:
        billconfig = gappconfig.objects.all()
        checkininfo = checkinmodel.objects.filter(pk=id)
        context = {'billconfig': billconfig, 'checkininfo': checkininfo}
        return render(request, 'billing.html', context)


# Filter Check-In Full History
def checkinhistory(request):
    if request.user.is_authenticated:
        # data = checkinmodel.
        history = checkinmodel.objects.all().order_by('chindate')
        counthistory = checkinmodel.objects.all().count()
        filterhistory = filtercheckinhistory(request.GET, queryset=history)
        history = filterhistory.qs
        fiteredcount = filterhistory.qs.count()

        context = {'history': history, 'filterhistory': filterhistory,
                   'counthistory': counthistory, 'fiteredcount': fiteredcount}

        return render(request, 'checkedinhistory.html', context)


#  Filter Customer history
def cutomerhistory(request):
    if request.user.is_authenticated:
        chistory = cregister.objects.all().order_by('in_date')
        cufilter = filtercustomerhistory(request.GET, queryset=chistory)
        chistory = cufilter.qs
        context = {'chistory': chistory, 'cufilter': cufilter}
        return render(request, 'customerhistory.html', context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')


# Customer Full Information
def customerfullinfo(request, id):
    if request.user.is_authenticated:
        fullinfo = cregister.objects.filter(pk=id)
        context = {'fullinfo': fullinfo}
        return render(request, 'customerfullinfo.html', context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/login')


# =====================================================================================
#                                      ALL TYPES REPORT
# =====================================================================================

# Mothly Date-wise Selling Report
def monthlysell(request):
    alldata = checkinmodel.objects.all()
    filterdata = monthlysellingrpt(request.GET, queryset=alldata)
    alldata = filterdata.qs

    sumofpaybleamount = alldata.aggregate(Sum('paybleamount'))[
        'paybleamount__sum']
    showgst = checkinmodel.objects.all()

    context = {'alldata': alldata, 'filterdata': filterdata,
               'sumofpaybleamount': sumofpaybleamount, 'showgst': showgst}
    return render(request, 'monthlysellingreport.html', context)

# Paymode Date-wise Selling Report


def Paymodedatewise(request):
    alldata = checkinmodel.objects.all()
    filterdata = monthlysellingrpt(request.GET, queryset=alldata)
    alldata = filterdata.qs

    sumofpaybleamount = alldata.aggregate(Sum('paybleamount'))[
        'paybleamount__sum']
    showgst = checkinmodel.objects.all()

    context = {'alldata': alldata, 'filterdata': filterdata,
               'sumofpaybleamount': sumofpaybleamount, 'showgst': showgst}
    return render(request, 'paymodereport.html', context)
