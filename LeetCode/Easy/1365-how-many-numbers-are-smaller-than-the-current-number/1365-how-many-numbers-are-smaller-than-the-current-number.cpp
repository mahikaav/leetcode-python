class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        map<int,int> mp;
        for (int i : nums){
            mp[i]++;
        }
        vector<int> ans;
        for (int i : nums){
            int count = 0;
            for (auto item : mp){
                if (i == item.first){
                    ans.push_back(count);
                    break;
                }
                else count += item.second;
            }
        }
        return ans;
    }
};