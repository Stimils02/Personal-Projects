import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;


public class Test {

    private String username;
    private String password;

    public Test(String username, String password) {
        this.username = username;
        this.password = password;
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }


    public void saveToFile() {
        String username = getUsername();
        String password = getPassword();
        File output = new File("Info.txt");
        try {
            BufferedWriter bw = new BufferedWriter(new FileWriter(output));
            bw.write(String.format("Username: %s, Password: %s", username, password));

            bw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {



    }
}
