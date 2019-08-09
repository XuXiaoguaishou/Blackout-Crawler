from django.contrib import admin
from .models import SearchRecord

# Register your models here.


class SearchRecordAdmin(admin.ModelAdmin):
    list_display = ('content_string',)
    #list_filter = ('created_time',)
    fieldsets = [
        (None, {'fields': ('content_string',)}),
    ]


admin.site.register(SearchRecord, SearchRecordAdmin)