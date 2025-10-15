s=input("Enter a String:")
ch=s[0]
new_s=ch+s[1:].replace(ch,'$')
print("Result:",new_s)
