import java.util.Scanner;

public class 功成不必在我 {
    public static boolean 初心是好的 = true;
    public static String 嘿嘿嘿 = "我看看我这个小本本上有没有这个内容";
    public static String 结果 = "烂尾";

    public static String 不忘初心(String 任何事情, String 初心是好的吗) {
        System.out.println("我为" + 任何事情 + "指明方向");
        if (初心是好的吗.equals("是") || 初心是好的吗.equals("那当然")||初心是好的吗.equals("不忘初心")){
            初心是好的 = true;
        }else{
            初心是好的 = false;
        }

        if (初心是好的)
            return 结果;
        else {
            return 嘿嘿嘿;
        }
    }

    public static void main(String[] args) {
        while (初心是好的) {
            Scanner scanner = new Scanner(System.in);
            System.out.println("一拍脑袋,我要为");
            String 事情 = scanner.next();
            System.out.println("指明方向");
            System.out.println("初心是好的吗？");
            String 初心是好的吗 = scanner.next();
            System.out.println(事情 +", "+ 不忘初心(事情, 初心是好的吗));
            System.out.println("爽！\n");

        }
    }
}
