from django.urls import path
from web.views import index, about, details, reporter, reporterregis, articelregis

urlpatterns = [
    path('', index, name = 'home'),
    path('details/<int:id>', details, name = 'details'),
    path('about/<slug:slug>', about, name = 'about'),
    path('reporter/',reporter, name = 'reporter'),
    path('regisreporter',reporterregis,name = 'regis-reporter'),
    path('regisart',articelregis,name = 'regis-art' )
] 