#nesned Fuctions(fonksiyonlarda iç içe fonksiyon):
# bir objedir
"""def greeting(name):
    print("Hello " , name)
    
#print(greeting("sedef"))
# print(greeting) 
sayHello=greeting"""
# print(sayHello)
# print(greeting)  # ikiside aynı adreste kayıt olur sadece isimler farklı olur. 

# print(greeting("ali"))
# print(sayHello("ali")) #ikisine de aynı şeyi yollamaktan bir farkı yok.

# del sayHello
# print(greeting)

#encapsulation:
"""def outer(num1):
    print("outer çalişiyor")
    def inner_increment(num1):
        print("inner çalişiyor")
        num2=num1 + 1 
        print(num1,num2)
    return inner_increment(num1)

outer(4)"""
#inner_increment(4) hata verir.çünkü bu fonksiyon sadece outer kapsamında çalişir.
"""def factorial(number):
    if not isinstance(number,int):
        raise TypeError(" number must be an integer")
    
    if not number >=0:
        raise ValueError("number must be zero or ppozitive")
    
    def inner_facturial(number):
        if number <=1:
            return 1
        return number* inner_facturial(number-1)

    return inner_facturial(number)
try:
   print(factorial("4"))
except Exception as  ex:
    print(ex)
    """
#FONKSİYONDAN FONKSİYON DÖNDÜRME:

"""def us_alma(number):
 
    def inner(power):
        return number ** power
    return inner

two=us_alma(2)  #2-3 ü hesaplar.us_almadan aldığı degeri innera aktarırken power
#değerini de two fonksiyonundana alır.
three=us_alma(3) #3-4 ü hasaplar
print(two(3))
print(three(3))"""

"""def yetki_sorgula(page):
    def inner(role):
        if role=='Admin':
            return "{} rolünün {} sayfasına ulaşılabilir".format(role, page)
        else:
            return "{} rolünün {} sayfasına ulaşılamaz:".format(role, page)    
        
    return inner   
user1=yetki_sorgula("Product Edit")
print(user1("Admin"))
print(user1("user"))"""

"""def islem_adi(islemadı):
    def toplam(args):
        toplam=0
        for i in args:
            toplam+= i
        return toplam
        
    def carpma(*arg):
        carpım=1
        for i in arg:
            carpım*=i
        return carpım 
        
    if islem_adi =="toplama":
        return toplam
    else:
        return carpma 

toplama=islem_adi("toplama")
print(toplama(1,2,3,4))    #burda hata vardı bul!
carpma=islem_adi("carpma")
print(carpma(1,2,3,4)) """ 


#Functions as Parameters:
"""def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4,islemadı):
    if islemadı=="toplama":
        print(f1(2,3))
    elif islemadı=="cıkarma":
        print(f2(5,3))
    elif islemadı=="carpma":
        print(f3(3,4))
    elif islemadı=="bolme":
        print(f4(10,2))
    else:
        print("geçersiz işlem")

islem(toplama,cikarma,carpma,bolme,"toplama") 
islem(toplama,cikarma,carpma,bolme,"cıkarma")  
islem(toplama,cikarma,carpma,bolme,"carpma")  
islem(toplama,cikarma,carpma,bolme,"bolme")  
islem(toplama,cikarma,carpma,bolme,"car")   """

#python  decoretor function:bir fonksiyona yeni bir özellik eklenince kullanılır
"""def my_decoretor(func):
    def wrapper(name):
        print("fonksiyondan önceki olan işlem")
        func(name)
        print("fonksiyondan sonraki işlemler.")
    return wrapper

@my_decoretor
def sayhello(name):
    print("hello",name)
sayHello("ali")   
#sayhello=my_decoretor(sayhello) #şimdilik burayı devre dısı bırakıyoruz:
"""
"""import math
import time
def calculate_time(func):
    def inner(*arg,**kwargs):
        start=time.time()
        time.sleep(1)
        func(*arg,**kwargs) 
         
        finish=time.time()
        print("fonksiyon "+ func.__name__ +str(finish-start)+" saniye sürdü.")
    return inner
@calculate_time
def us_alma(a,b):
    print(math.pow(a,b))
@calculate_time  
def faktoriyel(num):
    print(math.factorial(num)) 
    
us_alma(2,3)
faktoriyel(5)"""

#PYTHONDA İTERATORS:
#liste=[1,2,3,4,5]

# for i in liste:
#     print(i)
# print(dir(liste))
"""iterator=iter(liste) 
print(next(iterator))               
print(next(iterator))        
print(next(iterator)) 
print(next(iterator)) 
print(next(iterator)) 
# print(next(iterator)) # burda stop iteratör hatası döndürecek.
for i in liste:      
    print(i) 
    """
"""liste=[1,2,3,4,5]         # ikiside aynı işi yapar.
iterator=iter(liste)
while True:
    try:
       element=next(iterator)
       print(element)
    except StopIteration:
        break    """
"""
class MyNumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x=self.start
            self.start+=1
            return x
        else:
             raise StopIteration    

list=MyNumbers(10,20)
myiter=iter(list)    # kaç kere tekrarlarsak o kadar yazılır.
print(next(myiter))
#for x in list:
#    print(x)
"""
#PYTHON GENERATORS:bellekte yer işgal etmeyen iterator üretiyor.anında kullanıp başka zaman ihtiyacımız olmayan zaman.

"""def cube():
    for i in range(5): #5 değilde 5000 olsa bile belekte  yer kaplama yapmaz.sadece yazdırır.
        yield i**3 
generator=cube()
iterator=iter(generator)
print(next(iterator))
for i in iterator:
    print(i)
"""
#fonksiyon olamadan da yapılır.
"""liste=[i**3 for i in range(5)]# generatora dönüştürmek için köşeli parantez kaldırılır
liste=(i**3 for i in range(5))
print(liste)
#print(next(liste))
for i in range(5):
    print(i)"""

"""# datetime modülü:
import datetime
result=dir(datetime)
print(result)
"""
#JSON MODULE:json farklı diller arasında iletişimi sağlamak için geliştirilmiş
#BASİT BİR "veri formatıdır".pythondaki sözlükvelistelere çok benzer.iki tür kullanımı vardır.
#birincisi anahtar değer mantığıyla çalişir.

#dictionry:
"""import json 
person_string='{"name":"Ali","language":["python","C#"]}'
person_dict={ "name":"Ali", "language":["python","C#"] }"""
#sözlük yapısını string bir yapıya dönüştürürsek bu json yapısı olur.
####json string to Dict######
#result=json.loads(person_string)

"""with open("person.json") as f:
    data= json.load(f)
    print(data["name"])
    print(data["language"])
#result=result["name"]"""
#result=result["language"]
#result=result["lenguage"][0]
#print(type(result))

#dict to json string:
"""result=json.dumps(person_dict)
print(type(result))
print(result)"""    

"""with open("person.json","w") as f:
    json.dump(person_dict,f)
    """

"""person_dict=json.loads(person_string)
result=json.dumps(person_dict,indent=4,sort_keys=True)
print(person_dict)
print(result)"""


#uygulama JSON:"""
"""import json
import os
class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email
      
class UserRepository:
    def __init__(self):
        self.users=[]
        self.isloggedin=False
        self.currentUser={}
        #load users from. json file
        self.loadUsers()
    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json','r',encoding='utf-8') as file:
                users=json.load(file)
                for user in users:
                    user=json.loads(user)
                    newUser=User(username=user['username'],password=user['password'],email=user['email'])
                    self.users.append(newUser) 
            print(self.users)        
                           
         
    def register(self,user:User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı oluşturuldu")
       
    def login(self,username,password):
        if self.isloggedin:
            print('zaten login')
            
        else:
            for user in self.users:
                if user.username==username and user.password==password:
                    self.isloggedin=True
                    self.currentUser=user
                    print('login yapıldı')
                    break 
        
            
    def logout(self):
        self.isloggedin=False
        self.currentUser={}
        print('çikiş yapıldı')
      
    def identity(self):
        if self.isloggedin:
            print(f'username:{self.currentUser.username}')
        else:
            print('giriş yapılamadı')    
        
        
    def savetoFile(self):
        list=[]
        
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open('users.json','w') as file:
            json.dump(list,file)
            
            
repository=UserRepository()
             
while True:
    print(" Menü ".center(50,'*'))
    secim=input("1- Register\n2- Login\n3- Logout\n4- İdentity\n5-Exit\n seçiminiz:" )      
    if secim==5:
        break
    else:
        if secim=='1':
           username=input('username:')
           password=input('password:')
           email=input('email:')
           
           user=User(username=username,password=password,email=email)
           repository.register(user)
           
           print(repository.users)
        elif secim=='2':
            if repository.isloggedin:
                print('zaten login oldunuz')
                
            else:
                username=input('username:')
                password=input('password:')
                repository.login(username,password)    
                
        elif secim=='3':
           repository.logout()
            
        elif secim=='4':
            repository.identity()
        else:
            print("yanliş secim:")
          """

#REQUESTS MODÜLÜ:Python'ın internetteki verilerle etkileşimini sağlayan modüllerden biri olan Requests modülü, 
# HTTP istekleri ile projeniz ve webdeki kaynak verileriniz arasında iletişim sağlar. Bu modül, Python ile beraber default olarak gelmez





 
 
 
 
 
 
 
 
 
           