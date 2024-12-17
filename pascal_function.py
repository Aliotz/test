
'''creted by our'''

def pascal(n):
    t = [1]
    y = [0]
    for _ in range(n):
        print(t)
        t =[i+j  for i,j in zip(t+y , y+t)]

row = int(input('please enter the pascal row you want:'))
pascal(row)
