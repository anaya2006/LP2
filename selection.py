arr=[]
n=int(input("Enter no of elements in array : "))
for i in range (0,n):
    m=int(input(f"Enter element {i+1} : "))
    arr.append(m)
print(arr)
print("After selection sort: ")
for i in range (0,n):
    min_ind=i
    for j in range (i+1,n):
        if (arr[min_ind]>arr[j]):
            min_ind=j
    arr[min_ind],arr[i]=arr[i],arr[min_ind]

print(arr)

"""OUTPUT
admin1@Your:~/Anaya AI(LP2)/A1 (BFS-DFS)$ python3 selection.py
Enter no of elements in array : 5
Enter element 1 : 7
Enter element 2 : 4
Enter element 3 : 9
Enter element 4 : 3
Enter element 5 : 6
[7, 4, 9, 3, 6]
After selection sort: 
[3, 4, 6, 7, 9]
admin1@Your:~/Anaya AI(LP2)/A1 (BFS-DFS)$ """
