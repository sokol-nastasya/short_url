from django.db import models
from django.contrib.auth.models import User
from .utils import code_generator,create_shortlink

SHORT_TEXT = 20

class Urls(models.Model):
	url = models.CharField(max_length = 220)
	short_link = models.SlugField(max_length = 6, unique = True, blank = True)
	text = models.TextField(null = True, blank = True, default = 'Text')
	date = models.DateTimeField(auto_now_add = True, blank = True, null = True)
	active = models.BooleanField(default = True)
	count = models.IntegerField(default = 0)
	# author = models.ForeignKey(User, on_delete = models.CASCADE)

	def save(self, *args, **kwargs):
		if self.short_link is None or self.short_link == "":
			self.short_link = create_shortlink(self)
		super(Urls, self).save(*args, **kwargs)

	def __str__(self):
		return self.url

	def get_short_url(self):
		return "http://domain.com/{short_link}".format(short_link = self.short_link)

	def get_symb(self):
		return '<TM>'.join(self.text[i:i+6] for i in range(0, len(self.text), 6))


