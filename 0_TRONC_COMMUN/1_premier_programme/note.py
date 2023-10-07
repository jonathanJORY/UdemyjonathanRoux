import time
res = 5
for i in range(res):
    time.sleep(1)
    print(".", end="", flush=True)
print()
# renvoie: ...........


for i in range(res):
    time.sleep(1)
    print(i, end="\r")
print()
# fait un chrono de 0 à i


print("bib",res,"n") # renvoie: bib 5 n
print("bib"+res+"n") # renvoie: une erreur

print("-"*20) #  renvoie ----------------


a = print("tot")
print(a)
# renvoie tot puis None


a = 5
 
def ma_fonction():
  global a
  a = a + 1
  print(a)
 
ma_fonction()
ma_fonction()
# renvoie 6 puis 7

nom = "Jean"
print(nom[::-1])
#renvoie naeJ