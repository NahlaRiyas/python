names = input("enter first name seperated by space:").split()
count=sum(name.lower().count('a') for name in names)
print("Total 'a' count:",count)

