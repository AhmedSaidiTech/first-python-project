secret_number = 7 

devined_number = int ( input ( "Devinez le nombre secret \n"))

while devined_number != secret_number :
    devined_number = int ( input ( "Devinez le nombre secret \n"))
    if devined_number < secret_number :
        print ("le nombre est plus grand")
    elif devined_number > secret_number :
        print ("le nombre est plus petit")
if devined_number == secret_number :
    print ("Bravo ! ")    
    


number = int ( input ( "Tapez un nombre \n")) 

sum = 0 

fact = 1 

nb_div= 2

for i in range (1 , number +1 ):
    sum += i 
    fact*= i


print (f"Résultat somme : {sum} ") 
print (f"Résultat factoriel : {fact} \n") 

print ("-----------------------------table de multiplication :------------------------------------------------------------- \n")
for i in range(1,11):
    print(f"{number}* {i} = {number*i}\n")

for i in range (2 , (number // 2) + 1 ) :
    if number % i == 0 :
        nb_div += 1
        print (f"le nombre {number}  n'est pas premier car il est divisible aussi par {i}")
        break 

if nb_div == 2 :
    print (f"le nombre {number} est premier car il est divisible seulement par 1 et lui meme")

for i in range (1,101):
    if i % 3 == 0 and i % 5 == 0 :
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else : 
        print(i)   
       