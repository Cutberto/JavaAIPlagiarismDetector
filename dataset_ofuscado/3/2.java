public class PmN {
    public static void main(String[] args) {
        int a = 20;
        
        System.out.println("Prime numbers up to " + a + ":");
        for (int b = 2; b <= a; b++) {
            if (ip(b)) {
                System.out.print(b + " ");
            }
        }
    }
    
    public static boolean ip(int c) {
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
