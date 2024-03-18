public class sesliHarf {
    public static void main(String[] args) {
        char harf ='K';

        switch (harf){
            case 'A':
            case 'O':
            case 'I':
            case 'U':
                System.out.println("Kalın Sesli Harf");
                break;
            case 'E':
            case 'Ö':
            case 'İ':
            case 'Ü':
                System.out.println("İnce Sesli Harf");
                break;
            default:
                System.out.println("Harf, Sesli Harf Değil");

        }

    }
}
