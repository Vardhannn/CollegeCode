import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10**8)
import timeit
def bubble(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-i-1):
			if arr[j]>arr[j+1] :
				arr[j],arr[j+1]=arr[j+1],arr[j]
	return arr
def part(arr,l,h):
	p = arr[h]
	i = l-1
	plt.plot()
	for j in range(l, h):
		if arr[j] <= p:
			i=i+1
			(arr[i], arr[j]) = (arr[j], arr[i])
	(arr[i + 1], arr[h]) = (arr[h], arr[i + 1])
	return i + 1
def quick(array, low, high):
	if low < high:
		pi = part(array, low, high)
		if (pi-1-low)<=100 :
			array[low:pi]=bubble(array[low:pi])
		else :
			quick(array, low, pi - 1)
		if (high-pi-1)<=100 :
			(array[pi+1:high+1])=bubble(array[pi+1:high+1])
		else :
			quick(array, pi + 1, high)
import random
t1=[]
s1=[]
for i in range(0,6):
	x = timeit.default_timer()
	data=[]
	for i in range(10**(i+1)):
		data.append(random.randrange(1,10000,1))

	quick(data, 0, len(data) - 1)
	y=timeit.default_timer()
	t1.append(y-x)
	s1.append(i)
plt.plot(s1,t1)
