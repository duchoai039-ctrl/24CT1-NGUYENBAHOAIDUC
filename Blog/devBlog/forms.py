from django import forms
from django.contrib.auth.models import User
# pyrefly: ignore [missing-import]
from .models import Post, Comment, Tag


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        label='Email',
        error_messages={'required': 'Email không được để trống.'}
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Mật khẩu'
    )
    interests = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Chọn thẻ nội dung bạn quan tâm'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Thẻ bài viết'
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'tags']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Nội dung bình luận'
        }
