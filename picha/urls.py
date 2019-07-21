from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'home'),
    url(r'^search/',views.search_by_category, name='search_by_category'),
    url(r'^location/(?P<location>\d+)', views.search_by_location, name='location_filter'),

    # url(r'^$',views.picha_of_day,name='pichaToday'),
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_picha,name = 'pastPicha'),
    # url(r'^search/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)