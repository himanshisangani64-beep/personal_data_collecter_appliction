print(" Welcome To The Interactive  Personal Data Collector !")
print("-"*60)

# User Collect Data :

name = input("Enter Your Name:")
age = int(input("Enter Your Age:"))
city = input("Enter Your City:")
height = float(input("Enter Your Height [Meters]:"))
num = int(input("Enter Your Favourite Number:"))
print("\nYour Data Are Collected Successfully....")

#  Data Processing

birth_year = 2026-age

# Display Data

print("-"*60)
print("   Show Information   ")
print("-"*60)
print("Name                        :",name,type(name),"Memory Address:",id(name),sep="  ")
print("Age                         :",age,type(age),"  Memory Address:",id(age),sep="  ")
print("City                        :",city,type(city),"Memory Address:",id(city),sep="  ")
print("height                      :",height,type(height),"Memory Address:",id(height),sep="  ")
print("Favourite Number            :",num,type(num),"Memory Address:",id(num),sep="  ")

# Eixt Message

print("-"*60)
print("Your Birth year [approximately]  :",birth_year,"Base On Year of Age",age)
print("\n Thank You! for use Personal Data Collector Goodbye... \n ")





