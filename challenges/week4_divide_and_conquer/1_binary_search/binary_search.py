#python3
def binary_search(keys, query):
    

    # write your code here
    start = 0
    end = len(keys)-1
    
    
    
    while start <= end :
        
        middle = start +(end - start) //2
        
    
        if (query < keys[middle]):
            end = middle-1
        elif (query > keys[middle] ):
            start = middle+1
        
        elif(query == keys[middle] ):   
            return  middle       
    return -1

    


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
     
        print(binary_search(input_keys, q), end=' ')

