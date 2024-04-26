package day03;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing04 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing04 frame = new MySwing04();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 226, 330);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("출력단수");
		lbl.setBounds(35, 22, 60, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(113, 19, 60, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(35, 47, 138, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(35, 80, 138, 184);
		contentPane.add(ta);
	}
	void myclick() {
		String dan = tf.getText();
		int idan = Integer.parseInt(dan);
		
		String txt = "";
		
		for(int i=1;i<=9;i++) {
			txt += idan+"*"+i+"="+(idan*i)+"\n";
		}
		
		ta.setText(txt);
	}
}












