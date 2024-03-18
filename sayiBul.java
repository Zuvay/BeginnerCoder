public class sayiBul {
    public static void main(String[] args) {
        int [] sayilar = {1,2,3,4,55,6,7,8,9,12};
        int aranacakSayi = 53;
        boolean isFind = false;
        
        // Yöntem 1
        for (int i=0;i<sayilar.length;i++){
            if (i == aranacakSayi){
                isFind = true;
                break;
            }
        }
        if (isFind){
        System.out.println("Sayı bulundu, aranan sayıi: "+aranacakSayi);
        }
        else{
            System.out.println("Sayı bulunamadı");
        }    
        System.out.println("***************************************");

        //Yöntem 2
        for (int i : sayilar){
            if (i == aranacakSayi){
                isFind = true;
                break;
            }
        }
        if (isFind){
            System.out.println("Sayı bulundu, aranan sayıi: "+aranacakSayi);
            }
        else{
            System.out.println("Sayı bulunamadı");
        }    
    }
}
