package day03;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.SwingConstants;

public class MySwing07 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing07 frame = new MySwing07();
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
	public MySwing07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 192, 266);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setBounds(12, 26, 148, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn1 = new JButton("1");
		btn1.setBounds(12, 57, 43, 23);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.setBounds(62, 57, 43, 23);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.setBounds(117, 57, 43, 23);
		contentPane.add(btn3);
		
		JButton btn4 = new JButton("4");
		btn4.setBounds(12, 90, 43, 23);
		contentPane.add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.setBounds(62, 90, 43, 23);
		contentPane.add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.setBounds(117, 90, 43, 23);
		contentPane.add(btn6);
		
		JButton btn7 = new JButton("7");
		btn7.setBounds(12, 123, 43, 23);
		contentPane.add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.setBounds(62, 123, 43, 23);
		contentPane.add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.setBounds(117, 123, 43, 23);
		contentPane.add(btn9);
		
		JButton btn0 = new JButton("0");
		btn0.setBounds(12, 156, 43, 23);
		contentPane.add(btn0);
		
		JButton btn_call = new JButton("CALL");
		btn_call.setBounds(62, 156, 98, 23);
		contentPane.add(btn_call);
		
		
		btn1.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn2.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn3.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn4.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn5.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn6.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn7.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn8.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn9.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn0.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		
		btn_call.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { mycall(); } });
		
		

	}
	
	void mycall() {
		String str_tel = tf.getText();
		JOptionPane.showMessageDialog(this, "calling\n"+str_tel);
	}
	
	void myclick(MouseEvent e) {
		JButton o = (JButton) e.getSource();
		String str_new = o.getText();
		String str_old = tf.getText();
		
		tf.setText(str_old+str_new);
		
	}
	
	

}









