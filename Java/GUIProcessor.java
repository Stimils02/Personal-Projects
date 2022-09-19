import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.ArrayList;

public class GUIProcessor implements Runnable {
    public static ArrayList<User> users = new ArrayList<>();
    private BufferedReader reader;
    private PrintWriter writer;
    private Socket socket;

    public GUIProcessor(Socket serverSocket) throws IOException {
        socket = serverSocket;
        reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        writer = new PrintWriter(socket.getOutputStream());
    }

    public void run() {
        boolean loggedIn = false;
        String username;
        String password;;
        String password2;
        String response;
        while (!loggedIn) {
            try {
                String actionType = getInputFromClient();
                response = "";
                if (actionType.equals("login")) {
                    response = "NoAcc";
                    username = getInputFromClient();
                    password = getInputFromClient();
                    for (int x = 0; x < users.size(); x++) {
                        if (users.get(x).getUsername().equals(username)) {
                            if (users.get(x).getPassword().equals(password)) {
                                //user exists and password matches
                                response = "Yes";
                                loggedIn = true;
                            } else {
                                //user exists but password is invalid
                                response = "PW";
                            }
                            break;
                        }
                        //user does not exist
                        response = "NoAcc";
                    }
                    sendOutputToClient(response);
                }
                else if (actionType.equals("NewAcc")) {
                    sendOutputToClient("NewAcc");
                    boolean inNewAcc = true;
                    while (inNewAcc) {
                        username = getInputFromClient();
                        password = getInputFromClient();
                        password2 = getInputFromClient();
                        response = "Yes";
                        if (username.equals("cancel") && password.equals("cancel") && password2.equals("cancel")) {
                            response = "cancelNewUser";
                            inNewAcc = false;
                        } else {
                            for (int x = 0; x < users.size(); x++) {
                                if (users.get(x).getUsername().equals(username)) {
                                    //Functionalities.User already exists/name is taken
                                    response = "UserExists";
                                    break;
                                }
                                //user does not exist
                                response = "Yes";
                            }
                            if (response.equals("Yes")) {
                                users.add(new User(username, password));
                                inNewAcc = false;
                            }
                        }
                        sendOutputToClient(response);
                    }
                }
            } catch (Exception e) {
                return;
            }
        }
        //logged in stuff HERE
        System.out.println("Login Success");

    }
    public void sendOutputToClient(String toSend) {
        writer.write(toSend);
        writer.println();
        writer.flush();
    }
    public String getInputFromClient() throws IOException{
        return reader.readLine();
    }
}
