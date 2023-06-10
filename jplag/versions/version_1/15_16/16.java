public class As {
    public static void main(String[] args) {
        int[] a = {1, 2, 3, 4, 5};
        
        int b = c(a);
        System.out.println("Sum of the array elements: " + b);
    }
    
    public static int c(int[] d) {
        int b = 0;
        
        for (int i = 0; i < d.length; i++) {
            b += d[i];
        }
        
        return b;
    }
}
