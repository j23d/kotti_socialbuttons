# -*- coding: utf-8 -*-

"""
Created on 2016-05-26
:author: j23d (j23d@jusid.de)
"""

from __future__ import absolute_import

from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource


library = Library("kotti_socialbuttons", "static")

social_privacy_css = Resource(
    library,
    "socialshareprivacy/socialshareprivacy.css",
    minified='socialshareprivacy/socialshareprivacy.min.css',
    bottom=True
)
social_privacy_js = Resource(
    library,
    "socialshareprivacy/jquery.socialshareprivacy.js",
    minified='socialshareprivacy/jquery.socialshareprivacy.min.js',
    depends=[social_privacy_css],
    bottom=True
)
social_privacy_en_js = Resource(
    library,
    "socialshareprivacy/jquery.socialshareprivacy.en.js",
    minified='socialshareprivacy/jquery.socialshareprivacy.en.min.js',
    depends=[social_privacy_js],
    bottom=True
)
social_privacy_de_js = Resource(
    library,
    "socialshareprivacy/jquery.socialshareprivacy.de.js",
    minified='socialshareprivacy/jquery.socialshareprivacy.de.min.js',
    depends=[social_privacy_js],
    bottom=True
)

view_css_and_js = Group([social_privacy_css,
                         social_privacy_js])
