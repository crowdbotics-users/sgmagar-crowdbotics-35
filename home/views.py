from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'dj-paypal', 'url': 'http://pypi.python.org/pypi/dj-paypal/0.6.0'},
	{'name':'dj-stripe', 'url': 'http://pypi.python.org/pypi/dj-stripe/1.0.0.post1'},
	{'name':'django-paypal', 'url': 'http://pypi.python.org/pypi/django-paypal/0.4.1'},
	{'name':'cmsplugin-twitter', 'url': 'http://pypi.python.org/pypi/cmsplugin-twitter/1.1.2'},
    ]
    context = {
        'title': 'sgmagar-crowdbotics-35',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
