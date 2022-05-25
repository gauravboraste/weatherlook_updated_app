from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render,redirect
import requests




def index(request):
   
    return render(request, "weather_api/home.html")

val = None
def result(request):
    if request.method == "POST":
       #get city name form input box
        city_name = request.POST["city"].lower()
        
        #api for get Four  houly forcaste date
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid=f70c947861e71f9a10374d879215247d"
        w_dataset = requests.get(url).json()

        #api for get current data 
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=f70c947861e71f9a10374d879215247d"
        dataset = requests.get(url).json()

        #global variable for same city  for previous data
        global val
        def val():
            return city_name
        
        try:
             context ={
                'data':w_dataset,
                'today':dataset,
                
            }
        except:
            context = {

            "city_name":"Not Found, Check your spelling..."
        }

        return render(request, "weather_api/results.html", context)
    else:
    	return redirect('home')
       

def previous(request):
    #get city name from global variable
        ok = val()
        #print("hello" + ok)

        #get data for latitide & longitude 
        url = f"https://api.openweathermap.org/data/2.5/weather?q={ok}&appid=f70c947861e71f9a10374d879215247d"
        
        data = requests.get(url).json()
       
        current_time =data["dt"]
        lat=data["coord"]["lat"]
        lon=data["coord"]["lon"]
        
      #api for get current and horly backcast data using latitide and lagitude 
        url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={current_time}&appid=f70c947861e71f9a10374d879215247d"
        
        w_dataset = requests.get(url).json()
        try:
            check = {
                  'prev':w_dataset,
                  'city':ok,
            }
        except:
           check = {

            "error":"Not Found, Check your spelling..."
        }
        return render(request, "weather_api/previous.html", check)
   

