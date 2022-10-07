

public class SubarraySum {

    public static void main(String[] args) {
        int [] arr = {1,-1,0};
        int answer = subarraySum(arr, 0);
        System.out.printf("Answer: %d\n", answer);
    }

    private static int subarraySum(int[] nums, int k) {
        int count = 0;
        int sum;

        for (int i = 0; i < nums.length; i++) {
            sum = nums[i];

            int j = i + 1;
            while (j < nums.length) {
                sum += nums[j];
                if ((sum > k) || (sum == k)) { break; }
                j++;
            }

            if (sum == k) { count++; }
        }

        return count;
    }
}
