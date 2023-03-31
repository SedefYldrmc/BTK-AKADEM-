#error:

#error handling=> hata yönetimi:
#int(1ö2)=> value error
# print(s)=> NameError
#print(10/0)=>ZeroDivisionError
#print('denem'e)=>SyntaxError

#HATA YÖNETİMİ( Error handling):hata gelebilecek yerleri try bloğuna almak.
"""
try:
    x=int(input("x: "))
    y=int(input("y: "))
    print(x/y)          # bu şekilde gelebilecek olası hatalar için yönlendirme yapılır.
except ZeroDivisionError:
    print("y için 0 girilemez.")  
except ValueError:
    print("X ve Y için sayisal deger giriniz.")  """
    
    
"""try:
    x=int(input("x: ")) # daha mantıklı şekli
    y=int(input("y: "))
    print(x/y)          # bu şekilde gelebilecek olası hatalar için yönlendirme yapılır.
except (ZeroDivisionError, ValueError) as e:
    print("yanliş bilgi girdiniz.")
    print(e)"""
"""
while True:
    try:
       x=int(input("x: ")) 
       y=int(input("y: "))
       print(x/y)        
    except (ZeroDivisionError, ValueError,SyntaxError) as e:
        print("yanliş bilgi girdiniz.")
        print(e) 
    else:
        break  
    finally:
        print('try except sonlandı')"""
        
# Hata nesnesi oluşturma:
"""x=10
if x>5:
    raise Exception(" x ,5 `ten büyük değer alamaz.")
        """
"""def check_password(psw):
    import re
    if len(psw)< 8:
        raise Exception("parola en az 7 karakter olmalıdır.")
    elif not re.search("[a-z]", psw):
        raise Exception("parola küçük harf içermelidir.")
    elif not re.search("[A-Z]", psw):
        raise Exception("parola buyuk harf içermelidir.")
    elif not re.search("[0-9]", psw):
        raise Exception("parola rakam içermelidir.")
    elif not re.search("[_&$]", psw):
        raise Exception("parola alpha numerik karakter  içermelidir.")    
    elif re.search("\s", psw):
        raise Exception("parola boşluk içermemelidir.")
    else:
        print("Geçerli parola")
password="159199Se!&"

try:
    check_password(password)
except Exception as e:
    print(e)
else:
    print("Geçerli parola.")       
finally:
    print("validation tamamlandı")    
          """
"""class Person:
    def __init__(self,name,year):
        if len(name) >10:
            raise Exception("name alanı fazla karakter içeriyor.")
        else:
            self.name=name

p=Person("aliiiiiii",159)            
        """
        
# UYGULAMA:
#liste=["1","2","5a","10b","abc","10","50"]
#1: Liste elemanları içindeki sayısal değeri bulunuz:
"""for i in liste:
    try:
        result=int(i)
        print(result,end=" ")
    except ValueError:
        continue 
      """
#2:Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı
#olduğundan emin olunuz aksi halde hata mesajı yazın.

"""while True:
    sayi=input("sayi:")
    if  sayi=="q" :
        break
    try:
       result=float(sayi)
       print("Girdiğiniz sayı",result)
    except ValueError:
        print("HATALI DEĞER GİRDİNİZ:") 
        continue
        """

#3:Girilen parola içinde türkçe karakter hatası veriniz.

"""def checkPassword(parola):
    turkce_karakterler="şğıüçöİ"
    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola türkçe karakter içeremez")
        else:
            pass
    print("geçerli parola")

parola=input('parola giriniz:')
   
try:
    checkPassword(parola)
except TypeError as e:
    print(e)            
"""

#4:Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin:
        
"""def factoriyel(x):
    x=int(x)
    
    if x < 0:
        raise ValueError("Negatif deger içeremez.")
    result=1
    
    for i in range(1,x+1):
        result*=i
    print(result)
for x in [5,3,10,-3,"10"]: 
    try:    
        y=factoriyel(x) 
    except ValueError as e:
        print(e)
factoriyel(y)                 
"""

#DOsya açmak ve oluşturmak için open() fonksiyonu kullanılır.
#Kullanımı:open(dosya_adı,dosya_erişme_modu) 
#dosyaya erişme modu => dossyayı hangi amaçla açtığinizi belirtir.

#"w":(Write) yazma modu.
#     **Dosyayı konumda oluşturur.
#     **Dosya içeriğini siler ve yeniden ekleme yapar.
#file=open("newfile.txt","w")
#file=open("C:/users/asily/Desktop/BTK akademi/newfile.txt","w")
#file.close()

"""file=open("newfile.txt","w",encoding='utf-8')
file.write("Sadık turan")
file.close()
print(file)"""
#"a":(append) ekleme.Dosya konumunda yoksa oluşturur.
"""file=open("newfile.txt","a",encoding='utf-8')
file.write("\nÇınar turan")
file.write("Çınar turan\n") #yazan bilgiden sonra kursor bir altta iner.
file.close()"""
#"x":(create) oluşturma.Dosya zzaten varsa hata verir.
"""file=open("newfile2.txt","x",encoding='utf-8')"""
#"r":(read) okuma .varsayılan.Dosya konumunda yoksa hata verir.         
# try:
#     file=open("newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print('Dosya okuma hatası.')
# finally: 
#     print("dosya kapandı")
#     file.close()
file=open("newfile.txt","r",encoding='utf-8')

# #for döngüsü:

# for i in file:
#     print(i, end='')
# file.close()

#yol 2=> read() fonksiyonu:
"""content=file.read()
print(content)"""
#kürsor okumada en sona geldiğinde tekrar okku komutu gelirse 
#imlecın kaldığı yerden okumaya devam eder eğer içerik kalmamışasa
#boş döner.
"""content1=file.read()
print("içerik 1")
print(content1)

content2=file.read()
print("içerik 2")
print(content2)"""

"""content=file.read(5)
content=file.read(3)
content=file.read(3)
print(content)"""

#****** readline()fonksiyonu(her seferinde birer satır okur)
"""print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
file.close()"""
#****** readlines()fonksiyonu: her satırı dizi elemanı(liste elemanı) olarak alır
"""liste=file.readlines()
print(liste)
file.close()"""


#pythonda dosya okuma fonksiyonları:

"""with open("newfile.txt","r",encoding='utf-8') as file:
    content=file.read(10)
    print(content) # burda close a gerek yok çünkü blok sonlanınca ototmatık olarak kapanır 
    file.seek(10 )
    print(file.tell())
    content2=file.read()
    print(content2)"""
    # pythonda dosyadaa güncelleme yapma:
"""with open("newfile.txt","r+",encoding='utf-8') as file:
   file.seek(20)    
   file.write("deneme")        
    
with open("newfile.txt","r+",encoding='utf-8') as file:   
    print(file.read()) 
    """

"""with open("newfile.txt","a",encoding='utf-8') as file:   
   file.write("\nEmel turan")        

#*****Sayfa sonunda güncelleme:******   
with open("newfile.txt","r+",encoding='utf-8') as file:   
    print(file.read())    """
def ortalamalari_oku():
    pass
def NotGir():
    ad=input("öğrenci adı:")
    soyad=input("öğrenci soyadı:")
    not1=int(input("not 1 :"))
    not2=int(input("not 2:"))
    not3=int(input("not 3:"))
    
    with open("sınav_notları.txt","a",encoding='utf-8') as file:
        pass
    
    
    
    
def Notları_kaydet():
    pass

    
#uygulama dosya yönetimi: 
while True:
    islem=input("1-Notları Oku\n2-Not Gir\n3-Nor Kayıt ")
    if islem=="1":
        ortalamalari_oku()
    elif islem=="2":
        NotGir()
    elif islem=="3":
        Notları_kaydet()
    else:
        break             
           