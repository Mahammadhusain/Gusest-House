import django_filters
from .models import checkinmodel,cregister


class filtercheckinhistory(django_filters.FilterSet):
    fullname = django_filters.CharFilter(label='Customer Name',lookup_expr='icontains',label_suffix='')
    fromdate = django_filters.DateFilter(field_name='chindate',label='From Date',lookup_expr='gte',label_suffix='')
    todate = django_filters.DateFilter(field_name='chindate',label='To Date',lookup_expr='lte',label_suffix='')
    class Meta:
        model = checkinmodel
        fields = ['fullname',]
        

class filtercustomerhistory(django_filters.FilterSet):
    regisdate = django_filters.DateFilter(label='Register Date',field_name='in_date',label_suffix='',)
    class Meta:
        model = cregister
        fields = ['fullname']



# =====================================================================================
#                                      ALL TYPES REPORT FILTERS
# =====================================================================================

class monthlysellingrpt(django_filters.FilterSet):
    fromdate = django_filters.DateFilter(label='From Date',field_name='choutdate',lookup_expr='gte')
    todate = django_filters.DateFilter(label='To Date',field_name='choutdate',lookup_expr='lte')
    
    class Meta:
        model = checkinmodel
        fields = []
       