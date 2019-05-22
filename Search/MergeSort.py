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

A = [6, 5, 7, 1, 9, 3, 5, 4]

print(">> START :", A)
print(">> RESULT :", MergeSort(A, len(A)))