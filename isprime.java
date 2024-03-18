public class isprime {
    // returns false or true
    public static void main(String[] args) {
        int number = 14;
        boolean isPrime = true;        
      
         if (number <=1){
             isPrime = false;
             System.out.println(isPrime);
             return;
         }
         else if (number == 2){
             System.out.println(isPrime);
             return;
        }
        
        for (int i=2;i<number;i++){
            if (number % i == 0){
                isPrime = false;
                System.out.println(isPrime);
                break;
            }
        }

    }
}
