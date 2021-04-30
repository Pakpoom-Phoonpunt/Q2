
# Create your models here.
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200) #เก็บคำถาม
    pub_date = models.DateTimeField('date published') #เก็บวันที่ทำการสร้างคำถาม

    def __str__(self):
        return self.question_text #แสดงคำถาม

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE) #บอกว่าเป็นตัวเลือกของคำถามข้อไหน
    choice_text = models.CharField(max_length=200) #เก็บชื่อตัวเลือก

    def __str__(self):
        return self.choice_text #แสดงชื่อตัวเลือก