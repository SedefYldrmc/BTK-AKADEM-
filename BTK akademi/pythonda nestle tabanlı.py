##nestle tabanlı çalişma :
#object oriented programing(OOP):
#class
"""class person:
 
    #class attributes
    adress='no informasion'
    
    #constructor (yapıcı metod):
    def __init__(self,name,year):#oluşturulan her obje için çaliştırılır:
        #object attributes:
        self.name=name
        self.year=year
        print("init metodu çaliştırıldı")
    # instance methods:
    def intro(self):
        print(f'Hello there I am {self.name}')
        
    def calculateAge(self):
         return 2019-self.year        
#instance(object):
p1=person(name='sedef',year=1999)
p2=person(name='sezer',year=2000)

p1.intro()
#updating:
p1.name='ahmet'
p1.adress='Ağrı'

#accesing object attributes:
print(f" name: {p1.name}, year: {p1.year},adres:{p1.adress}")
print(f" name: {p2.name}, year: {p2.year}")
print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1==p2)
print(f"adım:{p1.name} yaşim:{ p1.calculateAge()}")
print(f"adım:{p2.name} yaşim:{ p2.calculateAge()}")"""

"""class Circle:
    #Class object attribute
    pi=3.14
    
    def __init__(self, yaricap=1):
        self.yaricap=yaricap
     
    #methods:
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)
    
c1=Circle()# yarıçap =1 alacak
c2=Circle(5)
print(f'c1 :alan ={c1.alan_hesapla()} çevre={c1.cevre_hesapla()}')
print(f'c2 :alan ={c2.alan_hesapla()} çevre={c2.cevre_hesapla()}')  """ 
       
#KALITIM:(Inheritance):Miras alma: 
       
#person => name, lastname, age,eat(),run(),drink():  
#studet (person),teacher(person) person özelliklerini miras gönderiyor:

"""class person():
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        print('Person Created')
    def who_am_I(self):
        print('I am a person')
        
    def eat(self):
        print('I am eating')    
        
class student(person):
    def __init__(self,fname,lname, number):
        self.studentnumber=number
        person.__init__(self,fname,lname)
        print('Student Created')
    #override(aynı isimli bir metod temel sınıftaki metodu ezer. )    
    def who_am_I(self):
        print('I am a student')

s1=student('sedef',' sezer ',125)
p1=person('ali',' yılmaz')
print(p1.firstname +'' + p1.lastname)
print(s1.firstname +'' + s1.lastname + str(s1.studentnumber))
p1.who_am_I()
s1.who_am_I( )"""

#nesne tabanlı progralama(özel metodlar)(special metods):
"""mylist=[1,2,3]
mystring='my string'
print(len(mylist))
print(len(mystring))
print(type(mylist))
print(type(mystring))

class movie():
    def __init__(self,title,director,duraction):
        self.title=title
        self.director=director
        self.duraction=duraction
        print('movie objesi oluşturuldu.')
    def __str__(self):
        return f" {self.title} by {self.director}"
   
m=movie('film adı','yönetmen adı','film süresi')
#print(len(movie)) çalişinca hata gelir çünkü movie classı len fonksiyonuna sahip değil.
print(type(m))
print(m) """


#QUİZ  UYGULAMASI:quiz classı dışardan soru alacak 
# ve bu soruları soracak doğru cevaba  göre skor tutacak aldığı soruları alma sırasına 
# göre kullanıcıya soracak:
#QUESTİON CLASSI:

"""class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
        
    def checkanswer(self,answer):
        return self.answer==answer
        


#print(q1.checkanswer('Python'))
#print(q2.checkanswer('C#'))
#QUİZ class:
class Quiz:
    def __init__(self,question):
        self.question=question
        self.score=0
        self.questionIndex=0
    
    
    def getQuestion(self):
        return self.question[self.questionIndex] 
    
    def displayQuestion(self):
        question=self.getQuestion()
        print(f' Soru {self.questionIndex +1 } : {question.text}')
        
        for q in question.choices:
            print('-'+ q)
            
        answer=input('cevap:')
        self.guess(answer)
        self.loadQuestion()
       # print(question.checkanswer(answer))   
        self.guess(answer)
        self.loadQuestion()     
    
    def guess(self,answer):
        question=self.getQuestion()
        if question.checkanswer(answer):
            self.score +=1
        self.questionIndex += 1    
        self.displayQuestion()
    def loadQuestion(self):
        if len(self.question)==self.questionIndex +1:
            self.showscore(self)
          
        else:
            self.displayProgres()
            self.displayQuestion()    
    def showscore(self):
        print('score', self.score )   
        
    def displayProgres(self):
        totalQuestion=len(self.question)
        questionNumber=self.questionIndex +1
        
        if questionNumber >totalQuestion:
            print('Quiz bitti ')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))    
            
q1=Question(' En iyi programlama dili hangisidir?',['C#','Python','Javascript','java'],'Python')
q2=Question(' En popüler programlama dili hangisidir?',['Python','Javascript','C#','java'],'Python')
q3=Question(' En çok kazandıran  programlama dili hangisidir?',['C#','Javascript','java','Python'],'Python')        
question=[q1,q2,q3] 
quiz=Quiz(question)
question=quiz.getQuestion()
quiz.displayQuestion()


     """
     
#MODULE NEDİR?
# (Yazdığımız programlar büyüdükçe kontrol zorlaşir bu
# yüzden program kucuk modullere  ayrılır: Modülden kasıt her modulun ayrı 
# bir py  uzantılı dosya olmasıdır .Bu ayırdığımız  her parçaya  farklı görev atamaktır.
# ve bu modüller arsaında iletişim var birbirleri arasında classları kullanabiliyor Bunlara başka bir deyişle kütüphane de deniliyor.)
#1-kendi hazırladığımız modüller 
#2-hazır modüller
#  a-standart kütüphane modüller
#  b-3. şahıs modülleri  (kütüphanee havuzu: pypi.org):
#     > pip install package -name: instal etme:
# hazır kullanımı nasıl olur:hazır standart modül kulllanırken
#kendimizde oluşturbiliriz:
#YÖNTEM 1
"""import math
value=dir(math)
value=help(math.factorial)
value=math.sqrt(49)
print(value)"""
"""import math as islem #kütüphane ye kendi taktığımız isimleri  takabiliriz:

value=islem.factorial(5)
print(value)"""
#YÖNTEM 2
"""from math import*
value=factorial(5)
value=sqrt(9)

from math import factorial,sqrt
value=factorial(5)
value=sqrt(9)        #aynı şeyleri yaparız:
print(value)

#random module:
import random 

#result=dir(random)
#result=help(random)
result=random.random() #0.0 -1.0
result=random.random()*100
result=int(random.uniform(10,100))
result=random.randint(1,100)
names=['ali','yağmur','deniz','cenk','ahmet','efe']
#result=names[random.randint(0,len(names)-1)]
result=random.choice(names)
print(result)
greeting='HELLO THERE' 
result=random.choice(greeting)
liste=list(range(10))
random.shuffle(liste)
result=liste
liste=range(100)
result=random.sample(liste,3)    
print(result)     
     """
#KENDİMİZ MODÜL HAZIRLAMA: 
#devanı artık mod ve mein dosyalarında:
     
     