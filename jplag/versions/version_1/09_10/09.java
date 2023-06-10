public class Factorial {
    public static void main(String[] args) {
        int n = 5;
        int factorial = calculateFactorial(n);
        System.out.println("Factorial of " + n + " is: " + factorial);
    }
    
    public static int calculateFactorial(int num) {
        if (num == 0 || num == 1) {
            return 1;
        }
        
        int result = 1;
        for (int i = 2; i <= num; i++) {
            result *= i;
        }
        
        return result;
    }
}
