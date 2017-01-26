from django.forms import ModelForm, Textarea
from hotelsite.models import Review, Hotel


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'description']
        widgets = {
            'description': Textarea(attrs={'cols': 40, 'rows': 15}),
        }
