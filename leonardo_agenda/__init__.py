
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_agenda.Config'

LEONARDO_OPTGROUP = 'Events'

LEONARDO_APPS = [
    'leonardo_agenda',
    'elephantagenda',
    'elephantagenda.backends.agenda'
]
LEONARDO_WIDGETS = [
    'leonardo_agenda.models.EventsWidget'
]

LEONARDO_PLUGINS = [
    ('leonardo_agenda.apps.events', _('Events'), ),
]

LEONARDO_ABSOLUTE_URL_OVERRIDES = {
    'agenda.event': 'leonardo_agenda.overrides.event'
}


class Config(AppConfig):
    name = 'leonardo_agenda'
    verbose_name = "leonardo-agenda"

    def ready(self):

        from ckeditor_uploader.widgets import CKEditorUploadingWidget
        from elephantagenda.backends.agenda import models
        models.EventAdminForm._meta.widgets.update({
            'description': CKEditorUploadingWidget(),
            'short_description': CKEditorUploadingWidget()
        })

        try:
            from ckeditor_uploader.widgets import CKEditorUploadingWidget
            from elephantagenda.backends.agenda import models
            models.EventAdminForm._meta.widgets[
                'description'] = CKEditorUploadingWidget()

        except Exception as e:
            raise e
