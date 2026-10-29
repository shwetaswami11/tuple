#t=(10,20,30,20,40)
# print(t.count(20))

# t=(1,2,3);
# print(t.index(5))

# t=(10,20,30,40,50)
# print(t[1:4])

# t=(1,2,3)+(4,5)
# print(t)

# t=(1,2)*3
# print(t)

# t=(1,2,3);
# t[0]=10

# print(len((1,2)))

# t=(1,[2,3],4);
# t[1][0]=99
# print(t)

# a,b,*c=(1,2,3,4,5)
# print(c)

# e=(1,2)<(3,4)
# print(e)

# t=(1,2,3)
# print(type(t))

# print(bool(()))

# t=(10,20,10,30,10)
# t.index(10,1)
# print(t)

# t=(1,2,3)
# del t[0]
# print(t)

# age=(18,21,25,30)
# 25 in age
# print(age)

# print(min(('apple','banana','cherry')))

# t=(1,2,3,4);
# print(t[-1])

# print((0,)*4)

# t=(10,20,30);
# print(30 in t)

# t=(1,2,3);
# print(sum(t,10))



# t=(10,20,30,40,50);
# print(t)

# a=("shweta",21,65.30,False)
# print(a)

# b=(10,)
# print(b)
# print(type(b))

# t=(10,20,30,40,50)
# print("First element:",t[0])
# print("middle element:",t[len(t)//2])
# print("last element:",t[-1])

# t=(1,2,3,4,5)
# print(t[::-1])

# t = (10, 20, 30, 40, 50, 60)
# print(t[::2])

# c=(25,13,14,25,13,25,16)
# print(c.count(25))

# a=(7,8,9,4,5,6)
# print(a.index(5))

# b=(10,20,40,80)
# total=(sum(b))
# average=total/len(b)
# print("sum:",total)
# print("average:",average)

# t=(10,150,20,25,30,35)
# even=0
# odd=0

# for i in t:
#     if i % 2==0:
#         even +=1
#     else:
#         odd +=1
# print ("even numbers:",even)
# print ("odd numbers:",odd) 

# a=(10,2,0,13,25,26,30,)
# print(min(a))
# print(max(a))

# T=(10,20,30,40,50,)
# value=30
# if value in T:
#     print("value exists in a tuple")
# else:
#     print("Not exists in a tuple")

# num = [10, 20, 30]
# t = tuple(num)
# print(num)
# print(t)

# sh=(20,40,60,80)
# a,b,c,d=sh
# print(a)
# print(b)
# print(c)
# print(d)

# a = 10
# b = 20
# a, b = b, a
# print(a)
# print(b)

# t = ((10, 20), (30, 40), (50, 60))
# print(t[1][0])

# t = (10, 20, 10, 30, 20, 40, 30)
# lst = list(t)
# lst = list(dict.fromkeys(lst))
# result = tuple(lst)
# print(result)

# t= (10, 50, 30, 50, 40, 30, 20)

# unique = sorted(set(t), reverse=True)

# if len(unique) >= 2:
#     print("Second-largest:", unique[1])
# else:
#     print("Second-largest distinct number does not exist")

# t= (50, 20, 40, 10, 30)
# result = tuple(sorted(t))
# print(result)

# students = (
#     ("Amit", 85),
#     ("Priya", 92),
#     ("Rahul", 78),
#     ("Sneha", 95)
# )

# for student in students:
#     name, marks = student
#     print("Name:", name, "| Marks:", marks)