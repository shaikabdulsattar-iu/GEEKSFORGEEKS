class Solution {
  public:
    int arraySum(vector<int>& arr) {
        int sum = 0;
        for (int num : arr) {
            sum += num;
        }
        return sum;
    }
};