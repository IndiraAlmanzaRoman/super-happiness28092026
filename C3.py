nums = ["Uno", "Dos","Tres","Cuatro","Cinco","Seis","Siete","Ocho","Nueve","Diez"]
colors = ["Blue","Red","Purple","Pink","Brown","Green","Black","White","Yellow","Orange"]
new_colors = []

#colors.append("Gray")
#colors.extend(["Violet","Gray"])      
#colors.insert(0, "Violet")
#extend es un metodo iterable, se puede usar en un for
#colors.clear()
#print (colors.pop(0))
#colors.append("Violet")
#colors.sort(reverse = False)
#colors.reverse()
colors_1 = colors.copy()
nums_1 = nums.copy()
print (colors_1)




"""for num in nums:
    out = f"[{num}, {colors[nums.index(num)]}]"
    print (out)
"""
#print([nums[0], colors[0]])
#print(colors_1)
"""
for num in nums:
    out = [num, colors[nums.index(num)]]
    new_colors.append(out)

new_colors.reverse()
print (new_colors)"""




