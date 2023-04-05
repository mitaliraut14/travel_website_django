from django.urls import path
from travelapp import views

urlpatterns = [
    path('',views.index),
    path('signup',views.signup),
    path('signin',views.signin),
    path('book/<rid>',views.book),
    path('udash',views.dashboard),
    path('delete/<rid>',views.delete),
    path('userreg',views.userreg),
    path('userlogin',views.userlogin),
    path('userlogout',views.userlogout),
    path('placedetail/<rid>',views.placedetail),
    path('placedetail/<rid>',views.placedetail),
    path('about',views.about),
]