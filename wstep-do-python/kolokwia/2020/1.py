

def wieza(N, D):    
    maxw = D + (N-1)*6
    for i in range(N):
        for j in range(4):
            print(("#"*(D + i*6)).center(maxw))

wieza(4, 10)