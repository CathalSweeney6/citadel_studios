from django import forms
from .widgets import CustomClearableFileInput
from django.forms import ModelForm
from .models import Product, Category, Calendar, Review, Time


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
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
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


TIME= [
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
    ('20:00', '20:00'),
    ('20:00', '20:00'),
    ('21:00', '21:00'),
    ]

class TimeForm(ModelForm):

    class Meta:
        model = Time
        fields = ['time']
        widgets = {
            'time': forms.widgets.DateInput(attrs={'type': 'time'})
        }

    def __init__(self, *args, **kwargs):
        super(CalendarForm, self).__init__(*args, **kwargs)
        self.fields['time'].label = ""