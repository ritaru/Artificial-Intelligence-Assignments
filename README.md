# About
https://github.com/JeongUkJae/Artificial-Intelligence-Assignments 중 8Puzzle Problem Solver만을 포크한 레포지토리입니다.
2018년 2학기 인공지능 수업 과제 제출용입니다.  

## 8 Puzzle

### Results

|steps	| BFS 		| IDS 		|Heuristics 1	|Heuristics 2	|
|---	|---		|---		|---			|---	        |
| 3 	| 0.00315s  | 0.01033s  | 0.00457s 	    | 0.00451s 	    |
| 5 	| 0.00675s  | 0.01635s  | 0.00577s 	    | 0.00810s 	    |
| 7	    | 0.01231s	| 0.02928s	| 0.00712s		| 0.00998s 	    |

steps 만큼 섞은 후 (랜덤하게 섞음) 특정 알고리즘으로 풀게 하였다. 랜덤하게 섞어, 각각의 시행마다 차이가 존재하여, 충분히 큰 수인 1000번 시행 후 평균을 내었다.

섞을 때는 랜덤한 action(UP, DOWN, LEFT, RIGHT)를 취하여 Goal Test를 통과할 수 있는 경우만을 생성하도록 하였다.

### 참고

Heuristics 1과 2는 A Star 방식의 탐색 알고리즘이다.

Heuristics 1은 잘못 놓은 타일의 갯수를 h 함수로 두었다. 반면 Heuristics 2는 전체 Manhattan Distance를 h 함수로 두었다.
