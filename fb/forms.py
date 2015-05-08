
from django.forms import (
    Form, CharField, Textarea, PasswordInput, ChoiceField, DateField,
    ImageField,
)

from fb.models import UserProfile


class UserPostForm(Form):
    text = CharField(widget=Textarea(
        attrs={'rows': 1, 'cols': 40, 'class': 'form-control','placeholder': "Put your thoughts here..."}))

class UserPostCommentForm(Form):
    text = CharField(widget=Textarea(
        attrs={'rows': 1, 'cols': 50, 'class': 'form-control','placeholder': "Write a comment..."}))


class UserLogin(Form):
    username = CharField(label='',max_length=30,widget=Textarea(attrs={'rows': 1, 'cols': 25,'placeholder': 'Username'}))
    password = CharField(widget=PasswordInput)


class UserProfileForm(Form):
    first_name = CharField(max_length=100, required=False)
    last_name = CharField(max_length=100, required=False)
    gender = ChoiceField(choices=UserProfile.GENDERS, required=False)
    date_of_birth = DateField(required=False)
    avatar = ImageField(required=False)


class AlbumForm(Form):
    album_name = CharField(max_length=100, required=False)
    album_date = DateField(required=False)


class PhotoForm(Form):
    photo = ImageField(required=False)
