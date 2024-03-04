import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class XOR {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        boolean repeat = true;
        while (repeat) {
            System.out.print("Masukkan banyak angka: ");
            int n = in.nextInt();
            int a = 0;
            for (int i = 0; i < n; i++) {
                System.out.print("Masukkan angka: ");
                a ^= in.nextInt();
            }
            System.out.println("Hasil XOR dari "+n+" bilangan bulat tsb adalah: "+a);
            System.out.print("Ulangi lagi? (yes/no): ");
            String response = in.next();
            if (!response.equalsIgnoreCase("yes")) {
                repeat = false;
            }
        }
        System.out.println("END");
    }
}