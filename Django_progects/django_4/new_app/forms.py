from django import forms

from .models import Blog


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

    def clean_email(self, *arsg, **kwargs):
        email = self.cleaned_data.get('email')
        if email.endswith('.edu'):
            raise forms.ValidationError("This is not valid email. Please don't use edu")
        return email


class BlogForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogModelForm(forms.ModelForm):  # !!!!!!! only ModelForm
    class Meta:
        model = Blog
        fields = ['title', 'image', 'slug', 'content', 'publish_date']

    def clean_title(self, *arsg, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = Blog.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This title has already been used")
        return title
