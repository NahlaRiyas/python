numbers=list(map(int,input("enter integers seperated byn space:").split()))
odd_numbers=[num for num in numbers if num%2!=0]
print("List after removing even number:",odd_numbers)
