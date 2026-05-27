
#1. ATM Withdrawal Feasibility Checker
n=int(input())
vr=0
ivr=0
amount=0
for i in range(n):
    num=int(input())
    if num%100==0 and num>0:
        vr+=1
        amount+=num
    else:        ivr+=1
print("valid request:",vr)
print("invalid request:",ivr)
print("total amount:",amount)
'''
'''
#2. Digital Root Without Formula
n=int(input())
s=0
while n>10:
    s=0
    while n>0:
        digit=n%10
        s+=digit
        n=n//10
    n=s
print(s)

#3. Parking Fee Collection Summary
n,k=map(int,input().split())
tc=0
ae=0
for _  in range(n):
    num=int(input())
    tc+=num
    if num>k:
        ae+=1
print("total collection:",tc)
print("above expected:",ae)

#4.Power Consumption Slab Counter
n=int(input())
low=0
noraml=0
high=0
for _ in range(n):
    num=int(input())
    if num<100:
        low+=1
    elif num>=100 and num<=300:
        noraml+=1
    else:
        high+=1
print("low",low)
print("noraml",noraml)
print("high",high)

