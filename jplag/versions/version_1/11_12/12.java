public class Pc {
    public static void main(String[] args) {
        int a = 17;
        
        if (b(a)) {
            System.out.println(a + " is a prime number.");
        } else {
            System.out.println(a + " is not a prime number.");
        }
    }
    
    public static boolean b(int c) {
        if (c <= 1) {
            return false;
        }
        
        for (int d = 2; d <= Math.sqrt(c); d++) {
            if (c % d == 0) {
                return false;
            }
        }
        
        return true;
    }
}
