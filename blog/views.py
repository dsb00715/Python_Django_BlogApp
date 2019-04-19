from django.shortcuts import render

posts = [
    {
        'author' : 'Deep Bhatt',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'April 18, 2019'
    },
    {
        'author' : 'Shraddha Bhatt',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'April 19, 2019'
    },
    {
        'author' : 'Adwait Pandya',
        'title' : 'Blog Post 3',
        'content' : 'third post content',
        'date_posted' : 'April 20, 2019'
    },
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
