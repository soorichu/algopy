#기수 정렬(Radix Sort)
#기수 정렬은 입력값을 자릿수 별로 부분적으로 비교하는 정렬 방식으로, 
#주어진 정렬의 키값을 자릿수별로 나누고, 자릿수별로 계수정렬과 같은 
#안정적인 정렬 알고리즘을 반복적으로 적용하여 정렬하는 방법이다.
#LSD(Least Sighificant Digit)와 MSD(Most Significant Digit)가 있다.
#시간복잡도는 O(n)
#안정적인 정렬, 비제자리 정렬

from MergeSort2 import MergeSort

def RadixSort(A, n):
	for i in range(len(str(max(A)))):
		print(i, A)
		R = [int(a%(10**(i+1))/(10**i)) for a in A]
		print(R)
		i = 0
		At = A[:]
		for r in MergeSort(R, n):
			print(At, R)
			A[i] = At.pop(R.index(r)); 
			i+=1; R.pop(R.index(r))
	return A


if __name__ == "__main__":
	A = [281, 265, 442, 94, 363, 68, 119, 100]
	print(RadixSort(A,len(A)))