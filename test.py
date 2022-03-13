def swap(e,a,b):
   i=e.index(a)
   j=e.index(b)
   e[i]=b
   e[j]=a
   return e
#Question-1
a=input("Enter root role name : ")
e=[a]
user={}
o=1
while(o!=0):
   o=int(input("Operation to be performed : "))
#Question-2
   if o==1:
      sr = input("Enter sub role name : ")
      r = input("Enter reporting to role name : ")
      if r in e:
         k = e.index(r)
         e.insert(k+1,sr)
#Question-3
   elif o==2:
      for i in e:
         print(i,end=' ')
#Question-4
   elif o==3:
      d=input("Enter the role to be deleted : ")
      tr=input("Enter the role to be transforrred : ")
      e=swap(e,d,tr)
      e.remove(d)
#Question-5
   elif o==4:
      au = input("Enter User Name : ")
      role = input("Enter Role : ")
      user[role]=au
   elif o==5:
      p=user
      p={v: k for k, v in p.items()}
      print(p)
