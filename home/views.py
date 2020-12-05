from django.shortcuts import render, get_object_or_404,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post,Orders
from .forms import postorderForm
from django.shortcuts import render, redirect

def main(request):
    return render(request,'home/main.html')


def home(request):
    context = {
        'orders': Orders.objects.all()
    }
    return render(request, 'home/home.html', context)


def payment(request):
    return render(request, 'home/payment.html')




def order_bid(request):
    return render(request, 'home/order_bid.html')


def home2(request):
    return render(request, 'home/home2.html')




def post_order(request):
    if request.method == 'POST':
        form = postorderForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = postorderForm()
    return render(request, 'home/post_order.html', {'form': form})



class PostListView(ListView):
    model = Post
    template_name = 'home/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


def contact(request):
    return render(request, 'home/contact.html', {'title': 'About'})

