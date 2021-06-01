package commanddesignpattern;

import java.util.Scanner;

public class RobotDriver {
	
	public void runDocumentDriver() {
		Scanner in = new Scanner(System.in);

		String robotName = getInputLine("Enter robots name", in);
		Robot robot = new Robot(robotName);
		InputHandler inHandler = new InputHandler(robot);

		while(true) {
			String command = getInputLine("Enter Command", in);
			if(command.contentEquals("quit"))break;
			inHandler.inputEntered(command);
		}
		
		System.out.println("Goodbye");
	}
	
	private String getInputLine(String prompt, Scanner in) {
		System.out.print(prompt + ": ");
		return in.nextLine().toLowerCase().trim();
	}
	
	public static void main(String[] args) {
		RobotDriver dDriver = new RobotDriver();
		dDriver.runDocumentDriver();
	}
}
