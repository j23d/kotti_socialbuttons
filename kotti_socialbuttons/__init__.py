# -*- coding: utf-8 -*-

"""
Created on 2016-05-26
:author: j23d (j23d@jusid.de)
"""

from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_socialbuttons')


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                kotti_socialbuttons.kotti_configure

        to enable the ``kotti_socialbuttons`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' kotti_socialbuttons'
    settings['kotti.populators'] += ' kotti_socialbuttons.populate.populate_settings'
    settings['kotti.fanstatic.view_needed'] += ' kotti_socialbuttons.fanstatic.view_css_and_js'


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``kotti_configure`` above to your ``kotti.configurators`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """

    config.add_translation_dirs('kotti_socialbuttons:locale')
    config.add_static_view('static-kotti_socialbuttons',
                           'kotti_socialbuttons:static')

    config.scan(__name__)
