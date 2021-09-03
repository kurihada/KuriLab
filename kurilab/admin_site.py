from django.contrib.admin import AdminSite


class KurilabAdminSite(AdminSite):
    site_header = 'Kurilab 管理员'
    site_title = 'Kurilab 站点管理'

    def __init__(self, name='admin'):
        super().__init__(name)

    def has_permission(self, request):
        return request.user.is_superuser


admin_site = KurilabAdminSite(name='admin')
