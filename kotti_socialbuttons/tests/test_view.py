# -*- coding: utf-8 -*-

"""
Created on 2016-05-26
:author: j23d (j23d@jusid.de)
"""


def test_social_media_buttons(root, dummy_request):

    from kotti_socialbuttons.views.view import social_media_buttons
    content = social_media_buttons(root, dummy_request)
    assert content == {'social_media_buttons': []}
