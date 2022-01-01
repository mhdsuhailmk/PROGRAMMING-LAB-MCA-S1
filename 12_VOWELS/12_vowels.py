a=input("Enter the word:")
vowels=["a","e","i","o","u","A","E","I","O","U"]
new=[]
new=[x for x in vowels if x in a]
print(new)