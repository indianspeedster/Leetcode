class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        int left = 0;
        long long ans = 0;
        long long curr = 0;

        unordered_set<int> hashset;

        for (int right =0; right < nums.size(); right++){

            curr += nums[right];

            while (hashset.count(nums[right])){
                hashset.erase(nums[left]);
                curr -= nums[left];
                left += 1;
            }

            hashset.insert(nums[right]);

            if (right-left+1==k){
                ans = max(ans, curr);
                curr -= nums[left];
                hashset.erase(nums[left]);
                left += 1;
            }

        }
        return ans;
        
    }
};