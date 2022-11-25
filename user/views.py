from django.shortcuts import redirect, render
from .forms import UserCreateForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def register(request):
    
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            username = form.save(commit=False)
            username.set_password(form.cleaned_data['password1'])
            #username = form.cleaned_data['username'] 
            username.save()
            messages.success(request,f'تهانينا {username} لقد تمت عملية التسجيل بنجاح')
            return redirect('user:login')
    else:
        form = UserCreateForm()
    
    context= {
        'title': 'التسجيل',
        'form' : form,
    }
    return render(request, 'user/register.html', context)

def login_user(request):
    
    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user:profile')
        else:
            messages.warning(request, "هناك خطأ في اسم المستخدم أو كلمة المرور!")
        
    else:
        form = LoginForm()
    context = {
        'title': 'تسجيل الدخول',
        'form': form,
    }
    return render(request, 'user/login.html', context)

def Logout_user(request):
    logout(request)
    context = {
        'title': 'تسجيل الخروج'
    }
    return render(request, 'user/logout.html', context)

@login_required(login_url='user:login')
def profile(request):
    
    posts = Post.objects.filter(author=request.user)
    post_list = Post.objects.filter(author=request.user)
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_page)
    context = {
        'title': 'الملف الشخصي',
        'posts': posts,
        'page' : page,
        'post_list': post_list,
    }
    return render(request, 'user/profile.html',context)


@login_required(login_url='user:login')
def profile_update(request):
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        user_form.save()
        profile_form.save()
        messages.success(request, 'تم تعديل الملف الشخصي بنجاح!')
        return redirect('user:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'title': 'تعديل الملف الشخصي',
        'user_form': user_form,
        'profile_form': profile_form,
    }

    
    return render(request, 'user/profile_update.html', context)