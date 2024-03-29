class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int count = 0;
        char[] strJewels = jewels.toCharArray();
        char[] strStones = stones.toCharArray();
        for (int i = 0; i < strJewels.length; i ++) {
            for (int j = 0; j < strStones.length; j ++) {
                if (strJewels[i] == strStones[j]) {
                    count ++;
                }
            }
        }
        return count;
    }
}