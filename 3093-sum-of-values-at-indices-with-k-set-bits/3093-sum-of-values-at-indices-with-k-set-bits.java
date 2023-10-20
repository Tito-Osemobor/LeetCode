class Solution {
    public int sumIndicesWithKSetBits(List<Integer> nums, int k) {
        String numsToBinary;
        int sum = 0;
        int countBit = 0;
        for (int i = 0; i < nums.size(); i ++) {
            numsToBinary = Integer.toBinaryString(i);
            countBit = 0;
            for (int j = 0; j < numsToBinary.toCharArray().length ; j ++) {
                if (numsToBinary.toCharArray()[j] == '1') {
                    countBit ++;
                }
            }
            if (countBit == k) {
                sum += nums.get(i);
            }
        }
        return sum;
    }
}