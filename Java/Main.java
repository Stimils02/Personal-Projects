public class Main {

    public static void main(String[] args) {
        try {
            Server2 theServer = new Server2(4242);
            theServer.Start();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}