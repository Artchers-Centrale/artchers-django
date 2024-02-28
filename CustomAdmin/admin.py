from django.contrib import admin
from artchers.models import district, vote
from .views import custom_app_view
from django.urls import path


class CustomAppAdmin(admin.AdminSite):
    index_template = 'admin/custom_index.html'
    site_title = site_header = index_title = 'Administration de Artchers'
 
    def get_urls(
        self,
    ):
        return [
            path(
                "custom-app/",
                self.admin_view(custom_app_view),
                name="custom_app_index",
            ),
        ] + super().get_urls()
 
 
admin_site = CustomAppAdmin()

admin.site.register(district)
admin.site.register(vote)
