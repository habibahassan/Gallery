from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
path('', views.homePage, name='home'),
path('search/',views.searchbycategory, name='searchbycategory'),
path('location/<int:location>', views.searchbylocation, name='location_filter'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)