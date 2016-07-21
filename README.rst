kotti_socialbuttons
*******************

This add on add `socialshareprivacy`_ to Kotti that allows you to add social media buttons to your site.
Add `<div class="socialshareprivacy" />` to the template of your content type, where the buttons should appear. In the settings section you can choose the buttons to include, namely Twitter, Facebook and Google+.

|pypi|_
|downloads_month|_
|license|_
|build_status_stable|_

.. |pypi| image:: https://img.shields.io/pypi/v/kotti_socialbuttons.svg?style=flat-square
.. _pypi: https://pypi.python.org/pypi/kotti_socialbuttons/

.. |downloads_month| image:: https://img.shields.io/pypi/dm/kotti_socialbuttons.svg?style=flat-square
.. _downloads_month: https://pypi.python.org/pypi/kotti_socialbuttons/

.. |license| image:: https://img.shields.io/pypi/l/kotti_socialbuttons.svg?style=flat-square
.. _license: http://www.repoze.org/LICENSE.txt

.. |build_status_master| image:: https://img.shields.io/travis/j23d/kotti_socialbuttons/master.svg?style=flat-square
.. _build_status_master: http://travis-ci.org/j23d/kotti_socialbuttons

`Find out more about Kotti`_

Development happens at https://github.com/j23d/kotti_socialbuttons

.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti

Setup
=====

To enable the extension in your Kotti site, activate the configurator::

    kotti.configurators =
        kotti_settings.kotti_configure
        kotti_socialbuttons.kotti_configure


Development
===========

Contributions to kotti_socialbuttons are highly welcome.
Just clone its `Github repository`_ and submit your contributions as pull requests.

.. _tracker: https://github.com/j23d/kotti_socialbuttons/issues
.. _Github repository: https://github.com/j23d/kotti_socialbuttons
.. _socialshareprivacy : https://github.com/patrickheck/socialshareprivacy
