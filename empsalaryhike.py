print("Enter the Values of List separated by Space:")
lst=[float(val) for val in input().split()]
from functools import reduce
lst10=list(float(val) for val in lst if(0<val<=500))
lst20=list(float(val) for val in lst if(500<val<=1000))
amt10= [float('%.2f'%val) for val in list(map(lambda n: n*1.10,list(filter(lambda n:500<n<=1000,lst))))]
totalamt10=reduce(lambda x,y:x+y,list(map(lambda n: n*1.10,list(filter(lambda n:500<n<=1000,lst)))))
amt20= [float('%.2f'%val) for val in list(map(lambda n: n*1.20,list(filter(lambda n:0<n<=500,lst))))]
totalamt20=reduce(lambda x,y:x+y,list(map(lambda n: n*1.20,list(filter(lambda n:0<n<=500,lst)))))

print("="*80)
print("Given List of Employees Salaries: ",lst)
print("="*80)
print("List of Employee Salary(0-500): ",lst10)
print("list of 20% hike Amount salary(0-500): ",amt20)
print("Total Amount of 20% hike for salary(0-500)= ",totalamt20)
print("="*80)
print("List of Employee Salary(500-1000): ",lst20)
print("list of 10% hike Amount salary(500-1000): ",amt10)
print("Total Amount of 10% hike for salary(500-1000)= ",totalamt10)
print("="*80)
