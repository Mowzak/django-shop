
from django.db.models.expressions import Random
from app.templatetags import tag
from django.shortcuts import get_object_or_404, render,redirect,reverse
from . import models
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as logi
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect, request
from django.core.paginator import Paginator
from django.utils.translation import gettext as _


from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from .form import checkoutform
from .templatetags import tag
from .task import randomint
from bs4 import BeautifulSoup
# Create your views here.
def home(request): 
    t = models.glasses.objects.all()
    t.reverse()
    return render(request,'s/index.html',context={"favs":models.fav.objects.get(id=1).fav.all(),'arash':models.homeview.objects.all(),'fo':models.glasses.objects.all()[:4],'blog':models.glasses.objects.all()[::-1][:3],'se':models.glasses.objects.all()[3:]})
@login_required(login_url="signup")
def profile(request):

    if request.POST:
        post = models.glasses.objects.get(id=request.POST["remove_btn"])

        models.savee.objects.get_or_create(user=request.user)[0].post_save.remove(post)

        lst = models.savee.objects.get(user=request.user).post_save.all()

        counter = 0
        for i in lst:
            counter+=int(i.price.replace(",",""))
        return render(request,'s/profile.html',context={'total':counter,'produc':lst,'tedad':len(lst)})

        
    lst = models.savee.objects.get_or_create(user=request.user)[0].post_save.all()
    

    counter = 0
    for i in lst:
        try:
            counter+=int(i.price.replace(",",""))
        except ValueError:
            t = models.glasses.objects.filter(price=i.price)
            t.delete()
    return render(request,'s/profile.html',context={'total':counter,'produc':lst,'tedad':len(lst)})

def us(r):
    return render(r,"s/about.html",{'c':models.us.objects.get(id=1)})

def shop(request,page_id=1):
    if request.method=="POST":

        if len(request.POST)==4:
            if not request.user.is_authenticated:
                return redirect("signup")

            elif 'id' in request.POST:
                return reverse('like',kwargs={'ido':request.POST['id']})
            else:
                post = models.glasses.objects.get(id=request.POST['add_card'])
                models.savee.objects.get_or_create(user=request.user)[0].post_save.add(post)
                return redirect("prof")

        else:
            lst = models.glasses.objects.filter(title__contains=request.POST['search'])
            if request.POST['drop1']=='':
                return render(request,'s/shop.html',context={'glass':lst,'counter':len(lst),'produc':lst})
            if request.POST['drop1']=='1':
                co =sorted(lst,key=lambda x:int((x.price).replace(",","")))
                context = {'glass':co,'counter':len(co),'produc':lst}
                return render(request,'s/shop.html',context=context)
            if request.POST['drop1']=='2':
                co=(sorted(lst,key=lambda x:int((x.price).replace(",","")),reverse=True))
                context = {'glass':co,'counter':len(co),'produc':lst}
                return render(request,'s/shop.html',context=context)

    else:
        co = models.glasses.objects.all()
        paginator = Paginator(co, 50)
        page_obj = paginator.get_page(page_id)

        context = {'glass':page_obj,'counter':len(co),'page':paginator}
        return render(request,'s/shop.html',context=context) 

def shopdet(request,post_id):
    if request.method=="POST":
        if not request.user.is_authenticated:
            return redirect("signup")

        
        if 'comment' in request.POST:
            sav = models.comment(comment=request.POST['comment'],user=request.user,proid=models.glasses.objects.get(id=int(post_id)))
            sav.save()
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        

        else:
            post = models.glasses.objects.get(id=request.POST['add_card'])
            s = models.savee.objects.get_or_create(user=request.user)
            s[0].post_save.add(post)
            return redirect("prof")
    else:
        t = get_object_or_404(models.glasses, id=post_id)
        #like 
        like_obg = models.like.objects.get_or_create(post=models.glasses.objects.get(id=int(post_id)))
        if like_obg[0].likee.filter(username=request.user).exists():
            not_active = True
        else:
            not_active = False
        like_c = like_obg[0].line_counter()
        return render(request,'s/shop-detail.html',context={'like_c':like_c,'not_active':not_active,'comment':models.comment.objects.filter(proid=post_id,active=True)[::-1],
                    'all':models.glasses.objects.all(),"det":t})


def like(request,ido):

    p = models.glasses.objects.get(id=ido)
    t = models.like.objects.get(post=p)
    if request.method=="POST":
        if not request.user.is_authenticated:
            return redirect("signup")
        
        elif t.likee.filter(username=request.user).exists():
            s = models.like.objects.get_or_create(post=p)

            s[0].likee.remove(request.user)

        else:
            s = models.like.objects.get_or_create(post=p)
            s[0].likee.add(request.user)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    

def checkout(r):
    if r.method=="POST":
        form = checkoutform(r.POST)
        if form.is_valid():
            if models.checkout.objects.filter(user=r.user).exists():
                models.checkout.objects.filter(user=r.user).delete()

            userma = User.objects.get(username=r.user)
            post = form.save(commit=False)
            form.instance.user = userma
            post.price = tag.total_price(r.user)

            post.tracing = randomint()
            post.save()
            return render(r, 's/suscheckout.html',{'code':post.tracing,'name':post.firstname})
        else:
            error = []
            
            errorlst = {'postcode':'کدپستی صحیح نیست',
'phone_number':'تلفن همراه صحیح نیست',
"house_number":'تلفن ثابت صحیح نیست'}
            for i in errorlst:
                if i in form.errors:
                    error.append(errorlst[i])
            return render(r, 's/checkout.html', {'form': form,'error':error})
    else:
        form = checkoutform()
    return render(r, 's/checkout.html', {'form': form})
    
    




def signin(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = AuthenticationForm()
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("prof")
        else:
            return render(request,'s/signin.html',{'form':form,"eror":"رمز عبور یا نام کاربری اشتباه است"})
    else:
        return render(request,'s/signin.html',{'form':form})


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = UserCreationForm()
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # login(request)
            user = authenticate(request, username=request.POST.get("username"),
            password=request.POST.get("password1"))
            login(request, user)
            return redirect('prof')
        else:
            if 'two password fields didn’t match' in str(form.errors):
                error = 'دو فیلد رمز عبور مطابقت ندارند.'
            else:
                soup = BeautifulSoup(str(form.errors), 'html.parser')
                error = [i.string for i in soup.find_all('li')][1]

            return render(request,'s/signup.html',{'form':form,'error':error})
    else:
        return render(request,'s/signup.html',{'form':form})


def logout(request):
    logi(request)
    return redirect("signin")


def coming(request):
    return render(request,"s/coming.html")
