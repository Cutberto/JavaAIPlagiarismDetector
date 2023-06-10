public class Fibonacci {
    public static void main(String[] args) {
        int n = 10;
        
        System.out.println("Fibonacci series up to " + n + ":");
        for (int i = 0; i < n; i++) {
            System.out.print(fibonacci(i) + " ");
        }
    }
    
    public static int fibonacci(int num) {
        if (num == 0 || num == 1) {
            return num;
        }
        
        int a = 0;
        int b = 1;
        int fib = 0;
        
        for (int i = 2; i <= num; i++) {
            fib = a + b;
            a = b;
            b = fib;
        }
        
        return fib;
    }
}
