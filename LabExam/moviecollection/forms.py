from django import forms
from .models import Movie, Review


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'release_year', 'description']


class ReviewForm(forms.ModelForm):
    # Override the field to set min and max values.
    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'min': 1, 'max': 5})
    )

    class Meta:
        model = Review
        fields = ['review_text', 'rating']
