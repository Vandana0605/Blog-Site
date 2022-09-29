from django.urls import path,include
urlpatterns = [
   path('acount/',include('acount.urls')),
   path('home/',include('home.urls'))
]
