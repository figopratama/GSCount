from django.shortcuts import render
from django.contrib import messages
from .models import UjiStasioner
#from .resources import UjiStasionerResource
#from tablib import Dataset
#import csv,io
from django.template import loader
from statsmodels.tsa.stattools import adfuller
#from ..crm.models import Date


# Create your views here.

#def count(request):
#    if request.method == 'POST':
#        songrank_resource = UjiStasionerResource()
#        dataset = Dataset()
#        new_songrank = request.FILES['myfile']

#       if not new_songrank.name.endswith('csv'):
#            messages.info(request,'Please Upload the CSV File only')
#            return render(request,'home.html')

#        data_set = new_songrank.read().decode('UTF-8')
#        io_string = io.StringIO(data_set)
#        next(io_string)
#        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
#            created = UjiStasioner.objects.update_or_create(
#                stat=column[0],
#                value=column[1],
#                crit=column[2])
#    return render(request, 'count.html')

def count(request):
    if request.method == 'POST':
#       mydata = Date.objects.all().values()
        mydata = [4, 7, 9, 4, 10]
        for i in mydata:
            result = adfuller(mydata[i], regression='ct', autolag='AIC')
            created = UjiStasioner.objects.create(
                stat=result[0],
                value=result[1],
                crit=result[2])
#        context = {
#            'hasil_uji': mydata,
#        }

    
        
    return render(request, 'count.html')