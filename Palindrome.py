def Palindromel(string):
    if len(string)==0:
        return True
    if string[0]!=string[len(string)-1]:
        return False
    return Palindromel(string[1:-1])
print(Palindromel("racecar"))