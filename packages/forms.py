from django import forms
from .widgets import CustomClearableFileInput
from django.forms import ModelForm
from .models import Product, Category, Calendar, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class DateInput(forms.DateInput):
    input_type = 'date'


class CalendarForm(ModelForm):

    class Meta:
        model = Calendar
        fields = ['date']
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'datetime-local'})
        }

    def __init__(self, *args, **kwargs):
        super(CalendarForm, self).__init__(*args, **kwargs)
        self.fields['date'].label = ""


RATING= [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ]

class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=RATING, widget=forms.Select(attrs={'class': 'dropbtn'}))
    class Meta:
        model = Review
        fields = ('name', 'rating', 'body',)
