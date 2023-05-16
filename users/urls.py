from django.urls import path,include
from .views import *

urlpatterns = []

from users.views import *

urlpatterns += [

    path('get-all-students',GetStudentsView.as_view()),
    path('get-and-save-orders',GetOrdersViews.as_view())

]
