public class Fbnc {
    public static void main(String[] args) {
        int b = 10;
        int[] a = new int[b];
        
        a[0] = 0;
        a[1] = 1;
        
        for (int i = 2; i < b; i++) {
            a[i] = a[i - 1] + a[i - 2];
        }
        
        System.out.println("Fibonacci series:");
        for (int i = 0; i < b; i++) {
            System.out.print(a[i] + " ");
        }
    }
}
