=====================================
``django-uni-form`` Contrib Templates
=====================================

What
----

This is my fork with additional features:

* `twitter_bootstrap` is a django app now, makes it uneccessary to copy templates
  manually

* added custom renderer that adds `inputs-list` class to radio fields

Contributed templates for `Daniel Greenfeld <https://github.com/pydanny>`_ and `Miguel Araujo <https://github.com/maraujop>`_'s 
awesome `django-uni-form <https://github.com/pydanny/django-uni-form>`_ library. Template sets are named for the library they 
relate to.

How
---

Install::

    pip install -e git://github.com/bmihelac/django-uni-form-contrib.git#egg=uni_form_contrib

Add ``uni_form_contrib.twitter_bootstrap`` application to ``INSTALLED_APPS`` in
settings.py **before** ``uni_form`` so django will pick this templates instead
of default ``uni_form`` templates.

Widgets
-------

For list of options, Bootstrap expect list tag to have a `inputs-list` class.
``BootstrapRadioFieldRenderer`` makes it easy to add css class:::

    from uni_form_contrib.twitter_bootstrap.widgets import BootstrapRadioFieldRenderer

    field = forms.ChoiceField(label=_('field'),
            choices=FIELD_CHOICES,
            widget=forms.widgets.RadioSelect(renderer=BootstrapRadioFieldRenderer)
            )

Who
---

Current contributors are:

    * `Kenneth Love <https://github.com/kennethlove>`_

    * `Bojan Mihelac <https://github.com/bmihelac>`_

License
-------

All templates are released under the MIT license.
