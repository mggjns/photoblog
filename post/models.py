from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Post(models.Model): 
	author = models.ForeignKey(User)
	content = models.TextField()
	photo = models.ImageField(upload_to='photos')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "Post {} written by {}".format(self.id, self.author.username) 
# null=True -- can be left empty
