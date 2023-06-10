public class Power {
    public static void main(String[] args) {
        int base = 3;
        int exponent = 4;
        
        int result = power(base, exponent);
        System.out.println(base + " raised to the power of " + exponent + " is: " + result);
    }
    
    public static int power(int base, int exponent) {
        int result = 1;
        
        for (int i = 1; i <= exponent; i++) {
            result *= base;
        }
        
        return result;
    }
}
