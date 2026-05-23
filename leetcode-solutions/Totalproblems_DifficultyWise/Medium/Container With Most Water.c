# Container With Most Water
# Difficulty: Medium
# Language: c

int maxArea(int* height,int heightSize){
    int left=0,right=heightSize-1,maxarea=0;
    while(left<right){
        int h=height[left]<height[right]?height[left]:height[right];
        int area=(right-left)*h;
        if(area>maxarea)maxarea=area;
        if(height[left]<height[right])left++;
        else right--;
    }
    return maxarea;
}
