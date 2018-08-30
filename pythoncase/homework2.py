'''
冰雹：任意给定一个正整数N，如果是偶数：N/2 奇数：N*3+1
'''
N = int(input('请输入一个正整数：'))
while True:
    if N % 2 == 0:        
        N = N/2
        print(N)
        if N == 1:
            break
        else: 
            continue
    else:
        N = N * 3 + 1
        print(N)
        if N == 1:
            break
        else:
            continue
    
