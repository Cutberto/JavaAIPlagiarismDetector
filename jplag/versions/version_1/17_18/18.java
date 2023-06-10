public class Fbncc {
    public static void main(String[] args) {
        int a = 10;
        
        System.out.println("Fibonacci series up to " + a + ":");
        for (int b = 0; b < a; b++) {
            System.out.print(c(b) + " ");
        }
    }
    
    public static int c(int d) {
        if (d == 0 || d == 1) {
            return d;
        }
        
        int e = 0;
        int f = 1;
        int g = 0;
        
        for (int h = 2; h <= d; h++) {
            g = e + f;
            e = f;
            f = g;
        }
        
        return g;
    }
}
s