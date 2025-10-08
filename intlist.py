nums = input ("Enter integers seperated by spaces : " ).split()
result = []

for n in nums:
    value = int(n)
    if value > 100: 
       result.append("Over")
    else:
       result.append(value)

print("Modfied Lists : ",result)
