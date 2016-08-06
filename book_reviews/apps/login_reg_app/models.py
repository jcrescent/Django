from __future__ import unicode_literals
from django.db import models
import re, bcrypt

class UsersManager():
	def validation(self, post_data):
		EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
		invalids = [] 
		if not post_data['first']:
			invalids.append("First name cannot be blank")
		elif len(post_data['first']) < 2:
			invalids.append("First name too short")
		if not post_data['last']:
			invalids.append("Last name cannot be blank")    
		elif len(post_data['last']) < 2:
			invalids.append("Last name too short")
		if not post_data['email']:
			invalids.append("Email cannot be blank")
		elif not EMAIL_REGEX.match(post_data['email']):
			invalids.append("please enter a valid email address")
		if not post_data['password']:
			invalids.append("password cannot be blank")    
		elif len(post_data['password']) < 8:
			invalids.append("Password must be at least 8 characters!")
		elif post_data['password'] != post_data['confirm']:
			invalids.append("Password and confirmation must match")
		if invalids:
			return {"successful":False , "invalids":invalids}
		else:
			encoded = post_data['password'].encode()
			hashed_pw = bcrypt.hashpw(encoded, bcrypt.gensalt())
			Users.objects.create(first_name=post_data['first'], last_name=post_data['last'], email=post_data['email'], pw_hash=hashed_pw)
			new_user = Users.objects.get(email=post_data['email'])
			return {"successful":True, "user":new_user}
	def login_val(self, post_data): 
		user = Users.objects.filter(email=post_data['email'])
		print user[0].email
		if user:
			encoded = post_data['password'].encode()
			if  user[0].pw_hash.encode() == bcrypt.hashpw(encoded, user[0].pw_hash.encode()):
				return {'successful': True, 'user': user[0]}
			return {'successful': False} 	

class Users(models.Model):
	first_name = models.CharField(max_length = 100) 
	last_name = models.CharField(max_length = 100)
	email = models.CharField(max_length = 255)
	pw_hash = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	usersManager = UsersManager()
	
