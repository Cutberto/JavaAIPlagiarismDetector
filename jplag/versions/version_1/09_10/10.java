public class Ftrl {
    public static void main(String[] args) {
        int a = 5;
        int b = cb(a);
        System.out.println("cb of " + a + " is: " + b);
    }
    
    public static int cb(int c) {
        if (c == 0 || c == 1) {
            return 1;
        }
        
        int d = 1;
        for (int e = 2; e <= c; e++) {
            d *= e;
        }
        
        return d;
    }
}
