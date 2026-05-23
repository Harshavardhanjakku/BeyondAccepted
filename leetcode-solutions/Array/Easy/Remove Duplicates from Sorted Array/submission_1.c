# Problem: Remove Duplicates from Sorted Array
# Difficulty: Easy
# Topic: Array
# Language: c
# Submission: 1

int removeDuplicates(int* nums, int numsSize) {
    if(numsSize==0)
        return 0;

    int i=0,j=0;

    while(j<numsSize){
        if(nums[i]!=nums[j]){
            i++;
            int temp=nums[i];
            nums[i]=nums[j];
            nums[j]=temp;
        }
        j++;
    }

    return i+1;
}
