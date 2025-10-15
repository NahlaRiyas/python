color_list1=input("Enter first color list(comma seperated):").split(",")
color_list2=input("enter second color list(comma seprated):").split(",")
color_list1=[c.strip() for c in color_list1]
color_list2=[c.strip() for c in color_list2]
result=[color for color in color_list1 if color not in color_list2]
print("colors in list 1 is not in list 2:",result)
