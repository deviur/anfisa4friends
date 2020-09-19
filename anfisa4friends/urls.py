from django.urls import include, path

urlpatterns = [
    # Тут должен быть path(), который при обращении к главной странице
    # переадресует запрос в файл urls.py из директории homepage
    path('', include('homepage.urls'))
]
