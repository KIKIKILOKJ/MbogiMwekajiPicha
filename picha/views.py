from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import Image

# Create your views here.
# def welcome(request):
#     return render(request,'welcome.html')

def picha_of_day(request):
    date = dt.date.today()
    #pics=Image.todays_pics
    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)

    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return render(request, 'all-pics/today-pics.html', {"date": date})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_picha(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(picha_of_day)

    pics = Image.days_pics(date)
    return render(request, 'all-pics/past-pics.html', {"date": date,"pics":pics})

def search_results(request):
    
    if 'pics' in request.GET and request.GET["pics"]:
        search_term = request.GET.get("pics")
        searched_pics = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"pics": searched_pics})

    else:
        message = "You haven't searched for any category"
        return render(request, 'all-pics/search.html',{"message":message})