from typing import Type
from accounts.models import Account, UserProfile
from django.shortcuts import get_object_or_404, render, redirect
from .forms import RegistrationForm, UserForm, UserProfileForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required

#verification 
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


from carts.views import _cart_id
from carts.models import Cart, CartItem
from orders.models import Order, OrderProduct


import requests

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']

            username = email.split("@")[0]

            # our create_user has no phone value
            user = Account.objects.create_user(first_name=first_name, 
            last_name=last_name, email=email, username=username, password=password)

            user.phone = phone
            user.save()

            # creating automatic user profile upon saving 
            profile = UserProfile()
            profile.user_id = user.id
            profile.profile_picture = 'default/default.png'
            profile.save()



            # user activation by email
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            mail_body = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)), #encoding id
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, mail_body, to=[to_email])
            send_email.send()


            # messages.success(request, 'We have sent you an email to activate your account.')
            return redirect('/accounts/login?command=verfication&email='+email)
    else: 
        form = RegistrationForm()

    context = {
        'form':form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            try: 
                # checking if there are items in cart then assign them to user before logging in
                cart = Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)

                    # getting product variations by cart id
                    product_variation = []
                    for item in cart_item:
                        variation = item.variations.all()
                        product_variation.append(list(variation)) # as queryset need to convert to list

                    # get cart items from the user to access his product variations
                    cart_item = CartItem.objects.filter(user=user)
                    # existing variations
                    ex_var_list = []
                    id = []
                    for item in cart_item:
                        existing_variation = item.variations.all()
                        ex_var_list.append(list(existing_variation))
                        id.append(item.id)
                    
                    # getting common product variation
                    for prod in product_variation:
                        if prod in ex_var_list:
                            index = ex_var_list.index(prod)
                            item_id = id[index]
                            item = CartItem.objects.get(id=item_id)
                            item.quantity += 1
                            item.user = user
                            item.save()
                        else:
                            cart_item = CartItem.objects.filter(cart=cart)
                            for item in cart_item:
                                item.user = user
                                item.save()
            except:
                pass

            auth.login(request, user)
            
            url = request.META.get('HTTP_REFERER') # to get previous page link
            try: 
                # pass
                query = requests.utils.urlparse(url).query
                # next=/cart/checkout/
                # print('query', query)

                
                params = dict(x.split('=') for x in query.split('&'))
                # print('params', params)
                # same logic as above but simpler
                if 'next' in query:
                    # nextPage = str(query.split('=')[1])
                    nextPage = params['next']
                    messages.success(request, 'You are now logged in!')
                    return redirect(nextPage)
            except:
                messages.success(request, 'You are now logged in!')
                return redirect('dashboard')
                
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('login')

    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')

 # user.is_active will be true with this operations


def activate(request, uidb64, token):
    # print(uidb64, token)
    # decoding user id
    
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)

    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True

        user.save()
        messages.success(request, 'Congratulations! Your account has been activated.')
        return redirect('login')
    
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')


@login_required(login_url='login')
def dashboard(request):
    orders = Order.objects.order_by('-created_at').filter(user_id=request.user.id, is_ordered=True)
    order_count = orders.count()
    
    user_profile = UserProfile.objects.get(user_id=request.user.id)

    context = {
        'order_count': order_count,
        'user_profile': user_profile
    }
    return render(request, 'accounts/dashboard.html', context)


def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
    
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__iexact=email)
            # password change verification via email
            current_site = get_current_site(request)
            mail_subject = 'Reset your password'
            mail_body = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)), #encoding id
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, mail_body, to=[to_email])
            send_email.send()
            messages.success(request, 'Password reset email has been sent to your account.')
            return redirect('login')

        else:
            messages.error(request, 'Account does not exists.')
            return redirect('forgotPassword')


    return render(request, 'accounts/forgotPassword.html')


def reset_password_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)

    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        # saving the uid in session
        request.session['uid'] = uid
        messages.success(request, 'Reset your password.')
        return redirect('resetPassword')
    
    else:
        messages.error(request, 'This link has been expired.')
        return redirect('login')


def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
    
        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else: 
            messages.error(request, 'Passwords do not match')
            return redirect('resetPassword')
    else:
        return render(request, 'accounts/resetPassword.html')

@login_required(login_url='login')
def my_orders(request):
    orders = Order.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
    context = {
        'orders': orders
    }
    return render(request, 'accounts/my_orders.html', context)

@login_required(login_url='login')
def edit_profile(request):
    # fetching the user profile to update it.
    user_profile = get_object_or_404(UserProfile, user=request.user)
    # updating both user and userprofile 
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form  = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('edit_profile')
    
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    context = {
        'user_form': user_form,
        'profile_form' : profile_form,
        'user_profile': user_profile
    }
    return render(request, 'accounts/edit_profile.html', context)


@login_required(login_url='login')
def change_password(request):

    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = Account.objects.get(username__exact=request.user.username)

        if new_password == confirm_password:
            # checking current password
            success = user.check_password(current_password)
            if success:
                # setting the the new password
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Your password has been updated successfully.')
                return redirect('dashboard')

            else:
                messages.error(request, 'Your current password is incorrect.')
                return redirect('change_password')
        
        else:
            messages.error(request, 'Password does not match')
            return redirect('change_password')
    
    else:
        return render(request, 'accounts/change_password.html')


@login_required(login_url='login')
def order_detail(request, order_id):
    order_detail = OrderProduct.objects.filter(order__order_number=order_id)
    order = Order.objects.get(order_number=order_id)

    subtotal = 0
    for i in order_detail:
        subtotal += i.product_price * i.quantity

    context ={
        'order_detail': order_detail,
        'order': order, 
        'subtotal': subtotal
    }

    return render(request, 'accounts/order_detail.html', context)