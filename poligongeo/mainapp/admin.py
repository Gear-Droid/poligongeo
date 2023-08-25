from django.contrib import admin
from .models import CallRequest


class CallRequestAdmin(admin.ModelAdmin):

    date_hierarchy = 'created'

    class Meta:
        model = CallRequest

    fields = (
        'created',
        ('first_name', 'phone', 'email', ),
    )
    list_display = (
        'first_name', 'phone', 'email',
    )
    readonly_fields = (
        'created',
    )
    list_filter = (
        'created',
    )
    search_fields = (
        'first_name', 'phone', 'email',
    )


admin.site.register(CallRequest, CallRequestAdmin)
