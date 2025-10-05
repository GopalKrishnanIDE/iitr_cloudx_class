def binary_search(a,b):#this will work only in sorted.
    #print(f"a:{a}, b:{b}")
    #a_=sorted(a) # it will consume lot of computational space. as it goes through the entire list.
    a_=a
    #print(f"a_ is {a_}")
    start=0
    end=len(a)-1
    
    if(end==-1):
     #   print("List is empty")
        return False
    
    while True:
        #print("-----------")
        mid=((start+end)//2)
        #print(f"start: {start},end: {end},mid: {mid}")
        #print(f"-->a_[mid]: {a_[mid]}")
        old_mid=mid
        #print(f"old_mid: {old_mid}")
        if(a_[mid]==b):
            
         #   print(f"found the match")
            return True
        elif (a_[mid]>b):
            
            end=mid-1
            
          #  print(f"a[mid]:{a_[mid]} is greater than b:{b}")
            
        elif (a_[mid]<b):
            start=mid+1
           # print(f"a[mid]:{a_[mid]} is less than b:{b}")
           
        if(old_mid==(start+end)//2):
            #print(f"found nothing")
            return False
        