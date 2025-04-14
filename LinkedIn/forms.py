from django import forms
from .models import Post
from Authentication.models import Profil

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'text']

class ProfileEditFrom(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['img', 'fullname', 'location', 'bio', 'profilBanner', 'ish']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
            'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
        })