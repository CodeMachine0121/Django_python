from django import forms
from.models import Vendor, Food

from django.utils.translation import ugettext as _
class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'

        # Label 對應
        labels = {
            'vendor_name':_('店販名稱'),
            'store_name':_('店名'),
            'phone_number':_('電話'),
            'address':_('地址'),
        }
