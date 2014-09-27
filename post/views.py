from django.shortcuts import render

# Create your views here.


from post.models import Post 

def index(request):
	posts = Post.objects.all()

	context = {
		'posts': posts
	}

	return render(request, 'index.html', context)

def post(request, post_id):
	post = Post.objects.get(id=post_id)

	context = {
		'post': post
	}

	return render(request, 'post.html', context)