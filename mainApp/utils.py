import random
import string


def code_generator(size = 6, chars = string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


def create_shortlink(instance, size = 6):
	new_link = code_generator(size = size)
	NClass = instance.__class__
	qs_exists = NClass.objects.filter(short_link = new_link).exists()
	if qs_exists:
		return create_shortlink(size = size)
	return new_link