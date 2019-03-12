## 정렬 알고리즘
정렬 - 여러 데이터로 구성된 리스트에서 값의 크기 순서에 따라 데이터를 재배치하는 것
<br />

## 정렬 시점에 따라 내부정렬과 외부정렬로 나눌 수 있다.
(1) 내부정렬 - 모든 데이터를 주기억장치에 저장한 후 정렬하는 방식<br />
(2) 외부정렬 - 모든 데이터를 주기억장치에 저장할 수 없는 경우, 모든 데이터를 보조기억장치를 정장한 채 일부 데이터씩만 반복적으로 주기억장치로 읽어 들여서 정렬하는 방식<br />
우리는 주로 내부정렬에 대해 공부<br />
<br />

## 내부정렬 알고리즘의 종류
정렬 방식에 따라 비교기반 알고리즘과 데이터 분포 기반 알고리즘.<br />
우리가 흔히 공부하는 것은 비교기반 알고리즘<br />
<br />

## 비교기반 알고리즘(★)
버블 정렬 Bubble Sort    O(n^2) 안정, 제자리<br />
선택 정렬 Selection Sort O(n^2) 불안정, 제자리<br />
삽입 정렬 Insert Sort    O(n)~O(n^2) 안정, 제자리<br />
셀   정렬 Shell Sort     O(n log(n))~O(n^2) 불안정, 제자리<br />
------------(보통 성능)<br />
합병 정렬<br />
퀵 정렬<br />
힙 정렬<br />
-----------(향상된 성능)<br />
키값의 비교횟수로 비교함.<br />

## 데이터 분포 기반 알고리즘
계수정렬<br />
기수정렬<br />
------------(선형시간의 복잡도를 가짐)<br />
자료의 이동횟수로서 비교함.<br />

## 안정적(stable) 정렬
동일한 값을 갖는 데이터가 여러 개 있을 때 정렬 전의 상대적인 순서가 정렬 후에도 그대로 유지되는 정렬 방식<br />
(예) 입력 데이터가 ....A...B....인 경우<br />
안정적인 정렬은   ....AB......<br />
불안정적인 정렬은 ....BA......<br />
<br />

## 제자리(in-place) 정렬
입력 데이터를 저장하는 공간 이외에 추가적인 저장공간을 상수 개만 필요로 하는 정렬 방식<br />
입력 크기 n이 증가함에도 불구하고 추가적인 저장공간은 증가하지 않음.<br />
<br />

## 버블, 선택, 삽입, 쉘 정렬을 비교해보았다.
$ python BubbleSort.py<br />
Input : H E L L O W O R L D<br />
Step1 : E H L L O O R L D W<br />
Step2 : E H L L O O L D R W<br />
Step3 : E H L L O L D O R W<br />
Step4 : E H L L L D O O R W<br />
Step5 : E H L L D L O O R W<br />
Step6 : E H L D L L O O R W<br />
Step7 : E H D L L L O O R W<br />
Step8 : E D H L L L O O R W<br />
Step9 : D E H L L L O O R W<br />
total time : 3.4720776081085205 millisec<br />

$ python SelectionSort.py<br />
Input : H E L L O W O R L D<br />
Step1 : D E L L O W O R L H<br />
Step2 : D E L L O W O R L H<br />
Step3 : D E H L O W O R L L<br />
Step4 : D E H L O W O R L L<br />
Step5 : D E H L L W O R O L<br />
Step6 : D E H L L L O R O W<br />
Step7 : D E H L L L O R O W<br />
Step8 : D E H L L L O O R W<br />
Step9 : D E H L L L O O R W<br />
total time : 3.150067090988159 millisec<br />

$ python InsertSort.py<br />
Input : H E L L O W O R L D<br />
Step2 : E H L L O W O R L D<br />
Step3 : E H L L O W O R L D<br />
Step4 : E H L L O W O R L D<br />
Step5 : E H L L O W O R L D<br />
Step6 : E H L L O W O R L D<br />
Step7 : E H L L O O W R L D<br />
Step8 : E H L L O O R W L D<br />
Step9 : E H L L L O O R W D<br />
Step10 : D E H L L L O O R W<br />
total time : 3.0931222438812256 millisec<br />

$ python ShellSort.py<br />
Input : H E L L O W O R L D<br />
Step1 : H E L L D W O R L O<br />
Step2 : H E D L L W O R L O<br />
Step3 : H E D L L W L R O O<br />
Step4 : H E D L L R L W O O<br />
Step5 : H E D L L R L O O W<br />
Step6 : H E D L L O L R O W<br />
Step7 : E H D L L O L R O W<br />
Step8 : E D H L L O L R O W<br />
Step9 : D E H L L O L R O W<br />
Step10 : D E H L L L O R O W<br />
Step11 : D E H L L L O O R W<br />
total time : 3.058487892150879 millisec<br />

H E L L O W O R L D로 실행해본 결과<br />
버블 - 선택 - 삽입 - 쉘 정렬 순으로 성능이 좋았다.<br />
