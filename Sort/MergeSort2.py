#합병정렬 Merge Sort
#최선과 최악의 평균 수행 시간이 모두 O(n*lon(n))
#안정적 정렬, 비제자리 정렬

def MergeSort(A, n):
  if n>1:
    Mid = int(n/2)
    B = MergeSort(A[:Mid], Mid)
    C = MergeSort(A[Mid:], n-Mid)
    print("ms B=", B, end=", ")
    print("ms C=", C, end=", ")
    A = Merge(B, C, Mid, n-Mid)
    print("m A=", A)
  return A

def Merge(B, C, n, m):
  i, j = 0, 0
  A = []
  while i<n and j<m:
    if B[i]<=C[j]:
      A.append(B[i])
      i+=1
    else:
      A.append(C[j])
      j+=1
  for k in range(i, n): A.append(B[k])
  for l in range(j, m): A.append(C[l])
  return A


if __name__=="__main__":
  A = [6, 5, 7, 1, 9, 3, 5, 4]
  print(">> START :", A)
  print(">> RESULT :", MergeSort(A, len(A)))