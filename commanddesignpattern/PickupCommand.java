/**
 * This is the JumpCommand. It has the command for when the user wants a robot to jump.
 * @author wmamos
 */

package commanddesignpattern;

public class PickupCommand implements Command{
	
	/**
	 * Constructs a PickupCommand.
	 * @param robot The robot that we want to pick something up.
	 */
	public PickupCommand(Robot robot) {
		super();
	}
	
	/**
	 * Prints out the output for when a robot picks something up.
	 */
	public void execute() {
		System.out.println("Oh treasure, picking it up!");
	}
}
