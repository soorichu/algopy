#정렬 알고리즘

정렬 - 여러 데이터로 구성된 리스트에서 값의 크기 순서에 따라 데이터를 재배치하는 것

* 정렬 시점에 따라 내부정렬과 외부정렬로 나눌 수 있다.
(1) 내부정렬 - 모든 데이터를 주기억장치에 저장한 후 정렬하는 방식
(2) 외부정렬 - 모든 데이터를 주기억장치에 저장할 수 없는 경우, 모든 데이터를 보조기억장치를 정장한 채 일부 데이터씩만 반복적으로 주기억장치로 읽어 들여서 정렬하는 방식
-> 주로 내부정렬에 대해 공부

* 내부정렬 알고리즘의 종류
정렬 방식에 따라 비교기반 알고리즘과 데이터 분포 기반 알고리즘.
우리가 흔히 공부하는 것은 비교기반 알고리즘

* 비교기반 알고리즘(★)
버블 정렬 Bubble Sort    O(n^2) 안정, 제자리
선택 정렬 Selection Sort O(n^2) 불안정, 제자리
삽입 정렬 Insert Sort    O(n)~O(n^2) 안정, 제자리
셀   정렬 Shell Sort     O(n*log(n))~O(n^2) 불안정, 제자리
------------(보통 성능)
합병 정렬
퀵 정렬
힙 정렬
-----------(향상된 성능)
키값의 비교횟수로 비교함.
*
* 데이터 분포 기반 알고리즘
계수정렬
기수정렬
------------(선형시간의 복잡도를 가짐)
자료의 이동횟수로서 비교함.
*
* 안정적(stable) 정렬
동일한 값을 갖는 데이터가 여러 개 있을 때 정렬 전의 상대적인 순서가 정렬 후에도 그대로 유지되는 정렬 방식
(예) 입력 데이터가 ....A...B....인 경우
안정적인 정렬은   ....AB......
불안정적인 정렬은 ....BA......
*
* 제자리(in-place) 정렬
입력 데이터를 저장하는 공간 이외에 추가적인 저장공간을 상수 개만 필요로 하는 정렬 방식
입력 크기 n이 증가함에도 불구하고 추가적인 저장공간은 증가하지 않음.
*
*
* 버블, 선택, 삽입, 쉘 정렬을 비교해보았다.
$ python BubbleSort.py
Input : H E L L O W O R L D
Step1 : E H L L O O R L D W
Step2 : E H L L O O L D R W
Step3 : E H L L O L D O R W
Step4 : E H L L L D O O R W
Step5 : E H L L D L O O R W
Step6 : E H L D L L O O R W
Step7 : E H D L L L O O R W
Step8 : E D H L L L O O R W
Step9 : D E H L L L O O R W
total time : 3.4720776081085205 millisec
*
$ python SelectionSort.py
Input : H E L L O W O R L D
Step1 : D E L L O W O R L H
Step2 : D E L L O W O R L H
Step3 : D E H L O W O R L L
Step4 : D E H L O W O R L L
Step5 : D E H L L W O R O L
Step6 : D E H L L L O R O W
Step7 : D E H L L L O R O W
Step8 : D E H L L L O O R W
Step9 : D E H L L L O O R W
total time : 3.150067090988159 millisec
*
$ python InsertSort.py
Input : H E L L O W O R L D
Step2 : E H L L O W O R L D
Step3 : E H L L O W O R L D
Step4 : E H L L O W O R L D
Step5 : E H L L O W O R L D
Step6 : E H L L O W O R L D
Step7 : E H L L O O W R L D
Step8 : E H L L O O R W L D
Step9 : E H L L L O O R W D
Step10 : D E H L L L O O R W
total time : 3.0931222438812256 millisec
*
$ python ShellSort.py
Input : H E L L O W O R L D
Step1 : H E L L D W O R L O
Step2 : H E D L L W O R L O
Step3 : H E D L L W L R O O
Step4 : H E D L L R L W O O
Step5 : H E D L L R L O O W
Step6 : H E D L L O L R O W
Step7 : E H D L L O L R O W
Step8 : E D H L L O L R O W
Step9 : D E H L L O L R O W
Step10 : D E H L L L O R O W
Step11 : D E H L L L O O R W
total time : 3.058487892150879 millisec
*
H E L L O W O R L D로 실행해본 결과
버블 < 선택 < 삽입 < 쉘 정렬 순으로 성능이 좋았다. ^^# algopy
알고리즘을 파이썬으로 구현
