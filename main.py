alph=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
newsentance=""
userimp = input("Enter a sentance: ")
shift = int(input("Enter a shift: "))
for each in userimp:
  if each in alph:
    newlet=alph[alph.index(each)+shift]
    newsentance += newlet
print(newsentance)
