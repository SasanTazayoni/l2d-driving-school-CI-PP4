from django.contrib import admin
from .models import Review, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('author', 'rating', 'approved', 'created_on')
    search_fields = ['content']
    list_filter = ('approved', 'created_on',)
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)