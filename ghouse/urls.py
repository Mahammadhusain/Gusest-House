from django.urls import path
from .views import AddRooms, DeleteRoom, EditRoom, DisplayAllRooms, CRegister, RCheckin,nevappname, dashboard, editcheckin, deletecheckin, checkeddetails, vacantroom, addonlyroom, deleteroomnumber, addonlyCategories, deleteroomCategories, addonlyPrice, deleteroomPrice, addgst, deletegst, ghouseconfig, billing, checkinhistory, cutomerhistory, customerfullinfo, editcregister, deletecregister, addpaymode, deletePaymode, monthlysell, Paymodedatewise


urlpatterns = [

    # App Title
    path('nevappname/',nevappname,name='nevappname'),

    # Dashboard
    path('dashboard/', dashboard, name='dashboard'),

    # Full Checked-In Details
    path('checkeddetails/<int:id>/', checkeddetails, name='checkeddetails'),

    # Make Room Vacant
    path('vacantroom/<int:id>/', vacantroom, name='vacantroom'),

    # Rooms Control
    path('AddRooms/', AddRooms, name='AddRooms'),
    path('DeleteRoom/<int:id>/', DeleteRoom, name='AddRooms'),
    path('EditRoom/<int:id>/', EditRoom, name='EditRoom'),


    # Display All Rooms For Check-In
    path('DisplayAllRooms/', DisplayAllRooms, name='DisplayAllRooms'),


    # Customer Register
    path('CRegister/', CRegister, name='CRegister'),
    path('editcregister/<int:id>/',editcregister,name='editcregister'),
    path('deletecregister/<int:id>/',deletecregister,name='deletecregister'),


    # Room Checkin
    path('CheckinForm/<int:id>/', RCheckin, name='RCheckin'),
    path('editcheckinRoomTrue/<int:id>/', editcheckin, name='editcheckin'),
    path('deletecheckin/<int:id>/', deletecheckin, name='deletecheckin'),
    path('checkeddetails/<int:id>/', checkeddetails, name='checkeddetails'),


    # Only Add & Delete Rooms Numbers
    path('addonlyroom/', addonlyroom, name='addonlyroom'),
    path('deleteroomnumber/<int:id>/', deleteroomnumber, name='deleteroomnumber'),

    # Only Add & Delete Rooms Categories
    path('addonlyCategories/', addonlyCategories, name='addonlyCategories'),
    path('deleteroomCategories/<int:id>/',
         deleteroomCategories, name='deleteroomCategories'),


    # Only Add & Delete Rooms Price
    path('addonlyPrice/', addonlyPrice, name='addonlyPrice'),
    path('deleteroomPrice/<int:id>/', deleteroomPrice, name='deleteroomPrice'),


    # Only Add & Delete Pay Modes
    path('addpaymode/', addpaymode, name='addpaymode'),
    path('deletePaymode/<int:id>/', deletePaymode, name='deletePaymode'),

    # Add GST (%)
    path('addgst/', addgst, name='addgst'),
    path('deletegst/<int:id>/', deletegst, name='deletegst'),

    # Update Application Config
    path('ghouseconfig/<int:id>/', ghouseconfig, name='ghouseconfig'),

    # Checked-In history
    path('checkinhistory/', checkinhistory, name='checkinhistory'),

    # Customer History
    path('cutomerhistory/',cutomerhistory,name='cutomerhistory'),

    # Customer Full Information
    path('customerfullinfo/<int:id>/',customerfullinfo,name='customerfullinfo'),


    # Billing
    path('billing/<int:id>/', billing, name='billing'),




# =====================================================================================
#                                     URLS FOR ALL TYPES REPORT
# =====================================================================================
    # Monthly Room Selling
    path('monthlysell/',monthlysell,name='monthlysell'),
    path('Paymodedatewise/',Paymodedatewise,name='Paymodedatewise'),









]
