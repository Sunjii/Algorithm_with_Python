def solution(name):
    answer = 0
    
    # 유니코드를 사용하여 문자열을 비교하자
    # 상하이동
    # moves = [min(ord(n) - ord('A'), ord('Z') - ord(n)+1) for n in name]
    
    # 좌우이동 ~ 그리드
    # 바꿔야 할 문자가 더 가까운 곳으로 이동해간다.
    # name에 A가 있는 곳을 가능한 방문하지 않아야 한다.
    
    # 현재 위치에서 다음 바꿀 곳 까지 right 방향과 left 방향의 거리를 구해본다. 'A'를 지나가면 된다.
    # 더 짧은 방향으로 최종 결정한다.
    
    cursor = 0
    name = list(name)
    
    while True:
        # 상하이동
        answer += min(ord(name[cursor]) - ord('A'), ord('Z') - ord(name[cursor])+1)
        
        name[cursor] = 'A' # 방문한 곳은 A로 표기하여 스킵
        if name.count('A') == len(name): return answer
        
        left, right = 1, 1
        # 오른쪽 탐색
        for r in range(1, len(name)):
            if name[cursor + r] == 'A':
                right += 1
            else:
                break
        # 왼쪽 탐색
        for l in range(1, len(name)):
            if name[cursor - l] == 'A':
                left += 1
            else:
                break
        # 더 짧은 방향이 어디인지 비교
        if left < right:
            answer += left
            cursor -= left
        else:
            answer += right
            cursor += right
    
    
    return answer