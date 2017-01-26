from django.forms import ModelForm, Textarea
from hotelsite.models import Review, Hotel


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'description']
        widgets = {
            'description': Textarea(attrs={'cols': 10, 'rows': 4}),
        }
