#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# insert into dictionary and print "Inserted"
def insert_dict(key, value, Dict):
    #code here
    Dict[key]=value
    print ("Inserted")
    
    

# deleting from dictionary and print "Deleted" if key present else "-1"
def del_dict(key, Dict):
    #code here
    del Dict[key]
    print("Deleted")
    

# print marks of student whos name is key if student name is present in Dict else "-1"
def print_dict(key, dict):
    if key in dict:
        print (f"Marks of geeks is {dict[key]}")
    else:
        print(-1)
    # Your code here
    
    
    

#{ 
 # Driver Code Starts.
# Driver code
def main():
    for _ in range(int(input())):

        Q = int(input())

        Dict = {}
        for i in range(Q):
            query = input().split()
            if(query[0] == 'i'):
                insert_dict(query[1], query[2], Dict)
                
            elif(query[0] == 'd'):
                del_dict(query[1], Dict)
                    
            else:
                print_dict(query[1], Dict) 


if __name__ == '__main__':
    main()
# } Driver Code Ends

# i dhi 100
# i ankit 200
# i harsh 300
# d harsh
# p harsh