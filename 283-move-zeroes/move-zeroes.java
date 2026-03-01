class Solution {
    public void moveZeroes(int[] nums) {

        int index = 0; // this will track where to put the next non-zero number

        // Step 1: Put all non-zero numbers in front
        for (int num : nums) {
            if (num != 0) {
                nums[index] = num;
                index++;
            }
        }

        // Step 2: Fill the rest of the array with zeroes
        while (index < nums.length) {
            nums[index] = 0;
            index++;
        }
    }
}