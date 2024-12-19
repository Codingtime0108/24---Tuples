def palind(r):
    a = len(r)-1
    b = 0
    while (b<a):
        if(r[b]!=r[a]):
              return False
        b+=1
        a-=1
    return True
r = (1,2,3,3,2,1)
if(palind(r)):
     print("The Tuple is Flip Flop:)")
else:
     print("The Tuple isn't Flip Flop!!!!")