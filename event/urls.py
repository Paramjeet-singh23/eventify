from event.views import EventView, EventSearchView
from django.urls import path

urlpatterns = [
    path('', EventView.as_view(), name='get-event'),
    path('create/', EventView.as_view(), name='create-event'),
    path('<int:pk>/', EventView.as_view(), name='event-patch'),
    path('<int:pk>/', EventView.as_view(), name='get-event-by-id'),
    path('search/', EventSearchView.as_view(), name='event-search'),

]
