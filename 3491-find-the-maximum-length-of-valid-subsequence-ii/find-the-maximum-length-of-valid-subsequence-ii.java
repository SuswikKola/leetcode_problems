import java.util.*;

class Solution {
    public int maximumLength(int[] nums, int k) {
        int n = nums.length;
        int[][] dp = new int[n][k];
        int ans = 1;

        for (int i = 0; i < n; i++) {
            for (int x = 0; x < k; x++) {
                dp[i][x] = 1;
            }

            for (int j = 0; j < i; j++) {
                int x = (nums[j] + nums[i]) % k;
                if (dp[j][x] + 1 > dp[i][x]) {
                    dp[i][x] = dp[j][x] + 1;
                    ans = Math.max(ans, dp[i][x]);
                }
            }
        }

        return ans;
    }
}
