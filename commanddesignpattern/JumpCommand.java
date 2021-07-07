/**
 * This is the JumpCommand. It has the command for when the user wants a robot to jump.
 * @author wmamos
 */

package commanddesignpattern;

public class JumpCommand implements Command{
	
	/**
	 * Constructs a JumpCommand.
	 * @param robot The robot that we want to jump.
	 */
	public JumpCommand(Robot robot) {
		super();
	}
	
	/**
	 * Prints the output for when a robot jumps.
	 */
	public void execute() {
		System.out.println("Oh no a hazard, I'm jumping over it.");
	}
}
