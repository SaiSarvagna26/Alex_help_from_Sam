A=list(map(int,input().split()))
new=[]
tens_digi=A[ :-2]
ones_digi=A[-1]
new+=[tens_digi]+list([ones_digi])
print(new)