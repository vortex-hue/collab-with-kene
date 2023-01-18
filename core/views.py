from django.shortcuts import render
from .models import Affiliate, About
from django.views.generic import ListView, TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(ListView):
    template_name = 'others/about.html'
    model = About
    context_object_name = 'abouts'

class AffiliatePageView(ListView):
    template_name = 'others/aff.html'
    model = Affiliate
    context_object_name = 'affiliates'


class FaqPageView(TemplateView):
    template_name = 'others/faq.html'

class PlansPageView(TemplateView):
    template_name = 'others/plans.html'

class TermsPageView(TemplateView):
    template_name = 'others/terms.html'

class ContactPageView(TemplateView):
    template_name = 'others/contact.html'