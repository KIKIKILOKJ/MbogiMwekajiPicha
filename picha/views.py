from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from .models import Image,Location

# Create your views here.
# def welcome(request):
#     return render(request,'welcome.html')

def index(request):
    # #date = dt.date.today()
    # #pics=Image.todays_pics
    # # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    # day = convert_dates(date)
    location = Location.objects.all()
    images = Image.objects.all()
    
    return render(request,'welcome.html',{"images":images, "location": location})
# def convert_dates(dates):

#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)

#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

#     # Returning the actual day of the week
#     day = days[day_number]
#     return day

# def past_days_picha(request,past_date):
#     try:
#         # Converts data from the string Url
#         date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

#     except ValueError:
#         # Raise 404 error when ValueError is thrown
#         raise Http404()
#         assert False

#     if date == dt.date.today():
#         return redirect(picha_of_day)

#     pics = Image.days_pics(date)
#     return render(request, 'all-pics/past-pics.html', {"date": date,"pics":pics})

def search_by_category(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        print(search_term)
        found_images = Image.search_by_category(search_term)
        print(found_images)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"images": found_images})

    else:
        message = "You haven't searched for any category"
        return render(request, 'all-pics/search.html',{"message":message})