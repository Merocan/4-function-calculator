def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  return a/b
  
print("İşleminizi Seçiniz")
print("1.Ekleme")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")

choice = input("Seçiminizi yapınız:(1/2/3/4):")
num1 = int(input("İlk değeri giriniz: "))
num2 = int(input("İkinci değeri girizin:"))

if choice == '1':
  print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
  print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
  print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
  print(num1,"/",num2,"=", divide(num1,num2))
else:
  print("Invalid input")
