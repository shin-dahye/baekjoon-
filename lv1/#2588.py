a = int(input())
b = int(input())

print(a * (b%10))
print(a * ((b%100)//10))
print(a * (b//100))
print(a * b)

#print 여러번 쓰지 않기

print(a*(b%10),a*((b%100)//10),a*(b//100),a*b,sep='\n')

#range 사용해서 역순으로

num1 = int(input())
num2 = input()

for i in range(len(num2), 0, -1):
    print(num1 * int(num2[i-1]))
print(num1 * int(num2))
