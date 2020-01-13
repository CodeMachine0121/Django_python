from django.shortcuts import render
from .models import Vendor
from .forms import VendorForm
# Create your views here.
'''
    render 就是Django提供你很多方便你操作的函式，
    而rendor可以將我們要傳達的資料一併打包，
    再透過 HttpResponse 回傳到瀏覽器
'''

def vendor_index(request):
    vendor_list = Vendor.objects.all() #Get all data 

    #前面的vendor_list 是要傳給template的變數名字
    context = {'vendor_list':vendor_list}

    return render(request,'detail.html',context) 
    # 要去template 改html


def showTemplate(request):
    vendor_list = Vendor.objects.all()
    context = {'vendor_list':vendor_list}
    return render(request,'vendor/vendor_detail.html',context)


# 建立表單 要自己新增 forms.py
def vendor_create_view(request):
    form = VendorForm(request.POST or None)

    if form.is_valid():
        form.save()
        #為了確保 form 真的有新增資料 => 清空 form
        form = VendorForm()
    context ={
        'form':form
    }
    return render(request,"vendor/vendor_create.html",context)

    """
    as_p 是新的夥伴，而它就是 Django 提供給 forms 顯示的一種方式，目前總共有 3 種方式，分別是

    as_table
    as_p
    as_ul

    但為了 防止 CSRF攻擊 要再html裡而外加 {%csrf_token%}
    """