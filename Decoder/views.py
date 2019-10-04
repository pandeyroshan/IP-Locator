from django.shortcuts import render,redirect
import requests
# Create your views here.

def index(request):
    if request.method == 'POST':
        response = requests.get('http://ip-api.com/json/'+str(request.POST.get("ipAddress")))
        countryCode = response.json().get('countryCode')
        country = response.json().get('country')
        region = response.json().get('regionName')
        serviceProvider = response.json().get('isp')
        city = response.json().get('city')
        timezone = response.json().get('timezone')
        org = response.json().get('org')
        context = {
            'ipAddress' : ipAddress,
            'countryCode' : countryCode,
            'country' : country,
            'region' : region,
            'isp' : serviceProvider,
            'city' : city,
            'timezone' : timezone,
            'org' : org
        }
        print(context)
        return render(request,'Decoder/index.html',context)
    else:
        print('GET REQUEST')
        return render(request,'Decoder/index.html')
