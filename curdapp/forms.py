from django import forms
from .models import Product


class DateInput(forms.DateInput):
    input_type = 'date'
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('prd_name', 'prd_price', 'prd_qnty', 'prd_desc', 'prd_mfg_date')
        widgets = {
            'prd_mfg_date': DateInput(),
        }