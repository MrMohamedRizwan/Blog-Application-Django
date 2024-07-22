from django.urls import path
from . import views
urlpatterns = [
    path('a/', views.post_list),
    path('msg/',views.getData),
    path('add/',views.addData),
    path('blog/',views.add_Blog),
    path('getblog/',views.get_Blog)

]