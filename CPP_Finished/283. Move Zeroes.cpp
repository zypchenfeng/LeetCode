/*
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
*/

class Solution
{
  public:
    void moveZeroes(vector<int> &nums)
    {
        int i = 0;
        int j = 0;
        while (j < nums.size())
        {
            if (nums[j] != 0)
            {
                nums[i++] = nums[j];
            }
            j++;
        }
        while (i < nums.size())
        {
            nums[i++] = 0;
        }
    }
};

/* solution 2
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        if(!n) return;
        int i = 0;
        for(int j=0; j<n; j++){
            if(nums[j] != 0)
                swap(nums[i++], nums[j]);
        }
    }
};
*/