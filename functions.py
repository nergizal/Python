# Fonksiyon Okuryazarlığı

print("a")
# Parametre fonksiyon tanımlanması esnasında ifade edilen değişkenlerdir.
# Argüman ise bu fonksiyonlar çağırıldığında parametre değerlerine karşılık girilen değerlerdir.
# Kullandığımız fonksiyonlar içinde argümanlar bulunur ve bunlar fonksiyonun genel amacını biçimlendirmek için kullanılır.


print("a", "b")
print("a", "b", sep="__")


# Fonksiyon Tanımlama
def calculate(x):
    print(x * 2)
calculate(5)

# İki argümanlı/parametreli bir fonksiyon tanımlayalım.

def summer(arg1, arg2): # sırası önemli
    print(arg1+arg2)
summer(7, 8)

#Docstring
def summer(arg1, arg2):
    """
    Sum of two numbers

    Args:
        arg1:int,float
        arg2: int,float
    Returns:
        int, float
    Examples:

    Notes:
    """
    print(arg1+arg2)

# Fonksiyonların Statement Bölümü
# def function_name(parameters/arguments): -bir fonksiyon parametresiz,argümansız da olabilir.
#   statements (function body)

def say_hi():
    print("Merhaba")
    print("Hi")
    print("Hello")
say_hi()


def multiplication(a,b):
    c= a * b
    print(c)
multiplication(10,9)


# girilen değerleri bir listeiçinde saklayacak fonksiyon

list_store= [] #global etki alanıda
# kullandığımız bazı metotlar yeniden atama işlemine gerek duymadan ilgili veri yapısında kalıcı bir değişiklik yapablir.
# örn: append metodu.
def add_element(a,b): #ilk olarak bir fonksiyon tanımladık
    c = a * b #fonksiyon içerisinde bir matematiksel işlem gerçekleştirdik.
    list_store.append(c) #liste yapısına bir eleman eklemek için metot kullandık
    print(list_store) #liste ekrana yazdırıldı.
add_element(1,8)
add_element(18,8)


# Ön tanınlı argümanlar (Default Parameters)

def divide(a,b):
    print(a/b)
divide(2,3)


def divide(a,b=1):
    print(a/b)
divide(1)


# Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak

def calculate(varm, moisture, charge):
    return  (varm+ moisture)/charge

calculate(98, 12, 78) * 10


