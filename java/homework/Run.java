class Make{
    int a;
    Make(int a){
        this.a = a;
    }
}
public class Run{
    public static void main(String[] args) {
        String s1 = "Welcome to Java";
        String s2 = s1;
        String s3 = new String("Welcome to Java");

        boolean out;
        out = s1 == s2;
        out = s1 == s3;
        s1.equals(s2);
        s2.equals(s3);
        s1.compareTo(s2);
        s2.compareTo(s3);

        System.out.println(s1.charAt(0));
        System.out.println(s1.indexOf('j'));
        System.out.println(s1.indexOf("to"));
        System.out.println(s1.lastIndexOf("o",15));
        System.out.println(s1.substring(3, 11));
        System.out.println(s1.endsWith("Java"));
        System.out.println(s1.startsWith("wel"));
        System.out.println("   We come  ".trim());
        System.out.println(s1.toUpperCase());
        System.out.println(s1.replace('o', 'T'));

        System.out.println(out);
        Make make1 = new Make(12);
        Make make2 = make1;
        System.out.println(make2 == make1);
    }
}
