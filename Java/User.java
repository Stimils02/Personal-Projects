import java.util.ArrayList;

public class User {
    // FIELDS
    private String username;
    private String password;
    private String name;
    private ArrayList<User> conversations;

    // CONSTRUCTORS
    public User(String username, String password) {
        this.username = username;
        this.password = password;
    }

    // METHODS
    public String getUsername() {
        return this.username;
    }

    public String getPassword() {
        return this.password;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }
}