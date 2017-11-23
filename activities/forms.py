from django import forms
from activities.models import Lecture, Poster, Author

class LectureForm(forms.ModelForm):

    abstract = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "60", 'rows': "20", }))
    class Meta:
        model = Lecture
        fields = ('title', 'abstract', 'tags', )

class PosterForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = ('title', 'abstract', 'tags', )
