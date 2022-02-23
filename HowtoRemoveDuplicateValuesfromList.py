a = [1,2,3,1,3,4,6,1]

# solution 1 using set()

uniqueList = list(set(a))


# Solution 2.1 create a temp list to store unique values
def removeDuplictese(a):
    try:
        temp=[]
        for item in a:
            if item not in temp:
                temp.append(item)
    except:
        pass
    else:
        return temp

# Solution 2.2 using list comprehension

listComprehension =[]
[listComprehension.append(x) for x in a if x not in listComprehension]



print(uniqueList)
print(removeDuplictese(a))
print(listComprehension)