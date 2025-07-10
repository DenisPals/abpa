from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .models import News, Event, CommitteeMember, MembershipApplication, ContactMessage
from .forms import MembershipApplicationForm, ContactForm

def index(request):
    """Homepage view"""
    featured_news = News.objects.filter(is_featured=True)[:3]
    upcoming_events = Event.objects.filter(is_featured=True)[:3]
    committee_members = CommitteeMember.objects.all()[:4]
    
    context = {
        'featured_news': featured_news,
        'upcoming_events': upcoming_events,
        'committee_members': committee_members,
    }
    return render(request, 'website/homepage.html', context)

def about_overview(request):
    """About us overview page"""
    return render(request, 'website/about/overview.html')

def about_history(request):
    """About us history page"""
    return render(request, 'website/about/history.html')

def about_committee(request):
    """Committee members page"""
    committee_members = CommitteeMember.objects.all()
    context = {
        'committee_members': committee_members,
    }
    return render(request, 'website/about/committee.html', context)

def about_constitution(request):
    """Constitution page"""
    return render(request, 'website/about/constitution.html')

def news_list(request):
    """News listing page"""
    news_list = News.objects.all()
    paginator = Paginator(news_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'website/news/list.html', context)

def news_detail(request, news_id):
    """Individual news article page"""
    try:
        news = News.objects.get(id=news_id)
        related_news = News.objects.exclude(id=news_id)[:3]
    except News.DoesNotExist:
        messages.error(request, 'News article not found.')
        return redirect('news_list')
    
    context = {
        'news': news,
        'related_news': related_news,
    }
    return render(request, 'website/news/detail.html', context)

def events_list(request):
    """Events listing page"""
    events_list = Event.objects.all()
    paginator = Paginator(events_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'website/events/list.html', context)

def events_detail(request, event_id):
    """Individual event page"""
    try:
        event = Event.objects.get(id=event_id)
        related_events = Event.objects.exclude(id=event_id)[:3]
    except Event.DoesNotExist:
        messages.error(request, 'Event not found.')
        return redirect('events_list')
    
    context = {
        'event': event,
        'related_events': related_events,
    }
    return render(request, 'website/events/detail.html', context)

def membership_apply(request):
    """Membership application page"""
    if request.method == 'POST':
        form = MembershipApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your membership application has been submitted successfully! We will contact you soon.')
            return redirect('membership_apply')
    else:
        form = MembershipApplicationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'website/membership/apply.html', context)

def membership_benefits(request):
    """Membership benefits page"""
    return render(request, 'website/membership/benefits.html')

def contact(request):
    """Contact page"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'website/contact.html', context)