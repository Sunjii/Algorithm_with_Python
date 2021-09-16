# https://leetcode.com/problems/merge-k-sorted-lists/
# k 개의 정렬된 리스트를 1개의 정렬된 리스트로 병합

# input 
# [ 1->4->5, 1->3->4, 2->6 ]
# output
# [1->1->2->3->4->4->5->6]

def mergeKLists(lists):
    root = result = ListNode(None)
    heap = []

    # 각 리스트의 루트를 힙에 저장
    for i in range(len(lists)):
        heapq.heappush(heap, (lists[i].val, i, lists[i]))

    # 힙 추출 후 다음 노드 저장
    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]

        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))
        
    return root.next