# import random
# # exercice 1, les mutliples de 3 et 5 additionés

# count = 0
# multiples = []
# for i in range(1000):
#     if i % 3 == 0 or i % 5 == 0:
#         count += i
# # print(count)
        
# # # réponse = 233168

# # # exercide 2, suite de Fibonacci

# i = 1
# j = 2
# count2 = 0
# while i and j < 4000000:
#     if i % 2 == 0:
#         count2 += i 
#     if j % 2 == 0:
#         count2 += j
#     i+=j
#     j+=i
# print(count2)
    
# # # réponse = 4613732

# # # exercice 3, plus grand facteurs premier de 600851475143 (100 premiers nombres premiers : 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, et 97.)

# probleme = 600851475143
# nombres_premiers = []
# facteurs_premiers = []

# def is_prime(n):
#   for i in range(2,n):
#     if (n%i) == 0:
#       return False
#   return True

# for i in range(2, 10000):
#     if is_prime(i):
#        nombres_premiers.append(i)

# for i in nombres_premiers:
#     if probleme % i == 0:
#         probleme = probleme / i
#         facteurs_premiers.append(i)
# #print(facteurs_premiers)

# # # réponse = 6857

# # # exercice 4, Trouve le plus grand palindrome créé par le produit de deux nombres à 3 chiffres. 



# # # exercice 5, le plus petit nombre qui peut être divisé par tous les nombres de 1 à 20, sans qu'il n'y aucun reste? 

# for i in range(100000000000):
#    if i % 1 == 0 and i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0 and i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and i % 9 == 0 and i % 10 == 0 and i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0 :
# #      print(i)
#       break

# # # réponse = 232792560
   
# # # exercice 6, trouve la différence entre la somme des carrés des 100 premiers nombres naturels et le carré de la somme de ces nombres.

# temp = 0
# temp2 = 0
# count6 = 0
# SecCount6 = 0
# resultat = 0

# for i in range(101):
#     temp = i * i 
#     count6 += temp


# for i in range(101):
#    temp2 += i
#    SecCount6 = temp2 * temp2


# resultat = SecCount6 - count6
# # #print(resultat)

# # # réponse = 25164150

# # # exercice 7, quel est le 10001eme nombre premmier 

# table_nbPremiers = []
# i = 2

# while len(table_nbPremiers) < 10001:
#     if is_prime(i):
#         table_nbPremiers.append(i)
#     i += 1
# #print(table_nbPremiers)

# # # réponse = 104743 

# # # # Exercice 8, Trouve les 13 chiffres adjacents dans ce nombre à 1000 chiffres qui donnent le plus grand produit:

# calcul = 0
# memoire = 0
# string = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
# table8 = ([*string])
# taille = len(table8)
# for i in range(taille):
#     table8[i] = int(table8[i])
# #print(table8)
# for i in range(taille-13):
#     calcul = table8[i] * table8[i+1] * table8[i+2] * table8[i+3] * table8[i+4] * table8[i+5]* table8[i+6]* table8[i+7]* table8[i+8]* table8[i+9]* table8[i+10]* table8[i+11]* table8[i+12]
#     if calcul > memoire:
#         memoire = calcul
# # #print(memoire)

# # # réponse = 23514624000

# # # Exercice 9, produit de a x b x c


# a = 0
# b = 1
# c = 2
# for a in range(500):
#     for b in range(500):
#         for c in range(500):
#             if a*a + b*b == c*c and a + b + c == 1000:
# #  print(a * b * c)
# # réponse = 31875000
                
# #Exercice 10, somme des nombres premiers jusqu'à 2M
# count9 = 0
# for i in range(2, 2000000):
#     if is_prime(i):
#         count9 += i
# # print(count9)
# # réponse = 142913828922
