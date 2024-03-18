public class arkadasSayi {
    public static void main(String[] args) {
        //220-284 bir sayının bölenlerinin toplamı diğer sayıya eşit. 220nin bölenleri toplamı 284, 284 bölenleri toplamı 220

        int sayi1 = 220;
        int sayi2 = 284;

        int sayi1bolenler = 0;
        int sayi2bolenler = 0;

        for (int i=1;i<sayi1;i++){
            if (sayi1 % i == 0){
                sayi1bolenler = sayi1bolenler + i;
            }
        }

        for (int i=1;i<sayi2;i++){
            if (sayi2 % i == 0){
                sayi2bolenler = sayi2bolenler + i;
            }
        }

        if (sayi1 == sayi2bolenler && sayi2 == sayi1bolenler){
            System.out.println(sayi1 + " ve " + sayi2 + " kardeş sayılardır.");
        }
        else{
            System.out.println(sayi1 + " ve " + sayi2 + " kardeş sayıl değiller.");
        }
    }
}
