public class mukemmelSayi {
    public static void main(String[] args) {
        // sayının bölenlerinin toplamı yine sayıyı veren sayılar
        // 6 -> 1+2+3 = 6

        int number = 28;
        int total = 0;

        for (int i=1;i<number;i++){
            if (number % i == 0){
                total = total +i;
            }
        }
        if (total == number){
            System.out.println(number+" bir mükemmel sayıdır");
        }
        else{
            System.out.println(number + " bir mükemmel sayı değildir");
        }
    }
}
