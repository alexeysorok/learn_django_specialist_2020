from django import forms
from .models import Product


class ProductForm(forms.Form):

    title = forms.CharField(label='Наименование', max_length=255)
    article = forms.CharField(label='Артикул', max_length=16)
    quantity = forms.IntegerField(label='Количество', min_value=0)
    description = forms.CharField(label='Описание', widget=forms.Textarea, required=False)


# форма по модели
class ProductModelForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'article', 'quantity', 'description']


class TagListForm(forms.Form):
    tag_list = forms.CharField(label='новые', required=False)




