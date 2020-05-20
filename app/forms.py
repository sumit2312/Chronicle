from django import forms
from .models import MyUser
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Article, Journal, Keyword, Subject, EditorNote


class MyUserCreationForm(UserCreationForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={
        'class': 'px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full'}))

    class Meta:
        model = MyUser
        fields = ('email', 'name', 'user_type',)

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full',
                'required': True}),
            'name': forms.TextInput(attrs={
                'class': 'px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full'}),
            'user_type': forms.Select(attrs={
                'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"', }),
        }


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ('email', 'name', 'user_type',)

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full',
                'required': True}),
            'user_type': forms.Select(attrs={'class': 'select is-primary is-fullwidth', }),
            'password': forms.PasswordInput(attrs={'class': 'input is-success'}),
        }


class ReviewForm(forms.Form):
    new_comment = forms.CharField(max_length=300,
                                  widget=forms.Textarea(attrs={
                                      'cols': 50, 'rows': 6,
                                      'class': 'border border-green-800 rounded shadow-inner p-4 border-0',
                                  }),
                                  required=False)
    APPROVAL_CHOICES = (
        ('approve', 'Approve this article '),
        ('reject', 'Reject this article and send it back to the author with your comment'),
    )
    approval = forms.ChoiceField(choices=APPROVAL_CHOICES, widget=forms.RadioSelect(attrs={
        'class': 'text-red',
    }))


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "abstract", "text", "keywords"]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full shadow-inner p-4 border-2'}),
            'abstract': forms.Textarea(attrs={
                'class': 'w-full shadow-inner p-4 border-2'}),
            'keywords': forms.CheckboxSelectMultiple,
        }


class ArticleFormFinal(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["volume", "issue", "issue_title", "title", "abstract", "text", "state",]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full shadow-inner p-4 border-2'}),
            'abstract': forms.Textarea(attrs={
                'class': 'w-full shadow-inner p-4 border-2'}),
            'issue_title': forms.TextInput(attrs={
                'class': 'w-full shadow-inner p-4 border-2'}),
            'volume': forms.NumberInput(attrs={
                'class': 'w-full shadow-inner md:w-1/3 rounded py-4 px-3 mb-6 md:mb-0 border-2'}),
            'issue': forms.NumberInput(attrs={
                'class': 'w-full shadow-inner md:w-1/3 rounded py-4 px-3 mb-6 md:mb-0 border-2'}),
            'state': forms.Select(attrs={
                'class': 'w-full md:w-1/3 rounded py-4 px-3 mb-6 md:mb-0'
            })
        }
