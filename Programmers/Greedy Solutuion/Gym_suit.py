"""
n = 5
reserve = 1 3 5
lost = 2 4
나눠주는 방법은 2가지가 가능하다.
1  3  5
 \  \
 2   4
 혹은
1  3  5
  /  /
 2   4
 * 빌려주는 방향에 따라서 최대 학생수가 달라질 수 있음!!!!
"""

def solution(n, lost, reserve):
    # sol2
    s = set(lost) & set(reserve) # 교집합
    l = set(lost) - s # 차집합. 이 학생은 체육복이 1개가 됨
    r = set(reserve) - s # 2벌 있는 학생
    for x in sorted(r):
        if x - 1 in l:
            l.remove(x-1) # 빌려주지 못하므로 제거
        elif x + 1 in l:
            l.remove(x+1) 
        # 남은 l은 빌려야 하는데 못 빌리는 사람임
    return n - len(l)

    """
    sol1)
    학생은 최대 30명. --> 학생 수 만큼 배열 확보
    배열에 각자 가지고 있는 체육복의 수를 기록한다 (도난당한것 반영)
    계산 결과 2인 학생만이 체육복을 빌려줄 수 있다.
    
    - 복잡도
        여벌을 가져온 학생 : reserve의 길이에 비례
        체육복을 잃어버린 학생 : lost에 비례
        빌려주기 처리 : 전체 학생 수에 비례
        따라서 전체 복잡도는 O(n)에 불과함
        
    sol2)
    만약 n이 엄청 크다면? 거기에 reserve가 매우 적다면?
    n에 해당하는 배열을 예약해야 함. 매우 많은 메모리가 필요하다.
    또 reserve가 매우 적기 때문에 쓸데없이 카운팅을 하게 됨
    -> reserve를 정렬하고 이 배열을 살펴보면서 빌려주기 처리를 하자
    정렬하므로 O(klogk) 이다.
    - 복잡도
        reserve 정렬 (reserve 길이가 k라면) : O(klogk)
        빌려주기 찾아서 처리 : O(k) x O(1) {해시테이블을 이용하여 상수처리 가능}
        전체 : O(klogk)
    n이 k랑 비슷하다면 sol1을 택하는게 좋을 수 있음. sol2를 채택하는 경우는 klogk가 n보다 유리한 경우 (k <<<< n)인 상황이다.
    """
    
    uniform = [1] * (n+2) # 앞 뒤로 허깨비를 하나씩 세워둠
    for i in reserve:
        uniform[i] += 1
    for i in lost:
        uniform[i] -= 1
    
    # 빌려주기 처리
    for i in range(1, n+1):
        if uniform[i - 1] == 0 and uniform[i] == 2:
            uniform[i-1:i+1] = [1,1] # i-1과 i가 1이 됨 (슬라이싱)
        elif uniform[i] == 2 and uniform[i+1] == 0:
            uniform[i:i+2] = [1,1]
    
    # 참여할 수 있는 학생 구하기
    return len([x for x in uniform[1:-1] if x>0])