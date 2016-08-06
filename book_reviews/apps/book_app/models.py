from __future__ import unicode_literals

from django.db import models

class BooksManager(models.model)
class Books(models.Model):
	title = models.CharField(max_length = 100) 
	author = models.CharField(max_length = 100)
	added_by = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	booksManager = BooksManager()