import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server2 {
    private boolean running;
    private int port;
    private ServerSocket serverSocket;

    public Server2(int port) throws IOException{
        this.port = port;
        serverSocket = new ServerSocket(port);
        running = false;
    }
    public void Start() {
        running = true;
        try {
            while (running) {
                Socket socket = serverSocket.accept();
                Thread user = new Thread(new GUIProcessor(socket));
                user.start();
            }
        } catch (IOException e) {
            e.printStackTrace(); //Handle exception better
        }
    }
    public void Stop() {
        running = false;
    }
}