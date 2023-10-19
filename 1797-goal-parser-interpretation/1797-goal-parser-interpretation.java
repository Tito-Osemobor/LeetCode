class Solution {
    public String interpret(String command) {
        String result = "";
        for (int i = 0; i < command.length(); i ++) {
            if (command.charAt(i) == '(' && command.charAt(i+1) == ')') {
                result += 'o';
            }
            else if (command.charAt(i) == '(' || command.charAt(i) == ')') {
                continue;
            }
            else {
                result += command.charAt(i);
            }
        }
        return result;
    }
}