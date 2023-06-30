# Create your views here.
import urllib
import os
from django.utils import timezone
from django.http import HttpResponse, Http404
import mimetypes
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render


from ReRAM.forms import QuestionForm
from ReRAM.models import Question, Category

@login_required(login_url='common:login')
def question_create(request, category_name):

    category = Category.objects.get(name=category_name)
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.category = category
            question.create_date = timezone.now()
            if request.FILES:
                if 'upload_files' in request.FILES.keys():
                    question.filename = request.FILES['upload_files'].name
            question.save()
            return redirect(category)
    else:  # request.method == 'GET'
        form = QuestionForm()
    context = {'form': form, 'category': category}
    return render(request, 'ReRAM/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, 'no permission')
        return redirect('ReRAM:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            if request.FILES:
                if 'upload_files' in request.FILES.keys():
                    question.filename = request.FILES['upload_files'].name
            question.save()
            return redirect('ReRAM:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form, 'category': question.category}
    return render(request, 'ReRAM/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, 'no permission')
        return redirect('ReRAM:detail', question_id=question.id)
    question.delete()
    return redirect('ReRAM:index')
@login_required(login_url='common:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, 'you cannot recommend the post which you uploaded')
    else:
        question.voter.add(request.user)
    return redirect('ReRAM:detail', question_id=question.id)



def question_download_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    url = question.upload_files.url[1:]
    file_url = urllib.parse.unquote(url)

    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            quote_file_url = urllib.parse.quote(question.filename.encode('utf-8'))
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
        raise Http404
