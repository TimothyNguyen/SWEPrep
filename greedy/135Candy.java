public class Solution {
    public int candy(int[] ratings) {
        if (ratings.length == 0) return 0;
        int ret = 1;
        int up = 0, down = 0, peak = 0;
        for (int i = 1; i < ratings.length; i++) {
            if (ratings[i - 1] < ratings[i]) {
                peak = ++up;
                down = 0;
                ret += 1 + up;
            } else if (ratings[i - 1] == ratings[i])  {
                peak = up = down = 0;
                ret += 1;
            } else {
                up = 0;
                down++;
                ret += 1 + down + (peak >= down ? -1 : 0);
            }
        }

        return ret;
    }
}
/*
To use two variables 'up' and 'down' to count the steps of continuous up and down respectively, and a 'peak' representing the peak before going down. In the below example:

[0, 1, 20, 9, 8, 7]
Scan from left to right, first child is given 1 candy;
the second child is given 2 candies, and up=1;
the third child is given 3 candies, and up=2; peak=2;
the fourth child is given 1 candy, and down=1; and third child still has 3 candies since peak=2;
the fifth child is given 1 candy, and down=2; and the previous child needs 1 more candy now but the third child no need more;
the sixth child is given 1 candy, and down=3; and both the fifth and fourth child needs 1 more candy now, and the peak, the third child need 1 more as well.

*/