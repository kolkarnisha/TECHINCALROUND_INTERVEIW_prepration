list=[2,21,2210,221027]
print(max(list))
def largestnum(list):
      for num in list:          
            if num>list:
                  largest=num
                  print(largest)
n=[1,"nisha",22,6.8,"taj"]
for i in n:
    # for j in n:
      print(i) # traverse by value
time and space complexity
a loop after loop is called consecutive,sequential loop
numbers=[10,27,38,46,59]
for index,j in enumerate(numbers):
    print(index,j)
reversearray=numbers[::-1]
print(reversearray)
list=[10,20,30,40,50]
count=0
while count<len(list):
    print(list[count])
    count+=1
sum=sum(numbers)
print(sum)  #time complexity 
sum=0
for i in numbers:
    i+sum
    print(sum)
n=0
for i in numbers:
    # n=0
    if i%2==0:
        print(i)
        n+=1
        print(n)
    else:
        print("odd number")
        print(i)
numbers=[4,8,12,16,20]
if 12 in numbers:
    print("true")
numbers=[4,8,12,16,20]
for i in numbers:
    if i==16:
        print(numbers.index(i))
list=[100,200,300,400]
for i in list:
    print(i)
revrsearray=list[::-1]
for i in revrsearray:
    print(i)
list=[1,2,3,4,"s",5,6,7,8,9,10]
print(len(list))
list.append("apple")
print(list)
print(list[1:5:2])
# print(list.remove("s"))
# print(list.pop())
# # print(list.remove(9))
# print(list.delete())
list=[1,2,3,4,"s",5,6,7,8,9,10]
print(list[2]==100)
list[3]=200
print(list)
list.insert(2,300)
print(list)
list.append(1)
list.extend([10,20,30])
print(list)
list.extend([10,20,30])
print(list)
list.pop()
list.pop[0]
