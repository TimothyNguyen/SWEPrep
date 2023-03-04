class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
        int n = nums.size();
        vector<int> dp;
        if (n == 0)
            return dp;
        dp.push_back(*max_element(nums.begin(), nums.begin()+k));
        for (int i=1; i<n-k+1; i++)
        {
            if (nums[i+k-1] >= dp[i-1])
                dp.push_back(nums[i+k-1]);
            else if (nums[i+k-1] < dp[i-1] && dp[i-1] > nums[i-1])
                dp.push_back(dp[i-1]);
            else
                dp.push_back(*max_element(nums.begin()+i, nums.begin()+i+k));
        }
        return dp;
    }
};