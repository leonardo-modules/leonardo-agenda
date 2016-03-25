
def event(self):
    from leonardo.module.web.widget.application.reverse import app_reverse
    return app_reverse(
        'event_detail',
        'leonardo_agenda.apps.events',
        kwargs={
            'slug': self.slug,
        })
