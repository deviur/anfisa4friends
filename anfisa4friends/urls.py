from django.urls import include, path


urlpatterns = [
    path('', include('homepage.urls')),
    # подключить urls.py из директории icecream? Легче лёгкого!
    # не забудьте поставить закрывающий / в конце адреса
    path('icecream/', include('icecream.urls'))
]
