import bisect


    

def main():
    N = [3,4,4,4,6,7,7,8]
    print(bisect.bisect_left(N,6))
    print(bisect.bisect_left(N,10))
    print(bisect.bisect_left(N,4))
    print(bisect.bisect_right(N,4))

    
    
    
if __name__ == "__main__":
    main()
