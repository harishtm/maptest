from apptest.forms import UserForm
from apptest.models import *
from django.shortcuts import render
from django.contrib.auth.models import User

def create_user(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit = False)
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            u = User.objects.create_user(username = username,email = email,password=password)
            user_profile = UserProfile.objects.create(user = u,
                                        description = request.POST.get('description'),
                                        phone1 = request.POST.get('phone1'))
            cont_type = ContentType.objects.get_for_model(UserProfile)
            address_obj = Address.objects.create(content_type = cont_type,object_id = user_profile.id,
                                    address1 = request.POST.get('address1'),
                                    pincode = request.POST.get('pincode'),
                                    state = request.POST.get('state'),
                                    country = request.POST.get('country')
                                    )
            
            #f.save()
        else:
            form = UserForm(request.POST)
    return render(request, 'create_user.html', locals())


def list_all_user(request):
    user_list = User.objects.all()
    return render(request, 'list_all_user.html', locals())
