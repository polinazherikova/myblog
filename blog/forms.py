from django import forms
from .models import Post,Subscriber,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=('published_date','user')

form=PostForm()
print(form)

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','text')