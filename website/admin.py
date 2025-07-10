from django.contrib import admin
from .models import News, Event, CommitteeMember, MembershipApplication, ContactMessage

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'is_featured')
    list_filter = ('is_featured', 'date_published')
    search_fields = ('title', 'content')
    date_hierarchy = 'date_published'

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'is_featured')
    list_filter = ('is_featured', 'date')
    search_fields = ('title', 'description', 'location')
    date_hierarchy = 'date'

@admin.register(CommitteeMember)
class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'order', 'email')
    list_filter = ('position',)
    search_fields = ('name', 'position', 'bio')
    ordering = ('order',)

@admin.register(MembershipApplication)
class MembershipApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'status', 'date_applied')
    list_filter = ('status', 'date_applied')
    search_fields = ('first_name', 'last_name', 'email')
    readonly_fields = ('date_applied',)
    date_hierarchy = 'date_applied'

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_sent', 'is_read')
    list_filter = ('is_read', 'date_sent')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('date_sent',)
    date_hierarchy = 'date_sent'
