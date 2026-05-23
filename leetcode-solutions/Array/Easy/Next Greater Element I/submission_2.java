# Problem: Next Greater Element I
# Difficulty: Easy
# Topic: Array
# Language: java
# Submission: 2

class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            int start = 0;
            int res = -1;

            for (int j = 0; j < nums2.length; j++) {
                if (nums1[i] == nums2[j]) {
                    start = j + 1;
                    break;
                }
            }

            while (start < nums2.length) {
                if (nums2[start] > nums1[i]) {
                    res = nums2[start];
                    break;
                }
                start++;
            }

            arr[i] = res;
        }

        return arr;
    }
}
