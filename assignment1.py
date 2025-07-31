print('Enter two numbers')
number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
number1= int(number1)
number2= int(number2)

print('What operation do you want to perform?')
print('Choisissez la lettre correspondante à une operation'),

opération = { 1: 'Addition', 2: 'Soustraction', 3:'Multiplication', 4:'Division' }
print(opération)
choix = input('Enter your choice: ')

choix=int(choix)

if choix==1:
    print(number1+number2)
elif choix==2:
    print(number1-number2)
elif choix==3:
    print(number1*number2)
elif choix==4:
    print(number1/number2)
else:
    print("Invalid option")