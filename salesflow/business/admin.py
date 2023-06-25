from django.contrib import admin

from salesflow.business.models import Business


# Register your models here.
@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "country",
        "owner",
        "manager",
        "assistant_manager",
        "date_created",
    )
    search_fields = (
        "name",
        "location",
        "country",
        "owner",
        "manager",
        "assistant_manager",
    )
    list_filter = ("country",)
    exclude = (
        "date_modified",
        "user_updated",
        "user_deleted",
    )
