from django.urls import path, include
from . views import *
from calendar_api.api.views import *

urlpatterns = [
    path('events/', eventListView.as_view()),
    path('events/<int:id>/', eventDetailView.as_view()),

]