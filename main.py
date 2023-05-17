import random

list1=[]

for i in range(5):
    num1 = random.randrange(21)
    input('enter no. ')
    list1.append(num1)
print(list1)
p = sum(list1)
print(p)
# coomment to check the post and pull using jrnkins
list2=[]
# changes
for i in range(5):
    num2 = random.randrange(21)
    input('enter no. ')
    list2.append(num2)

print(list2)
c = sum(list2)

print(c)

if p > c:

    print('player 1 is winner')
else:
#this is test the pipeline
    print('player 2 is winnear')
