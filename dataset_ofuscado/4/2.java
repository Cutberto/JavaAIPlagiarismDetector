public class Pd {
    public static void main(String[] args) {
        String a = "radar";
        
        if (b(a)) {
            System.out.println(a + " is a palindrome.");
        } else {
            System.out.println(a + " is not a palindrome.");
        }
    }
    
    public static boolean b(String c) {
        String d = "";
        for (int e = c.length() - 1; e >= 0; e--) {
            d += c.charAt(e);
        }
        return c.equals(d);
    }
}
