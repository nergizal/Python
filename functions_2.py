# Döngüler- Loops
students = ["John", "Mark", "Venessa", "Mariam"]

students[0]
students[1]
students[2]

for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)

for salary in salaries:
    print(int(salary * 20 / 100 + salary))


def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)


new_salary(1500, 10)
new_salary(2000, 20)

# Uygulama - Mülakat sorusu

# amaç: aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz
# before: "hi my nameis john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

range(len("miuul"))
range(0, 5)

for i in range(len("miuul")):
    print(i)


def alternating(string):
    new_string = ""
    #girilen string'in indexlerinde gez
    for string_index in range(len("string")):
        #index çift ise büyük harfe çevir
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        #index tek ise küçük harfe çevir
        else:
            new_string += string[string_index].lower()
        print(new_string)


# Enumerate: Otomatik Counter/Indexer ile for loop

students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

#for index, student in enumerate(students):
    #if index % 2 == 0:
    #    A.append(student)
    #else:
    #    B.append(student)
   # print(index, student)


#Uygulama- Mülakat Sorusu
# divide_students fonksiyonu yazınız.
# çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri başka bir listeye alnız.
# Fakat bu iki liste tek bir liste olarak return olsun.

students=["John", "Mark", "Venessa", "Mariam"]

def divide_students(students):
    groups=[[],[]]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups
st= divide_students(students)
st[0]
st[1]



#Alternating fonksiyonunun enumerate ile yazılması

def alternating_with_enumerate(string):
    new_string=""
    #hem kendisinde hem indexinde gezmemiz gerekiyor.
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating_with_enumerate("hi my name is john and ı am learning python")


#Zip
students = ["John", "Mark", "Venessa", "Mariam"]

departments = ["A", "B", "C", "D"]

ages=[23,30,26,22]

list(zip(students, departments, ages))


# lambda, map, filter, reduce

def summer(a, b):
    return a + b
summer(2, 3) * 9

new_sum =lambda a, b: a + b
new_sum(4, 5)
