from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from django_htmx.http import trigger_client_event
from .models import Cart, CartItem
from products.models import Product


def get_or_create_cart(request):
    """Get or create cart for authenticated/anonymous users"""
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, _ = Cart.objects.get_or_create(session_key=session_key)
    return cart

@require_http_methods(["GET"])
def cart_view(request):
    cart = get_or_create_cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})

@require_http_methods(["POST"])
def add_to_cart(request, product_id):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    item, created = CartItem.objects.get_or_create(
        cart=cart, 
        product=product
    )
    if not created:
        item.quantity += 1
        item.save()

    # Return partial template instead of redirect
    response = render(request, 'cart/navcart.html', {'cart': cart})
    return response

@require_http_methods(["POST"])
def remove_from_cart(request, item_id):
    cart = get_or_create_cart(request)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    item.delete()
    
    response = render(request, 'cart/_cart_items.html', {'cart': cart})
    trigger_client_event(response, 'cartUpdated')
    return response

@require_http_methods(["POST"])
def update_cart_item(request, item_id):
    cart = get_or_create_cart(request)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    action = request.GET.get('action', 'increment')
    
    if action == 'increment':
        item.quantity += 1
    elif action == 'decrement':
        item.quantity = max(1, item.quantity - 1)
        # item.quantity -= 1
    else:
        raise ValueError(f"Invalid action: {action}")
    
    # TODO: Implement auto delete upon quantity <= 0
    if item.quantity <= 0:
        remove_from_cart(request, item_id)
        context = {'cart': cart}
        # return HttpResponse(status=204)  # No content
    else:
        item.save()
        context = {
            'item': item,
            'cart': cart
        }
    
    # item.save()
    # context = {
    #     'item': item,
    #     'cart': cart
    # }
    
    # response = render(request, 'cart/_cart_items.html', {'cart': cart})
    response = HttpResponse(item.quantity)  # No content
    response = render(request, 'cart/update_response.html', context)
    trigger_client_event(response, 'cartUpdated')
    return response

@require_http_methods(["GET"])
def cart_partial(request):
    cart = get_or_create_cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})
    # response = HttpResponse(status=204)  # No content
    trigger_client_event(response, 'cartUpdated')

@require_http_methods(["GET"])
def cart_items_partial(request):
    cart = get_or_create_cart(request)
    return render(request, 'cart/_cart_items.html', {'cart': cart})

@require_http_methods(["GET"])
def nav_cart_partial(request):
    cart = get_or_create_cart(request)
    return render(request, 'cart/navcart.html', {'cart': cart})