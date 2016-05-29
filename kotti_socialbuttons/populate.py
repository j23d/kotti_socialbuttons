import colander

from deform.widget import Select2Widget

from kotti_settings.util import add_settings
from kotti_socialbuttons import _


social_media_buttons = ((u'facebook', _(u'Facebook')),
                        (u'twitter', _(u'Twitter')),
                        (u'google', _(u'Goolge+')),
                        )


class SocialMediaButtons(colander.SchemaNode):
    name = u'social_media_buttons'
    title = _(u'Social media buttons')
    description = _(u'Enable only specific social media buttons.')
    widget = Select2Widget(values=social_media_buttons, multiple=True)
    default = [u'facebook', u'twitter', u'google']
    missing = [u'facebook', u'twitter', u'google']


class KottiSocialbuttonsSettingsSchema(colander.MappingSchema):
    social_media_buttons = SocialMediaButtons(colander.Set())


KottiSocialbuttonsSettings = {
    'name': 'kotti_socialbuttons_settings',
    'title': _(u'Kotti social buttons settings'),
    'description': _(u"Settings for kotti_socialbuttons"),
    'success_message': _(u"Successfully saved social buttons settings."),
    'schema_factory': KottiSocialbuttonsSettingsSchema,
}


def populate_settings():
    add_settings(KottiSocialbuttonsSettings)
