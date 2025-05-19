from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from .models import UserData

# Create your views here.

@login_required
def user(request):
    if request.method == 'POST' and request.POST.get('btn_update') == 'clicked':
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        try:
            user_social = UserSocialAuth.objects.get(user_id=request.user.id)
            UserData.objects.update_or_create(
                user_social=user_social,
                defaults={'phone': phone, 'address': address}
            )
        except UserSocialAuth.DoesNotExist:
            pass
    email = request.user.email
    first_name = request.user.first_name
    last_name = request.user.last_name

    try:
        user_social = UserSocialAuth.objects.get(user_id=request.user.id)
        user_data, _ = UserData.objects.get_or_create(
            user_social=user_social,
            defaults={'phone': '', 'address': ''}
        )
    except UserSocialAuth.DoesNotExist:
        user_data = None

    return render(request, 'user/user.html', {
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'user_data': user_data

    })

