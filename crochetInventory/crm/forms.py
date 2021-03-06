from django import forms
from .models import CrochetHook, Yarn, Gift


class CrochetHookForm(forms.ModelForm):
    class Meta:
        model = CrochetHook
        fields = ('crochetHook_size', 'material', 'count')


class YarnForm(forms.ModelForm):
    class Meta:
        model = Yarn
        fields = ('crochetHook_size', 'yarn_color', 'yarn_texture', 'yarn_amount')

class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ('crochetHook_size', 'yarn_color', 'recipient_name', 'p_description', 'gift_size',
'p_description')