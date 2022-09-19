import javax.swing.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Client2 implements Runnable{
    public static BufferedReader reader;
    public static  PrintWriter writer;
    public void run() {
        Socket socket;
        try {
            socket = new Socket("localhost", 4242);
            reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            writer = new PrintWriter(socket.getOutputStream());
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Error: unsuccessful connection. " +
                    "The program will now exit.", "Campuswire2", JOptionPane.ERROR_MESSAGE);
        }
        boolean loggedIn = false;
        while (!loggedIn) {
            LoginGUI login = new LoginGUI();
            login.run();
            String serverResponse = GetFromServer();
            if (serverResponse.equals("Yes")) {
                loggedIn = true;
            }
            else if (serverResponse.equals("PW")) {
                JOptionPane.showMessageDialog(null, "Incorrect Password. " +
                        "Please try again.", "Campuswire2", JOptionPane.WARNING_MESSAGE);
            }
            else if (serverResponse.equals("NoAcc")) {
                JOptionPane.showMessageDialog(null, "Username Not Found. " +
                        "Please try again.", "Campuswire2", JOptionPane.WARNING_MESSAGE);
            }
            else if (serverResponse.equals("NewAcc")) {
                boolean endNewAccScreen = false;
                while (!endNewAccScreen) {
                    NewUserGUI createAccount = new NewUserGUI();
                    createAccount.run();
                    serverResponse = GetFromServer();
                    if (serverResponse.equals("UserExists")) {
                        JOptionPane.showMessageDialog(null, "Username is already " +
                                "in use. Please use a different username", "Campuswire2", JOptionPane.WARNING_MESSAGE);
                    } else if (serverResponse.equals("Yes"))
                    {
                        JOptionPane.showMessageDialog(null, "Account creation " +
                                "successful!", "Campuswire2", JOptionPane.INFORMATION_MESSAGE);
                        endNewAccScreen = true;
                    } else if (serverResponse.equals("cancelNewUser"))
                    {
                        endNewAccScreen = true;
                    }
                }
            }
        }
    }
    public static void main(String[] args) {
        Thread thisClient = new Thread(new Client2());
        thisClient.start();
    }
    public void SendToServer(String message) {
        writer.write(message);
        writer.println();
        writer.flush();
    }
    public String GetFromServer() {
        try {
            return reader.readLine();
        } catch (Exception e) {
            return "";
        }
    }
}
