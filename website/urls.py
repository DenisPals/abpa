from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    
    # About pages
    path('about/', views.about_overview, name='about_overview'),
    path('about/history/', views.about_history, name='about_history'),
    path('about/committee/', views.about_committee, name='about_committee'),
    path('about/constitution/', views.about_constitution, name='about_constitution'),
    
    # News pages
    path('news/', views.news_list, name='news_list'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    
    # Events pages
    path('events/', views.events_list, name='events_list'),
    path('events/<int:event_id>/', views.events_detail, name='events_detail'),
    
    # Membership pages
    path('membership/apply/', views.membership_apply, name='membership_apply'),
    path('membership/benefits/', views.membership_benefits, name='membership_benefits'),
    
    # Contact page
    path('contact/', views.contact, name='contact'),
]