# -*- coding: utf-8 -*-

"""
Created on 2016-05-26
:author: j23d (j23d@jusid.de)
"""

from pyramid.events import subscriber
from pyramid.events import BeforeRender

from pyramid.view import view_config
from pyramid.threadlocal import get_current_registry

from kotti_settings.util import get_setting


@subscriber(BeforeRender)
def include_social_media_buttons_lang(event):
    settings = get_current_registry().settings
    default_locale_name = settings['pyramid.default_locale_name']
    if 'de' in default_locale_name:
        from kotti_socialbuttons.fanstatic import social_privacy_de_js
        social_privacy_de_js.need()
    else:
        from kotti_socialbuttons.fanstatic import social_privacy_en_js
        social_privacy_en_js.need()


@view_config(name='social_media_buttons',
             permission='view',
             renderer='json')
def social_media_buttons(context, request):
    social_media_buttons = get_setting('social_media_buttons', [])
    if social_media_buttons:
        social_media_buttons = [str(button) for button in social_media_buttons]
    return {'social_media_buttons': social_media_buttons}
