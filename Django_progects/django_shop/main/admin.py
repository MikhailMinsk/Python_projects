from django.contrib import admin
import datetime

from .models import AdvUser, SubRubric, SuperRubric
from .utilities import send_activation_notification
from .forms import SubRubricForm


def send_activation_notifications(modeladmin, request, queryset):
    for record in queryset:
        if not record.is_activated:
            send_activation_notification(record)
    modeladmin.message_user(request, 'An email notification is send')


send_activation_notifications.short_description = 'Send email with notification is send'


class Nonactivatedfilter(admin.SimpleListFilter):
    title = 'Activation done'
    parametr_name = 'actstate'

    def lookups(self, request, model_admin):
        return (
            ('activated', 'Dona'),
            ('threedays', 'Not gone more than three days '),
            ('week', 'Not gone more than week ')
        )

    def queryset(self, request, queryset):
        val = self.value()
        if val == 'activated':
            return queryset.filter(is_active=True, is_activated=True)
        elif val == 'threedays':
            d = datetime.date.today() - datetime.timedelta(days=3)
            return queryset.filter(is_active=False, is_activated=False, date_joined__date__lt=d)
        elif val == 'week':
            d = datetime.date.today() - datetime.timedelta(weeks=1)
            return queryset.filter(is_active=False, is_activated=False, date_joined__date__lt=d)


class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = (Nonactivatedfilter,)
    fields = (('username', 'email'), ('first_name', 'last_name'),
              ('send_messages', 'is_activate', 'is_activated'),
              ('is_staff', 'is_superuser'),
              'groups', 'user_permissions',
              ('last_login', 'date_joined'))
    readonly_fields = ('last_login', 'date_joined')
    actions = (send_activation_notification,)


class SubRubricInLine(admin.TabularInline):
    model = SubRubric


class SuperRubricAdmin(admin.ModelAdmin):
    exclude = ('super_rubric',)
    inlines = (SubRubricInLine,)


class SubRubricAdmin(admin.ModelAdmin):
    form = SubRubricForm


admin.site.register(AdvUser)
admin.site.register(SuperRubric, SuperRubricAdmin)
admin.site.register(SubRubric, SubRubricAdmin)

