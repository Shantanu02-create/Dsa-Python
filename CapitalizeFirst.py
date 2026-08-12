def Capitalize(arr):
    if len(arr)==0:
        return []
    result=[]
    result.append(arr[0][0].upper()+arr[0][1:])
    return result+Capitalize(arr[1:])
print(Capitalize(['hello','world','python']))
