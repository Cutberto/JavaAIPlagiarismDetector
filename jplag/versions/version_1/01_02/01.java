public class SumArray {
    public static void main(String[] args) {
        int[] array = {5, 2, 7, 3, 9};
        int sum = 0;
        
        for (int i = 0; i < array.length; i++) {
            sum += array[i];
        }
        
        System.out.println("Sum: " + sum);
    }
}
