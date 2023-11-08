from django.urls import path
from . import views
urlpatterns=[
    path('login', views.login_page, name="login-page"),
    path('logout', views.logout_page, name="logout-page"),
    path('signup', views.signup, name="signup-page"),
    path('home', views.home, name="home-page"),
    path('service', views.service, name="service-page"),
    path('book', views.book, name="book-page"),
    path('about', views.about, name="about-page"),
    path('list',views.list, name="list-page"),
    path('schedule',views.schedule, name="schedule-page"),
    path('delete/<int:id>', views.delete, name="delete-page")
]