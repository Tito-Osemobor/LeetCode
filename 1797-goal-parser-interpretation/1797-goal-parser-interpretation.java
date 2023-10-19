class Solution {
    public String interpret(String command) {
        char[] strCommand = command.toCharArray();
        String result = "";
        for (int i = 0; i < strCommand.length; i ++) {
            if (strCommand[i] == '(' && strCommand[i+1] == ')') {
                result += 'o';
            }
            else if (strCommand[i] == '(' || strCommand[i] == ')') {
                continue;
            }
            else {
                result += strCommand[i];
            }
        }
        return result;
    }
}