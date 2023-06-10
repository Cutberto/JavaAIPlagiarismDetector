public class Crc {
    private double a;
    
    public Crc(double b) {
        this.a = b;
    }
    
    public double c() {
        return a;
    }
    
    public double d() {
        return Math.PI * a * a;
    }
    
    public double e() {
        return 2 * Math.PI * a;
    }
    
    public static void main(String[] args) {
        Crc f = new Crc(5.0);
        System.out.println("Radius: " + f.c());
        System.out.println("Area: " + f.d());
        System.out.println("Circumference: " + f.e());
    }
}
