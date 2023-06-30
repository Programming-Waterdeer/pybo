from django import forms
from ReRAM.models import Question, Answer

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content', 'upload_files']  # questionform 에서 사용할 question 모델의 속성
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.CharField(widget=CKEditorUploadingWidget()),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용'
        }

