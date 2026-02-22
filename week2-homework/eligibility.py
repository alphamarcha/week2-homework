#python eligibility.py

#vecuma pārbaude ar kļūdu
while True:
    try:
        vecums = int(input("# Ievadi vecumu: "))
        break
    except ValueError:
        print("# Kļūda: ievadi skaitli ")        #kļūdas gadījums SKAITLIS


#auto īres loģika bool un and
while True:
    aplieciba = input("# Vai ir autovadītāja apliecība? (j/n): ").lower()
    if aplieciba in ('j', 'n'):
        break
    else:
        print("# Kļūda: ievadi j vai n")         #kļūdas gadījums J vai N

ir_tiesibas = aplieciba == 'j'
ir_21_vai_vairak = vecums >= 21                     
var_iret_auto = ir_tiesibas and ir_21_vai_vairak   #a=c+b


#studenta loģika bool un and
while True:
    students = input("# Vai ir students? (j/n): ").lower()
    if students in ('j', 'n'):
        break
    else:
        print("# Kļūda: ievadi j vai n")         #kļūdas gadījums J vai N

ir_students = students == 'j'
ir_26_vai_mazak = vecums <= 26
studentu_atlaide = ir_students and ir_26_vai_mazak   #a=c+b


#veterana loģika bool un and
while True:
    veterans = input("# Vai ir veterāns? (j/n): ").lower()
    if veterans in ('j', 'n'):
        break
    else:
        print("# Kļūda: ievadi j vai n")         #kļūdas gadījums J vai N

ir_veterans = veterans == 'j'
ir_65_vai_vairak = vecums >= 65
senioru_atlaide = ir_veterans and ir_65_vai_vairak   #a=c+b


print("# ---")

#atbildes
print("# Balsošana:", "Jā ✓" if vecums >= 18 else "Nē ✗")
print("# Auto īre:", "Jā ✓" if var_iret_auto else "Nē ✗")
print("# Studentu atlaide:",  'Jā ✓' if studentu_atlaide else 'Nē ✗')
print("# Senioru atlaide:",  'Jā ✓' if senioru_atlaide else 'Nē ✗')


