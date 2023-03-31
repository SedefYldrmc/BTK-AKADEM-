"""message="Hello there .My name is Sadık Turan.".split()
print(message)
#string  içindeki her karakter aslında bir listenin bir öğesini temsil ediyor.
#split ile de her bir boşluktan ayırıp ekrana yazdırır
#her kelimeye indeks ile ulaşilabilir
my_list=[1,2,3]
my_list=["bir",2,True,5.6]
print(my_list)
list1=["one","two","there"]
list2=["four","five,","six"]
numbers=list1+list2
print(numbers)
print(len(numbers))
print(message[0])
"""
"""
userA=["Sadık", 36]
userB=["Cinar", 2]

users=[userA,userB]
print(users)
print(users[1][1])"""


#uygulamalar:"""
"""list=["Bmw","Mercedes","opel","Mazda"]
#1-"Bmw ,Mersedes,Opel,Mazda" elemanlarına sahip bir liste oluşturununz:
# mazda degerin toyata ile değiştirin:
list[3]="toyata"
print(list)
#Mersedes listenin bir elemanı mıdır?
a='Mercedes' in list
print(a)
#listenin soniki elemanı yerine "toyota" ve " renult" değerlerini ekleyin:
list[-2:]='toyota','renult'
print(list)"""
#listenin üzerine "audi" ve nissan ekleyin"""
'''list.append('audi')
list.append('nissan')
print(list)'''


"""list=list+['audi',"Nissan"]
print(list)"""

"""a=list[::-1]
print(a)"""

#""" 12- Asağidaki  verileri bir liste içinde saklayınız:
       #studentA:yiğit bilgi 2010,(60,70,60)
       #studentB:Sena Turan 1999,(80,80,70)
       #studentC:Ahmet Turan 1998,(80,70,90)
"""studentA=['Yiğit',' bilgi',2010,[70,60,70]]
studentB=['Sena','Turan',1999,[80,80,70]]
studentC=['Ahmet','Turan',1998,[80,70,90]]

list=[studentC+studentB+studentA] 
print(list) """     

 
#Pythonda TUPLE:
"""list=[1,2,3]
tuple=1,"3",6
print(type(list))
print(type(tuple))
print(len(tuple))
print(tuple[2])"""
#listede herhengi bir indekdini değiştirebilirsek bile 
#tupleda herhangi bir elemanı değiştirilemiyor

# DİCTİONARY:
#key-value şeklinde çalişir:
"""sehirler=['kacaeli','istanbul']
plakalar=[41,34]
print(plakalar[sehirler.index('istanbul')])"""

"""plakalar={'kacaeli':41,'istanbul':34}
print(plakalar['istanbul'])

plakalar['ankara']=6
print(plakalar)

plakalar['kacaeli']='new value'
print(plakalar)
"""
users={
       'sadıkturan':{
              'age':36,
               'roler':['user'],
              'email':'sadık@gmail.com',
              'adress':'kocaeli',
              'phone':'02201020101'
               },
       'cinarturan':{
              'age':2,
              
              'roler':['admin','user'],
              'email':'cinar@gmail.com',
              'adress':'istanbul',
              'phone':'02201020101'
               }}

"""print(users['cinarturan'])

print(users['cinarturan']['age'])
#UYGULAMALAR:
ogrenciler={}
no=input("öğrenci numarası:")
ad=input("isim :")"
soyad=input("soyadı :")
telefon=input("telefon:")
ogrenciler[no]={
       'ad':ad,
       'soyad':soyad,
       'telefon':telefon,           
}
print(ogrenciler)"""

#yanı şeyi update ile de yapabiliriz:
"""
ogrenciler={}
no=input("öğrenci numarası:")
ad=input("isim :")
soyad=input("soyadı :")
telefon=input("telefon:")
ogrenciler.update({
       no:{
            'ad':ad,
          'soyad':soyad,
          'telefon':telefon
       

}}
)


no=input("öğrenci numarası:")
ad=input("isim :")
soyad=input("soyadı :")
telefon=input("telefon:")
ogrenciler.update({
       no:{
            'ad':ad,
          'soyad':soyad,
          'telefon':telefon
       

}})

no=input("öğrenci numarası:")
ad=input("isim :")
soyad=input("soyadı :")
telefon=input("telefon:")
ogrenciler.update({
       no:{
            'ad':ad,
          'soyad':soyad,
          'telefon':telefon
       

}})

no=input("öğrenci numarası:")
ad=input("isim :")
soyad=input("soyadı :")
telefon=input("telefon:")
ogrenciler.update({
       no:{
            'ad':ad,
          'soyad':soyad,
          'telefon':telefon
       

}})
print(ogrenciler)
# arama yapma ve bulma:
ogrno=input('öğrenci no giriniz:')
ogrenci=ogrenciler[ogrno]

print(f"Aradığınız {ogrno} nolu öğrencinin adı:{ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")"
"""
"""#SETLER:

fruit={'orange','apple','banana'}
#indekslenemez(print(fruit[0])):
#listelenemz:

for i in fruit:
        print(i)
#Eleman tekraru olmaz:
#eleman ekleme:
fruit.add('cherry')
fruit.update(['Mango','grape'])
print(fruit)
fruit.discard('apple')

#Value and Refence Types:
#value types=> string,number
x=5
y=25
x=y
y=10
print(x,y)

#referens types: =>list
a=["apple","banana"]
b=["apple","banana"]
a=b
b[0]="grape"
print(a,b)
"""

# Atama operatörleri:
#x=5
#y=10
#z=20

#x,y,z=5,10,20
#x,y=y,x
#x=x+5,x+=5 aynı şey

#x%=5x in 5 e bölümden kalan
#x//=5x in 5 e bölümde bölüm
#x**=5 x üzeri 5 olarak alır.
#print(x,y,z)
"""
values=1,2,3,5,6,8

print(values)
print(type(values))
x,y,*z =values

print(x,y,z)
"""
"""x,y,z=5,10,20
numbers=1,5,7,10,6
# atama operatörleri uygulama:
# kullanıcıdan aldığınız 2 sayınıı çarpımı ile z,y,x toplamının farkı nedir?
a=int(input("a="))
b=int(input("b="))
result=a*b-(x+y+z)print(result)
#y nin x e kalansız bölümünu hesaplayınız:
result=y//x
print(result)

#x y z toplamının mod 3 ü nedir?
print((x+y+z)%3)
#y nin x. kuvvetini hesalayınız:
print(y**x)
#x, *y, z =numbers işlemine göre z nını küpü kaçtır?
x,*y,z=numbers
print(z**3)
#x, *y, z = numbers işlemine göre y nin değerleri toplamıı kaçtır?
numbers=x,*y,z
print(y[0]+y[1]+y[2])
"""

#karşılaştırma operatörleri:
# username ,password => database
# 'sadıkturan' ,'123456'
"""username='sadıkturan'
password='123456'
a,b,c,d=5,5,10,4
result=a==b#True
result=a==c # False
result=('sdktrn'==username)
result=(a!=b)
result=(a!=c)"""

# Mantıksal operatörler:(logical operatörler)
"""x=5
result=5<x<10
print(result)
#and
result=(x>5) and (x<10) #True, True=> True
#or
result=(x>0) or (x%2==0)
#True, False=>True
#True, True=>True
#false, false=>false

#NOT
result=not(x>0)
print(result)

#UYGULAMA:
x=int(input("x sayısını giriniz:"))
emeil="yildirimcisedef@gmail.com"
password='199'
#1-Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz:
result=(x>0) and (x<=100)
print(result)

#2-girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz:
result=(x>0) and (x%2==0)
print(result)
#3-Email  ve parola bilgileri ile giriş kontrolu yapınız:
a=input('meilinizi giriniz')
b=input('şifrenizi giriniz')
result=(a==emeil) and (b==password)
print(result)
#4-Girilen 3 sayıyı büyüklük olarak  karşilaştırınız:
sayı1=int(input("sayı1 sayısını giriniz:"))
sayı2=int(input("sayı2 sayısını giriniz:"))
sayı3=int(input("sayı3 sayısını giriniz:"))
result1=(sayı1>sayı2)
result2=(sayı1>sayı3)
result3=(sayı2>sayı3)
print(result1 , result2 ,result3)

#5-Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hasaplayınız:
vize1=int(input('vize notunu giriniz'))
vize2=int(input('vize2 notunu giriniz:'))
final=int(input('final notunu giriniz:'))
ort=((vize1+vize2)*0.6+(final*0.4))/2
result=((ort>=50) and (final==50)) or (final==70)
print(result)
#EĞER ortalama 50n ve ustundeyse geçti değilse kaldı yazınç
#a-)Ortalama 50 olsa bile final notu en az 50 olmalıdır
#b-)Finalden 70 alındığında ortalamanın önemi olmasın:"""


"""#identity((is)) and membership(in)) operations:
#Identity operator:is
x=y=[1,2,3]
z=[1,2,3]
print(x==y)
print(x==z) #değerler dikkate alınır:

print(x is y)
print(x is z) #referans dikkate alınır:
x=[1,2,4]
y=[2,4]
print(x is y)

#Membership opereator:in
x=['apple','banana']
print('banana' in x)
name='Çınar'
print('a' in name)
"""
#KOŞUL İFADELERİ=====>>>>>
#İF ELSE BLOKLARI:
#İF::::::::(EĞER):
#(bir kod bloğundan başka bir kod bloğuna 
# geçiş yapmakk istiyorsam kullanılır
# kod akişini belli bir şarta bağlı olarak değiştir:)
 
"""if  3>2:
       print('Hoş geldiniz')
if  3==3:
       print('Hoş geldiniz') #ana şartın doğru ise bloğa girer:
if  True:
       print('Hoş geldiniz') # bu 3 şekilde olur 
isLoggedin=True
if isLoggedin:
       print('Hoş geldiniz')  """      

# for döngüleri:
"""numbers=[1,32,3,4]
for num in numbers:
       print(num ,end=' ')
names=['Çınar','Sadık','Sena']
for name in names:
       print(f' my names is {name}')

tuple=(1,2,3,4)
for t in tuple:
       print(t)    
       
tuple=[(1,2),(2,3),(3,4)]
for a,b in tuple:
       print(a,b)   

d={'k2':1,'k2':2,'k3':3}
for key,value in d:
       print(key, value)  """         
       
#while döngüsü:
# 1-100 e kadar yazdır:
"""x=1
while x<=100:
       print(x ,end=',')
       x+=1
print("Bitti...")          

name=''# False
while not name.strip():# baştan ve sondan boşluk karakteri siler:
      name=input("İsminizi giriniz::")
print(f'Merhaba ,{ name }')       
"""
#UYGULAMALAR:
"""sayılar=[1,3,5,7,9,12,19,21]
#1:sayılar listesini while ile ekran yazdırın.
x=0
while x<len(sayılar):
       print(sayılar[x])
       x+=1
       """
#2:Başlangıç ve bitiş değerlerini kullanıcıdan alıp arasındaki tüm tek sayıları ekrana yazdırın.
"""bas=int(input("başalgıç değerini giriniz:"))
bit=int(input("bitiş değerini giriniz:"))

while bas<bit:
       if (bas)%2==1:
              print(bas)
       bas+=1"""
      
#3:1-100 arasındaki sayıları azalan şekilde yazın:
"""x=100
while x>0:
       print(x)
       x-=1"""
#4:Kullanıcıdan alacağinız sınırsız ürün bilgisini urunler listesi içinde saklayın:
"""urun_sayısı=int(input("urun sayısı giriniz:"))
x=0
urunler=[]
while x<urun_sayısı:
       name=input("urun adınını giriniz:")
       price=input("urunun fiyatını giriniz:")
       urunler.append({
            'name':name,
            'price':price  
              
       })
     
       x+=1
for urun in urunler:
       print(f' urun adı: {urun[ "name"]} urun fiyatı {urun["price"]}')


"""

#**ürün sayısını kullanıcıya sorun
#***dictionary listesi yapısı(name,price)şeklinde olsun
#**ürün ekleme işlemi bittiğinde ürünleri ekrana while ile listeleyin:




#BREAK  VE CONTİNUE İFADELERİ:
"""name='Sadık Turan'
 
for letter in name:
       if letter=='u':
              break # döngüyü tamamen sonlandırırken;
       print(letter)
        
for letter in name:
       if letter=='u':
            continue # continue ise sadece geçerli şartı geçip döngüye devam eder.
       print(letter) 
       
x=0
while x<5:
       if x=
       print(x)
       x+=1       =3:
         continue"""
         
#DÖNGÜ METODLARI:range(),zip()enumerate()

#range()
"""liste=[1,2,3]
for item in liste:
       print(item)          
for i in range(2,100,20):
       print(i)
       
print(list(range(2,100,20)))             """

#enumerate:
"""index=0 # Normal hali bu 
greeting="Hello There"
for letter in greeting:
       print(f'index:{ index} letter: { letter}')
       index+=1
       
index=0 #enumerate hali de bu
greeting="Hello There"
for item in enumerate(greeting):
      # print(f'index:{ index} letter: { letter}')
      print(item)
"""
# zip

"""list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
print(list(zip(list1,list2)))
for item in zip(list1,list2):
       print(item)
for a,b in zip(list1,list2):
       print(b)"""
       
   
#list Comprehensions:       

"""numbers=[]
for i in range(10):
       numbers.append(i)
print(numbers)       
# ikiside aynı şey: 
numbers=[x for x in range(10)]
print(numbers) """
#liste = ['ali', 'veli', 'ahmet', 'mehmet', 'celal', 'selin', 'nihat']
#random.choice(liste)
#'ali'
#random.choice(liste)
#'mehmet'
#random.choice(liste)
#'selin'
#kardiz = 'istihza'
#random.choice(kardiz)

#uygulama sayı tahmini:
"""1-100 arasında rasgele sayı üretilecek bir sayıyı
aşağı yukarı ifadeleri ile buldurmaya çalişin
**"random modulu " için "python random " şeklinde arama yapın.
** 100 üzerinden puanlama yapın.her soru 20 puan.
hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın."""



"""import random
x=random.randint(1,100)
kaç_hak=int(input("hak sayısı giriniz:"))
    
for i in range(1,kaç_hak+1):
       tahmin=int(input("tahmin:"))
       if i<kaç_hak:
              if tahmin>x:
                  print("daha aşağıda bir sayı ")             
              elif tahmin==x:
                   print("TEBRİKLER oyunu kazandınız:)")      
              
              else:
                   tahmin<x
                   print(" daha yukarıda bir sayı")
      
       else :
             
              print("ÜZGÜNÜM kaybettiniz :(")
       
       kaç_hak-=1"""
     
#soru Girilen bir sayının asal olup olmadığını bulun:
#**Asal sayı 1 ve kendisi haric tam böleni olmayan sayılara denir. 
"""     
sayı=int(input("sayı giriniz:"))

y=0
for x in range(2,sayı,1):
    if sayı%x==0:
        y+=1
  
        break       
                   
if y==1:
       print(f'{sayı} sayısı asal değildir')           
else:
        print(f'{sayı} sayısı asal ')"""

           
           
               
#pythonda metodlar:
#method
"""list=[1,2,3] # class bünyesinde bir çok  metod bulunduran yapı
list.append(4)
print(list) #  append liste sınıfının bir metodu.
Mystring="hello"
print(type(Mystring))"""

#fonksiyonlar:#aynı metod gibi  belli amaçlara hizmet eder: 
#Fonksiyon kullanımı:
"""def sayHello(name= 'user'):
       print('Hello '+ name)
       
sayHello("sedef")       
sayHello()      
def sayHello(name= 'user'):
       return 'Hello '+ name
s=sayHello('Buğra')
print(s)


def total(num1,num2):
       return num1+num2
result=total(10,20)
result=total(15,20)
print(result)

def yasHesapla(dogumYili):
       return (2023-dogumYili)
age1=yasHesapla(1999)
age2=yasHesapla(2001)
age3=yasHesapla(2000)
print(age1, age2, age3)


def EmekliliğeKaçYılKaldı(dogumYili,isim):
       '''DOCSTING:dogum yiliniza gore emeklilik kaç yil kaldi
       INPUT:Dogum yili
       OUTPUT:Hesaplanan  yil bilgisi
       '''
       yas=yasHesapla(dogumYili)
       emeklilik=65-yas
       
       if emeklilik >0:
              print(f'emekliliğe {emeklilik} yıl kaldı')
       else:
              print('Zaten emekli oldunuz')
EmekliliğeKaçYılKaldı(1983,'sedef')       
print(help(EmekliliğeKaçYılKaldı))"""

#fonksiyon parametreleri:

""""def changeName(n):
       n='ada'
       
name='yiğit'
changeName(name)     
print(name)


def change(n):
       n[0]='İstanbul'
sehirler=['Ankara','İzmir']
change(sehirler)
print(sehirler)     

sehirler=['Ankara','İzmir']
n=sehirler[:] #slincing

n[0]='İstanbul'
print(sehirler) 
print(n)  

"""
"""def add(a,b):
       return sum((a,b))
print(add(10,20)) # iki parametre için

def add(a,b,c=0,d=0,e=0):#böylelikle 5 tane ye kadar değer alır
       return sum((a,b))
print(add(10,20))
print(add(10,20,30))

def add(*params):
       return sum((params))
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,60,50,))


def add(*params):# yukardakinin diğ er sekli
       sum=0
       for n in params:
              sum=sum+n
       return sum       

print(add(10,20,30,60,50,))"""
"""def displayuser(**args):# keyvalue yani dictionry değer alır:
       print(type(args))
       for key,value in args.items():
              print('{} is {}'.format(key,value))


displayuser(name='Çinar', age=2,city='İstanbul')
displayuser(name='ada', age=12,city='Kocaeli',phone=123)
displayuser(name='yiğit', age=14,city='Ankara',phone=123,emeil='sedef')

def myfunc(a,b,c,*args, **kwargs):
       print(a)
       print(b)
       print(args)
       print(kwargs)# anahtar değere karşi gelen değer:
       
myfunc(10,20,30,40,50,key1='value 1',key2='value 2')     
"""

#fonksiyonlar uygulama:
#1-Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
"""def yazdır(a,b):
       for i in range(b):
              print(a)
     
yazdır('sedef',5) """     
  
#2-Kendine gönderilen sınırsız sayıdaki parametreyi listeye çeviren fonksiyon.
"""
def yaz(*param):
    list=[]
    list.append(param)
    print(list)
yaz(1,2,3,4)      """

#3-gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

"""def asal(x,y):
     for sayı in range(x,y+1):
              if sayı >1:
                     for i in range(2,sayı):
                            if (sayı%i==0):
                                   break
                     else:
                            print(sayı)
                                   
x=int(input("x sayısını giriniz:"))
y=int(input("y sayısını giriniz"))                 
asal(x,y)              
             """
    

                            
                           
#4-Kendine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndür.

"""def bolen(c):
       list=[]
       for i in range(1,c+1):
              if c%i==0:
                     list.append(i)
       return list              
print(bolen(12))                     
       """

"""#LAMDA EXPRESİONS,Map ve Filter:
def square(num):return num**2
result=square(2)
print(result)

def square(num):return num**2
numbers=[1,3,5,9]
result=list(map(square,numbers))
#alternatif:ya bir listeyle yada bir for döngüsü ile döndürmesi lazım:

for item in map(square,numbers):
       print(item)

print(result)

#MAP::::>>>>>
# Parametre olarak aldığı fonksiyona, parametre olarak aldığı 
# listenin her elemanını sırasıyla parametre olarak gönderir.
#result=square(2)


#Lambda expression:

numbers=[1,3,5,9]
result=list(map(lambda num:num**2,numbers))


def check_even(num):return num%2==0
result=list(filter(check_even,numbers))
#Çağırılan fonksiyonun döndürdüğü değerin true
# olduğu durumlara göre liste döndürür.
result=check_even(numbers[2])#sadece 2 numaralı indeksi kullanılır.

print(result)"""

#GLOBAL VE LOCAL DEĞİŞKENLER:

#global scope
""""x='global x'

def function():
       #local scope
       x='local x'
       print(x)
function()
print(x)       
       
 #global
name='Çinar'
def changename(new_name):
       #local
       name=new_name
       print(name)
changename('ada')
print(name)             
 
name='global string'
def greeting():
       #name='Çınar'
       def hello():
              #name='Ada'
              print('Hello ' + name)
       hello()
greeting()                    

x=50
def test(x):
       print(f'x :{x}')
       
       x=100
       print(f'changed x to : {x}')
       
test(x)            
#gobal olan x i fonksiyon içindde kullnama       
x=50
def test():
       global x
       print(f'x :{x}')
       
       x=100
       print(f'changed x to : {x}')
       
test()
print(x) # fonsiyon global x i kullanıyor."""
#BANKAMATİK UYGULAMASI:

"""HesapA={
       'ad':'Sadık Turan',
       'hesapNo':'12345678',
       'bakiye':3000,
       'ekHesap':2000,
}

HesapB={
       'ad':'Ali Turan',
       'hesapNo':'12112345678',
       'bakiye':2000,
       'ekHesap':1000,
}



def paraCek(hesap, miktar):
       print(f"Merhaba { hesap['ad']}")
       
       if (hesap['bakiye']>=miktar):
              hesap['bakiye']-=miktar
              print("paranızı alabilirsiniz")
              bakiyeSorgula(hesap)
       else:
              toplam=hesap['bakiye']+hesap['ekHesap']
              if toplam>=miktar:
                     ekhesapkullanımı=input('ek hesap kullanilsin mi?(e/h):')
                     if ekhesapkullanımı=='e':
                            ekhaspkullanılacakmiktar=miktar-hesap['bakiye']
                            hesap['bakiye']=0
                            hesap['ekHesap']-=ekhaspkullanılacakmiktar
                            print('paranızı alabilirsiniz')
                            bakiyeSorgula(hesap)
                     else:
                            print(f"{hesap['hesapNo']} nolu hesabınızda  {hesap['bakiye']} bulunmaktadır")
              else:
                     print(' üzgünüz bakiye yetersiz:')                     
                     bakiyeSorgula(hesap)
                     
def bakiyeSorgula(hesap):
       print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")                 
       
paraCek(HesapA,4000)       

paraCek(HesapA,1)            
              
       """
     
       
       