from django.forms import ModelForm, Textarea
from hotelsite.models import Review, Hotel


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'hotel', 'rating', 'description']
        widgets = {
            'description': Textarea(attrs={'cols': 5, 'rows': 4}),
        }
