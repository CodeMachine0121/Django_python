from django.db import models

from django.contrib import admin
from django.utils.translation import gettext as _
# Create your models here.
''''
資料名稱是<Vendor: Vendor object (1)>，實在不太方便
=> 要將回傳的資料變得具有可讀性,
   將它的值設定為我們所熟知或是方便辨識的內容
=>覆寫 __str__ , 它會去改變資料所要顯示的值
'''
# id,PK Django自動給了 
#要自訂在欄位上 primary_key=True 
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=20)
    store_name  = models.CharField(max_length=10)
    phone_number =models.CharField(max_length=20)
    address =models.CharField(max_length=100)
    
    def __str__(self):
        return self.vendor_name

class Food(models.Model):
    food_name = models.CharField(max_length=30)
    # decimal_places: 小數點後幾位
    price = models.DecimalField(max_digits=3,decimal_places=0)
    #代表食物是哪間攤販 
    '''
        最關鍵的地方在最後一個 ForeignKey，在 Django中是 多對一(many-to-one)的關聯，
        而前方的參數代表的意思就是對應到哪一個類別，這裡對應到的是 Vendor，而後方的 
        on_delete 代表的是當對應的類別被刪除之後，這些對應到別人的資料要怎麼被處理，
        而 CASCADE 就是一倂刪除
    '''
    food_vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)

    #寫完去setting 加上 "vendor.apps.VendorConfig(去看 app底下的app.py) or vendor
    #再下 python manage makemigrations "app name"

    #如果要 superuser能夠處理 要去 app底下admin.py import models 跟註冊 


    def __str__(self):
        return self.food_name


# 用來管理 攤販ID
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    #決定要顯示啥項目
    #list_display =["id","vendor_name"]
    #選擇不填鴨
    list_display = [field.name for field in Vendor._meta.fields]
    # 寫完後要去amdin.py設定 , 太麻煩了 於是用 @admin.register(Vendor)
    #記得註解掉 admin.py裡的設定 (整個弄掉)


'''
只想要找 >50價位的麵包，但是資料庫顯示的資料可能有 
    60 65 70... 各種價位的麵包，這時候你便可以自行設定
'''
class Morethanfifty(admin.SimpleListFilter):
    #要找的變數
    title=_("price")
    parameter_name = "compareprice" #url 後面要接的參數
    def lookups(self,request,model_admin):
        return (
            ('>50',_(">50")), # 前方對應下方'>50'(也就是url的request)，
                              #  第二個對應到admin顯示的文字
            ('<=50',_("<=50")),
        )
    #定義查詢時的過濾條件
    def queryset(self,request,queryset):
        if self.value() == ">50": # greater than 
            return queryset.filter(price__gt=50) 
        if self.value() == "<=50": # low or equal than 
            return queryset.filter(price__lte=50)

# 用來管理 菜單
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display =[field.name for field in Food._meta.fields]

    #過濾price
    list_filter=(Morethanfifty,)

    #顯示欄位 只能改該欄位
    fields=["price"] 
    #exclude是除了...之外
    #exclude=["food_name","food_vendor"]

    #搜尋欄位
    search_fields=("food_name","price")

    #排序
    #ordering=('price',)#價格 由小到大
    ordering=('-price',)# 由大到小