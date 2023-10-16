from event.views import EventView
from django.urls import path

urlpatterns = [
    path('', EventView.as_view(), name='create_event'),
    path('create/', EventView.as_view(), name='create_event'),

]
