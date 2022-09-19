import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class LoginGUI extends JComponent implements Runnable {
    JButton newAccount;
    JLabel userText;
    JTextField userField;
    JLabel passText;
    JTextField passField;
    JButton enter;
    JLabel space;
    LoginGUI loginGUI;
    JFrame login;
    ActionListener actionListener = new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e) {
            if(e.getSource() == newAccount) {
                Client2.writer.write("NewAcc");
                Client2.writer.println();
                Client2.writer.flush();
                login.dispose();
            }
            if (e.getSource() == enter) {
                boolean ableToSend = VerifyLoginInput(userField.getText(), passField.getText());
                //Send to server if output valid
                if (ableToSend) {
                    Client2.writer.write("login");
                    Client2.writer.println();
                    Client2.writer.flush();
                    Client2.writer.write(userField.getText());
                    Client2.writer.println();
                    Client2.writer.flush();
                    Client2.writer.write(passField.getText());
                    Client2.writer.println();
                    Client2.writer.flush();
                    login.dispose();
                }
            }
        }
    };
    public void run() {
        login = new JFrame("Campuswire2.0 Login Screen");
        Container content = login.getContentPane();
        content.setLayout(new GridLayout(4, 2));
        loginGUI = new LoginGUI();
        content.add(loginGUI);
        login.setSize(350, 500);
        login.setLocationRelativeTo(null);
        login.setVisible(true);
        login.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

        newAccount = new JButton("Make New Account");
        userField = new JTextField(15);
        userText = new JLabel("Enter Username:");
        passField = new JTextField(15);
        passText = new JLabel("Enter Password:");
        enter = new JButton("Enter");
        space = new JLabel("");
        JPanel panel = new JPanel();
        panel.add(space);
        panel.add(userText);
        panel.add(userField);
        panel.add(passText);
        panel.add(passField);
        panel.add(enter);
        panel.add(newAccount);
        panel.add(space);
        content.add(panel);
        newAccount.addActionListener(actionListener);
        enter.addActionListener(actionListener);
        SwingUtilities.updateComponentTreeUI(login);
    }
    public boolean VerifyLoginInput(String user, String pass) {
        if(user.equals("") || pass.equals("")) {
            JOptionPane.showMessageDialog(null, "Please fill in " +
                    "all fields.", "Campuswire2", JOptionPane.WARNING_MESSAGE);
            return false;
        }
        return true;
    }
}
