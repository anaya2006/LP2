import sys
arr=[]
def selection(n):
   for i in range (0,n):
       m=int(input(f"element {i+1} : "))
       arr.append(m)
   print("unsorted arr ",arr)
   for i in range (0,n):
      min_ind=i
      for j in range (i+1,n):
          if arr[j]<arr[min_ind]:
              min_ind=j
      arr[i],arr[min_ind]= arr[min_ind], arr[i]
   print("sorted ",arr)
 
#selection(5)
labels=['A', 'B', 'C', 'D', 'E']          
graph= [  [0,3,2,0,0],
          [3,0,5,4,5],
          [2,5,0,0,3],
          [0,4,0,0,1],
          [0,5,3,1,0]
       ]         

def prims(graph, V, labels):
    selected=[False]*V
    selected[0]=True
    wt=0
    edges=0
    while edges<V-1:
        min=sys.maxsize
        x=0
        y=0
        for i in range (V):
           if selected[i]:
             for j in range (V):
                if not selected[j] and graph[i][j]!=0:
                     if min>graph[i][j]:
                        min=graph[i][j]
                        x=i
                        y=j
        print (f"{labels[x]}-{labels[y]} : {graph[x][y]}")
        selected[y]=True
        wt+=graph[x][y]
        edges+=1
    print("total cost of mst: ", wt)



def main ():
   int ch=3
   while ch!=0:
       ch=int(input("Select option : "))
       print("GREEDY ALGORITHM")
       print("1. Selection Sort \n2. Prims Algorithm \n0.Quit")
       if ch==1:
           n=int(input("array elements you want? :"))
           selection(n)
      
       elif ch==2:
           prims(graph,5,labels)
       else:
          print("?")           
    
main()