"""Forms for API management."""
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from openedx.core.djangoapps.api_admin.models import ApiAccessRequest, Catalog
from openedx.core.djangoapps.api_admin.widgets import TermsOfServiceCheckboxInput


class ApiAccessRequestForm(forms.ModelForm):
    """Form to request API access."""
    terms_of_service = forms.BooleanField(widget=TermsOfServiceCheckboxInput(), label='')

    class Meta(object):
        model = ApiAccessRequest
        fields = ('company_name', 'website', 'company_address', 'reason', 'terms_of_service')
        labels = {
            'company_name': _('Company Name'),
            'company_address': _('Company Address'),
            'reason': _('Describe what your application does.'),
        }
        help_texts = {
            'reason': None,
            'website': _("The URL of your company's website."),
            'company_name': _('The name of your company.'),
            'company_address': _('The contact address of your company.'),
        }
        widgets = {
            'company_address': forms.Textarea()
        }

    def __init__(self, *args, **kwargs):
        # Get rid of the colons at the end of the field labels.
        kwargs.setdefault('label_suffix', '')
        super(ApiAccessRequestForm, self).__init__(*args, **kwargs)


class CatalogForm(forms.ModelForm):
    """Form to create a catalog."""

    # viewers = forms.Textarea()

    class Meta(object):
        model = Catalog
        fields = ('name', 'query',)
        # help_texts = {
        #     'viewers': _('Comma-separated list of usernames which will be able to view this catalog.'),
        # }

    def clean(self):
        cleaned_data = super(CatalogForm, self).clean()
        # viewers = cleaned_data.get('viewers')
        # usernames = [username.strip() for username in viewers.split(',')]
        # for username in usernames:
        #     try:
        #         User.objects.get(username=username)
        #         self.instance.viewers.add(username)
        #     except User.DoesNotExist:
        #         self.add_error('viewers', _('The specified user does not exist.'))
