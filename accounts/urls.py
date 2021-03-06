from django.urls import path

from . import views
# Create your views here.




app_name = 'accounts'


urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='account_login'),
    path('signup/', views.MySignupView, name='account_signup'),
    path('signup/mentee/', views.signup_mentee, name='mentee_signup'),
    path('signup/mentor/', views.signup_mentor, name='mentor_signup'),
    path('logout/', views.Logout, name="account_logout"),
    path('password_reset/', views.MyPasswordResetView.as_view(), name='account_reset_password'),
    path('profile/<str:username>/', views.profile_detail_mentor_univ, name='profile_detail_mentor_univ'),
    path('confirm/', views.confirm_email, name='confirm_email'),
    path('confirm/sent/', views.email_confirm_sent, name='email_confirm_sent'),

    path('mentorpage/<str:username>', views.mentorpage, name="mentorpage"),
]