import heapq

class Solution:
    # @param nums {int[]} an integer unsorted array
    # @param k {int} an integer from 1 to n
    # @return {int} the kth largest element
    def kthLargestElement2(self, nums, k):
        # Write your code here
        # �����ص㣺N is much larger than k
        # ����ʹ��O(n)��quick select����Ҫʹ��O(klogn)�Ķ�����
        return heapq.nlargest(k, nums)[-1]