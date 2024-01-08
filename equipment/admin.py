from django.contrib import admin
from .models import Equipment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Equipment)
class EquipmentAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
