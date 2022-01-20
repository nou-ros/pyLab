from .models import CartItem, Cart
from .views import _cart_id

# for cart counter in the nav
def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            #if user logged in show his cart
            if request.user.is_authenticated:
                cart_items = CartItem.objects.all().filter(user=request.user)
            # normally show cart by cart's id in session.
            else:
                cart_items = CartItem.objects.all().filter(cart=cart[:1])

            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0

    
    return dict(cart_count=cart_count)