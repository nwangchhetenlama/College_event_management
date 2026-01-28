from django.contrib import admin
from django.urls import path,include

from events import views
urlpatterns = [
    # path('',views.base,name="base"),
    path('',views.event_list,name="event_list"),
    path('event/<int:id>/',views.event_detail,name="event_detail"),
    path('create/',views.create_event,name="create_event"),

]
