from django.urls import path, include

from . import views

urlpatterns = [
    
    path('home/', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('faq/', views.FaqPageView.as_view(), name='faq'),
    path('plans/', views.PlansPageView.as_view(), name='plans'),
    path('terms/', views.TermsPageView.as_view(), name='terms'),
    path('affiliate/', views.AffiliatePageView.as_view(), name='affiliate'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
]