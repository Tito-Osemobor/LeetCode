class Solution {
    public String interpret(String command) {
        StringBuilder S = new StringBuilder(command.length());
        for (int i = 0; i < command.length(); i ++) {
            if (command.charAt(i) == '(' && command.charAt(i+1) == ')') {
                S.append('o');
            }
            else if (command.charAt(i) == '(' || command.charAt(i) == ')') {
                continue;
            }
            else {
                S.append(command.charAt(i));
            }
        }
        return S.toString();
    }
}