a=int(input("Quel est votre age? "))
t=int(input("Quel votre taille? "))
x=input("Quel est ton sexe? Si femme enter 1, si homme enter 2: ")
if x==1 :
    p=0.8*(t-100+(a/10))
else :
    p=0.9*(t-100+(a/10))
print("votre masse est",p,"kg")
