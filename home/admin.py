from django.contrib import admin
from .models import Contact, Newsletter
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email',)