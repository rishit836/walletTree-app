from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
<<<<<<< HEAD
    path('',views.home,name="home")
=======
    path('',views.home,name="home"),
    path('login',views.login_view, name="login"),
    path('signup',views.signup_view,name="signup"),
    path('logout',views.logout_view,name="logout")
>>>>>>> 290a52e (decluttered signup and login page and now backend works)
]
