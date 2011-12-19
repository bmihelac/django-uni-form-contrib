from django.forms.widgets import RadioFieldRenderer
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe


class BootstrapRadioFieldRenderer(RadioFieldRenderer):
    """
    Adds `inputs-list` class to ``ul`` html tag for ReadioFields.
    """

    def render(self):
        """Outputs a <ul> for this set of radio fields."""
        return mark_safe(u'<ul class="inputs-list">\n%s\n</ul>' % u'\n'.join([u'<li>%s</li>'
                % force_unicode(w) for w in self]))


