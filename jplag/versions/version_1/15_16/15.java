public class ArraySum {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5};
        
        int sum = calculateSum(array);
        System.out.println("Sum of the array elements: " + sum);
    }
    
    public static int calculateSum(int[] arr) {
        int sum = 0;
        
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        
        return sum;
    }
}
