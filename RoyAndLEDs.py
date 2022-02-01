# Problem
# Its Diwali time and there are LED series lights everywhere. Little Roy got curious about how LED lights work.
# He noticed that in one single LED Bulb there are 3 LED lights, namely Red, Green and Blue.
# State of the bulb at any moment is the sum of Red, Green and Blue LED light.
# Bulb works as follows:
# enter image description here
# Roy took out all the LEDs and found that Red LED stays ON for R seconds, Green LED stays ON for G seconds and Blue LED stays ON for B seconds. Similarly they stay OFF for same respective R, G, B number of seconds. 
# (Initially all the LEDs are OFF. See Sample Test Case Explanation for better understanding)
# Roy has one query for you, given the total number of seconds T, find the number of seconds Red, Green, Blue, Yellow, Cyan, Magenta, White, Black(no light) lights are visible.

# Input:
# One line containing space separated integers T, R, G, B
# Output:
# One line containing 8 space separated integers indicating the number of seconds Red, Green, Blue, Yellow, Cyan, Magenta, White, Black (no light) lights are visible. (See Sample I/O for clarification)

# Sample Test Case Explanation:

# enter image description here

# Sample Input
# 12 2 3 5
# Sample Output
# 1 1 1 3 2 2 0 2

# Explanation
# As shown in the image above, we have 0 to , a total of  seconds. State of Bulb for each second is also shown. 
# Red, Blue and Green occur for 1 second; Yellow occur for 3 seconds; Cyan, Magenta and Black occur for 2 seconds and White does not occur at all. 




x=input()
t,r,g,b=x.split()
t=int(t)
r=int(r)
g=int(g)
b=int(b)
rlist=[]
blist=[]
glist=[]
for i in range(0,t):
    rlist.append(0)
    glist.append(0)
    blist.append(0)
for i in range(r,t,2*r):
   
    for j in range(i,i+r):
      if j<t:
        rlist[j]=1
      else:
        break
    
for i in range(g,t,2*g):
   
    for j in range(i,i+g):
       if j<t:
        glist[j]=3
       else:
        break
    
for i in range(b,t,2*b):
    for j in range(i,i+b):
      if j<t:
        blist[j]=5
      else:
        break


for l in range(0,t):
    summ=0
    summ=rlist[l]+glist[l]+blist[l]
    rlist[l]=summ

cl=[]
for i in range(0,8):
    cl.append(0)
for m in range(0,t):
    if rlist[m]==1:
        cl[0]=cl[0]+1
    elif rlist[m]==3:
        cl[1]=cl[1]+1
    elif rlist[m]==5:
        cl[2]=cl[2]+1
    elif rlist[m]==4:
        cl[3]=cl[3]+1
    elif rlist[m]==8:
        cl[4]+=1
    elif rlist[m]==6:
        cl[5]+=1
    elif rlist[m]==9:
        cl[6]+=1
    elif rlist[m]==0:
        cl[7]+=1

cl=map(str,cl)
yy=" ".join(cl)
print(yy)

