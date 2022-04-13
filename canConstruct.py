# 605 · Sequence Reconstruction LintCode
# Description
# Check whether the original sequence org can be uniquely 
# reconstructed from the sequences in seqs. The org sequence 
# is a permutation of the integers from 1 to n, with 1 <= n <= 10^4. 

# Reconstruction means building a shortest common supersequence
#  of the sequences in seqs (i.e., a shortest sequence so that 
#  all sequences in seqs are subsequences of it). Determine whether 
#  there is only one sequence that can be reconstructed from seqs 
#  and it is the org sequence.


# Example 1:

# Input:org = [1,2,3], seqs = [[1,2],[1,3]]
# Output: false
# Explanation:
# [1,2,3] is not the only one sequence that can be reconstructed,
#  because [1,3,2] is also a valid sequence that can be 
#  reconstructed.

# Example 2:

# Input: org = [1,2,3], seqs = [[1,2]]
# Output: false
# Explanation:
# The reconstructed sequence can only be [1,2], can't 
# reconstruct the sequence [1,2,3]. 

# Example 3:

# Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
# Output: true
# Explanation:
# The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct 
# the original sequence [1,2,3].

# Example 4:

# Input:org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
# Output:true


from collections import deque

def canConstruct(originalSeq, sequences):
    indegree = dict()
    graph = dict()

    for sequence in sequences:
        for number in sequence:
            indegree[number] = 0
            graph[number] = list()

    if len(indegree) != len(originalSeq):
        return False
    
    for sequence in sequences:
        for i in range(len(sequence) - 1):
            parent = sequence[i]
            child = sequence[i + 1]
            indegree[child] += 1
            graph[parent].append(child)

    queue = deque()

    for key, value in indegree.items():
        if value == 0:
            queue.append(key)
    
    sortedOrder = []

    while queue:
        if (len(queue) > 1):
            return False
        
        currNode = queue.popleft()
        sortedOrder.append(currNode)
        for nbr in graph[currNode]:
            indegree[nbr] -= 1
            if indegree[nbr] == 0:
                queue.append(nbr)

    if len(sortedOrder) != len(originalSeq):
        return False

    # for i in range(len(originalSeq)):
    #     if originalSeq[i] != sortedOrder[i]:
    #         return False

    return len(sortedOrder) == len(originalSeq)

if __name__ == '__main__':
    originalSeq = [3, 1, 4, 2, 5]
    seqs = [[3, 1, 5], [1, 4, 2 ,5]]
    print(canConstruct(originalSeq, seqs))