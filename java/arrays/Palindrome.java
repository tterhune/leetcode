public class Palindrome {

    public static boolean pal(String s) {
        System.out.println(s);
        int i = 0;
        int j = s.length() - 1;
        char [] chars = s.toLowerCase().toCharArray();

        while (i <= j) {
            if (chars[i] == chars[j]) {
                i++; j--;
            }
            else if (chars[i] != chars[j]) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        String s = "foobar";
        boolean result = pal(s);
        System.out.printf("String: %s palindrome? %b\n", s, result);

        s = "RaCecar";
        result = pal(s);
        System.out.printf("String: %s palindrome? %b\n", s, result);

        s = "abaaba";
        result = pal(s);
        System.out.printf("String: %s palindrome? %b\n", s, result);

        s = "a";
        result = pal(s);
        System.out.printf("String: %s palindrome? %b\n", s, result);

        s = "abcdcba";
        result = pal(s);
        System.out.printf("String: %s palindrome? %b\n", s, result);
    }
}
