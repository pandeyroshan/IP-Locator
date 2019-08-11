from django.shortcuts import render,redirect
import requests
# Create your views here.

def index(request):
    if request.method == 'POST':
        print('POST REQUEST')
        ipAddress = request.POST.get("ipAddress")
        requestURL = 'http://ip-api.com/json/'
        IPURL = requestURL+str(ipAddress)
        response = requests.get(IPURL)
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