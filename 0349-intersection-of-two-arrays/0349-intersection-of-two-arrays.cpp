
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        
        vector<int> result;
        int i = 0, j = 0;
        
        while(i < nums1.size() && j < nums2.size()) {
            if(nums1[i] == nums2[j]) {
                if(result.empty() || result.back() != nums1[i]) {
                    result.push_back(nums1[i]);
                }
                i++;
                j++;
            } else if(nums1[i] < nums2[j]) {
                i++;
            } else {
                j++;
            }
        }
        
        return result;
    }
};
/*class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {

        
        /*vector<int> inter;
        

        for(int i = 0; i < nums1.size(); i++)
    {
        for(int j = 0; j < nums2.size(); j++)
        {
            if(nums1[i] == nums2[j])
            {
                // check if already in inter
                bool exists = false;
                for(int k = 0; k < inter.size()&&!exists; k++)
                {
                    if(inter[k] == nums1[i])
                    {
                        exists = true;
                    }
                }

                if(!exists)
                inter.push_back(nums1[i]);
            }
        }}
        return inter;*/
//}
 //   };

    