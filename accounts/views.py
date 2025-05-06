from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings    
from store.models import Order, Product


@login_required
def user_profile(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')[:5]  # Get the last 5 orders
    recommended_products = Product.objects.filter(is_new=True).order_by('?')[:6]  # Random 6 new products

    return render(request, 'accounts/profile.html', {
        'user': request.user,
        'orders': orders,
        'recommended_products': recommended_products
    })

class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        self.extra_context = self.extra_context or {}
        next_url = request.GET.get('next', '')
        self.extra_context['next'] = next_url
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        next_url = request.POST.get('next') or request.GET.get('next')
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        redirect_to = self.request.POST.get('next') or self.request.GET.get('next')
        if redirect_to and url_has_allowed_host_and_scheme(redirect_to, allowed_hosts={self.request.get_host()}):
            return redirect_to
        return self.get_redirect_url() or settings.LOGIN_REDIRECT_URL


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # or dashboard

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})
