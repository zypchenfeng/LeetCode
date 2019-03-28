/*
Given two arrays, write a function to compute their intersection.
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
*/
using namespace std;
class Solution
{
  public:
    vector<int> intersection(vector<int> &nums1, vector<int> &nums2)
    {
        unordered_set<int> s(nums1.begin(), nums1.end());
        vector<int> res;
        for(int x : nums2){
            if(s.erase(x))
                res.push_back(x);
        }
        return res;
    }
};