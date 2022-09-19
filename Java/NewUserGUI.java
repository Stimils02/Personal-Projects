import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class NewUserGUI extends JComponent implements Runnable {
    JTextField userField;
    JTextField passField;
    JTextField confPassField;
    JLabel userText;
    JLabel passText;
    JLabel confPassText;
    JButton enter;
    JButton cancel;
    NewUserGUI newUserGUI;
    JFrame frame;
    ActionListener actionListener = new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e) {
            if (e.getSource() == enter) {
                boolean verified = VerifyNewUserInput(userField.getText(), passField.getText(), confPassField.getText());
                if (verified) {
                    Client2.writer.write(userField.getText());
                    Client2.writer.println();
                    Client2.writer.flush();
                   Client2.writer.write(passField.getText());
                   Client2.writer.println();
                   Client2.writer.flush();
                   Client2.writer.write(confPassField.getText());
                   Client2.writer.println();
                   Client2.writer.flush();
                    frame.dispose();
                }
            } else if (e.getSource() == cancel) {
                for (int x = 0; x < 3; x++) {
                   Client2.writer.write("cancel");
                   Client2.writer.println();
                   Client2.writer.flush();
                }
                frame.dispose();
            }
        }
    };
    public void run() {
        frame = new JFrame("Campuswire2.0 NewUser Creation");
        Container content = frame.getContentPane();
        content.setLayout(new GridLayout(4, 2));
        newUserGUI = new NewUserGUI();
        content.add(newUserGUI);
        frame.setSize(350, 500);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

        userField = new JTextField(15);
        passField = new JTextField(15);
        confPassField = new JTextField(15);
        userText = new JLabel("New Username:");
        passText = new JLabel("New Password:");
        confPassText = new JLabel("Confirm Password:");
        confPassField = new JTextField(15);
        enter = new JButton("Enter");
        cancel = new JButton("Cancel");
        JPanel panel = new JPanel();
        panel.add(userText);
        panel.add(userField);
        panel.add(passText);
        panel.add(passField);
        panel.add(confPassText);
        panel.add(confPassField);
        panel.add(enter);
        panel.add(cancel);
        content.add(panel);
        enter.addActionListener(actionListener);
        cancel.addActionListener(actionListener);

        SwingUtilities.updateComponentTreeUI(frame);
    }
    public boolean VerifyNewUserInput(String user, String pass, String confPass) {
        if(user.equals("") || pass.equals("") || confPass.equals("")) {
            JOptionPane.showMessageDialog(null, "Please fill in " +
                    "all fields.", "Campuswire2", JOptionPane.WARNING_MESSAGE);
            return false;
        } else if (!pass.equals(confPass)) {
            JOptionPane.showMessageDialog(null, "Passwords " +
                    "must match.", "Campuswire2", JOptionPane.WARNING_MESSAGE);
            return false;
        } else if (pass.toLowerCase().equals(pass) || !ContainsNumber(pass) || pass.length() < 5) {
            JOptionPane.showMessageDialog(null, "Password must be at least 5 " +
                    "characters, and must contain at least one " +
                    "capital letter and number.", "Campuswire2", JOptionPane.WARNING_MESSAGE);
            return false;
        }
        return true;
    }
    public boolean ContainsNumber(String q) {
        if (q.contains("0") || q.contains("1")|| q.contains("2")|| q.contains("3")|| q.contains("4")) {
            return true;
        } else if (q.contains("5") || q.contains("6")|| q.contains("7")|| q.contains("8")|| q.contains("9")) {
            return true;
        }
        return false;
    }
}
