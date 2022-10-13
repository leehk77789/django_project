from unittest.util import _MAX_LENGTH
from django.db import models
from users.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #on_delete=models.CASCADE
    #계정값이 삭제가 되었을때 내가 작성한 글들 전부 삭제
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #admin에서 확인하는 게시물 제목 변경 방법
    def __str__(self):
        return str(self.content)