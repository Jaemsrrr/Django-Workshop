from django.shortcuts import render
import math
 

# Create your views here.
def home(request):
    n1=5
    
    result=square(n1)
   
    temp=evenodd()
    x=temp[0]
    y=temp[1]
    
    res=tables(3,20)
    print(res)
    return render(request,'app1/index.html',{'param1':result,'param2':x,'param3':y,'param4':res})

def square(n1):
    return n1*n1



def evenodd():
    list=[]
    list2=[]
    for i in range (1,10,2):
            list.append(i) 
            list2.append(i+1)
    
    return (list,list2)

def tables(start, end):
    list1 = []
    for j in range(start, end + 1):
        list2 = []
        for i in range(1, 11):  
            str1 = f"{j} X {i} = {j * i}"
            list2.append(str1)
        list1.append(list2)
    return list1
    
        
