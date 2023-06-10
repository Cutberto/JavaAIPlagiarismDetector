public class Pw {
    public static void main(String[] args) {
        int a = 3;
        int b = 4;
        
        int c = d(a, b);
        System.out.println(a + " raised to the power of " + b + " is: " + c);
    }
    
    public static int d(int a, int b) {
        int c = 1;
        
        for (int i = 1; i <= b; i++) {
            c *= a;
        }
        
        return c;
    }
}
