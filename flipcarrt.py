#print the following series: 10,20...300

num=10
while(num<=300):
    print(num,end=",")
    num=num+10

#print the series: 105,98,91...7

num=105
while(num<=7):
    print(num) 
    num=num-7      

#sum of calculation example:

sum_list=[20,48,12,76,24]
i=0
sum=0

while i<len(sum_list):
    sum+=sum_list[i]
    i+=1
print(sum)    

#finding multiples of numbers:

n=int(input("Enter an integer:"))
i=1

while i<=10:
    cross=i*n
    i+=1
    print(cross)