#We create a funtion called "suma_local"
num3 = 0
def suma_local(num,num2):
    num3 = num + num2
    print(num3)
    return num3 #Bring back original num3 to the function so, in case we use the function again, its value is the original again.

#Main
num = int(input("Dame un número "))
num2 = int(input("Dame otro número "))

suma_local(num,num2)