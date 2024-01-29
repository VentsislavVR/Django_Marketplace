from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from market.core.forms import SignupForm
from market.item.models import Item, Category


# Create your views here.
def index(request):
    items = Item.objects.filter(
        is_sold=False
    )[:6]
    categories = Category.objects.all()

    context = {
        'items': items,
        'categories': categories
    }
    return render(
        request,
        'core/index.html',
        context
    )


class SignInView(auth_views.LoginView):
    template_name = 'core/login.html'


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login user')
    else:
        form = SignupForm()

    context = {
        'form': form
    }
    return render(request, 'core/signup.html', context)


def contact(request):
    return render(request, 'core/contact.html')
