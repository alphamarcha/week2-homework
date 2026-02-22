#Mainīgie str, int, float, bool, None
#STR
name = str('Marks')             #Piešķiru string vērtību
print(name)

lastname = str('Kirillovs')     #<class 'type'>
print(type(str))

print(name, lastname)           #str vērtības viena līnija

#INT
x = int(26.150)                 #Piešķiru int vērtību
print(x)
print(type(x))                  #<class 'int'>

a =int(20.7)                    #Rada veselu skaitli (20)
print(a)

y = [1,2,3]
print(type(y))                  #<class 'list'>

#FLOAT
c = float('30.200')             #float mainīga saīsina skaitli pēc ,0 (30.2)
print(c)

z = float('31.270')             #float mainīga saīsina skaitli pēc ,0 (31.27)
print(z)

#BOOL
print(20>17)                    #True     20 ir lielāks par 17
print(20<17)                    #False    17 nav lielāks par 20
print(bool('Hello World!'))     #True     pareizi uzraksīts kods
print(bool(''))                 #False    ne pareizi uzrakstīts kods (iekavas nevar būt tukšas)
print(bool(0))                  #False    kad ir nulle tad ir FALSE.

#EXPLICIT CONVERSION
print(int("fortuna"))           #Ne strādās, jo int strādā tikai ar skaitliem.
print(int(24))                  #24

print(float('30,20'))           #Ne strādās, jo vajag būt punktam, ne bet komatam.
print(float(30.20))             #30.2

print(bool(''))                 #False, tukšas iekavas
print(bool('hello'))            #Hello