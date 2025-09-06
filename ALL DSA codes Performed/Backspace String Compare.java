package q3596;

public class CTJ3596 {

	public static boolean backspaceCompare(String s, String t) {
		return processString(s).equals(processString(t));
    }
    
    private static String processString(String str) {
        StringBuilder result = new StringBuilder();
        for (char c : str.toCharArray()) {
            if (c == '#') {
                if (result.length() > 0) {
                    result.deleteCharAt(result.length() - 1);
                }
            } else {
                result.append(c);
            }
        }
        return result.toString();

	}

	public static void main(String[] args) {
		String s = args[0];
		String t = args[1];
		System.out.println(backspaceCompare(s, t));
	}
}