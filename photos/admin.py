from django.contrib import admin
from photos.models import Photo
# Register your models here.


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner_name', 'license', 'visibility')
    list_filter = ('license', 'visibility', 'created_on')
    search_fields = ('name', 'description', 'owner_name')

    fieldsets = (
        ("Photo", {
            "classes": ("wide",),
            "fields": ("name", 'owner', 'url', 'description',)
        }),
        ("License & visibility", {
            "classes": ("wide", "collapse"),
            "fields": ('license','visibility')
        })
    )

    def owner_name(self, obj):
        return obj.owner.first_name + ' ' + obj.owner.last_name

    owner_name.short_description = "Author"
    owner_name.admin_order_field = "owner__first_name"

admin.site.register(Photo, PhotoAdmin)