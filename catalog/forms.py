import os

from django import forms
from .models import Product

FORBIDDEN_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар',
    ]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category' , 'price', 'image',]


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            name_lower = name.lower()
            for word in FORBIDDEN_WORDS:
                if word in name_lower:
                    raise forms.ValidationError(f'Название содержит запрещённое слово: "{word}"')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description:
            desc_lower = description.lower()
            for word in FORBIDDEN_WORDS:
                if word in desc_lower:
                    raise forms.ValidationError(f'Описание содержит запрещённое слово: "{word}"')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None:
            raise forms.ValidationError("Укажите цену товара.")
        if price <= 0:
            raise forms.ValidationError("Цена не может равняться 0 или быть отрицательным.")
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            return image
        ext = os.path.splitext(image.name)[1].lower()
        allowed_exts = ('.jpg', '.jpeg', '.png')
        if ext not in allowed_exts:
            raise forms.ValidationError("Допустимые форматы изображения: JPEG и PNG.")
        max_size = 5 * 1024 * 1024  # 5MB
        if image.size > max_size:
            raise forms.ValidationError("Размер файла не должен превышать 5 МБ.")
        return image

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите имя'
        })
        self.fields['category'].empty_label = 'Выберите категорию'
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Категория товара'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Напишите про товар как можно интереснее!'
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Стоимость товара'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
        })
