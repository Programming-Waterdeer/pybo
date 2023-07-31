import os
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from uuid import uuid4
from datetime import datetime

from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

def get_file_path(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    uuid_name = uuid4().hex
    return '/'.join(['upload_file/', ymd_path, uuid_name])

class Category(MPTTModel):
    name = models.CharField(max_length=64, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = (('parent', 'slug', ))
        verbose_name_plural = 'categories'

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except:
            ancestors = list()
        else:
            ancestors = [i.slug for i in ancestors]
        slugs = list()
        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i+1]))
        return slugs

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('MBE:index', args=[self.name])

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='MBE_author_question')
    subject = models.CharField(max_length=200)
    content = RichTextUploadingField()
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='MBE_voter_question')  # 추천인 추가
    upload_files = models.FileField(upload_to=get_file_path, null=True, blank=True, verbose_name='MBE_File Upload')
    filename = models.CharField(max_length=64, null=True, verbose_name='MBE_File_Name')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='MBE_category_question')

    def __str__(self):
        return self.subject
    def get_absolute_url(self):
        return reverse('MBE:question_detail', args=[self.id])


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='MBE_author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='MBE_voter_answer')  # 추천인 추가
