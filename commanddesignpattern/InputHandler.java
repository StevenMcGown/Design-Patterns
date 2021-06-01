package commanddesignpattern;

import java.util.HashMap;

/**
 * InputHandler handles the inputed commands for a robot.
 */
public class InputHandler {
    private HashMap<String, Command> commands;
    private Robot robot;

    /**
     * Construct an InputHandler. Puts the commands for a robot into a HashMap.
     * @param The robot that we are commanding.
     */
    public InputHandler(Robot robot) {
        commands = new HashMap<>();
    	commands.put("pickup", new PickupCommand(robot));
    	commands.put("jump", new JumpCommand(robot));
    	commands.put("fire", new FireCommand(robot));
    	commands.put("heal", new HealCommand(robot));
        this.robot = robot;
    }

    /**
     * Depending on the command entered by the user, that command is called.
     * @param data The command that the robot is to do next.
     */
    public void inputEntered(String data) {
    	switch (data) {
    		case "pickup":
    			robot.pickup();
    			break;
    		case "jump":
    			robot.jump();
    			break;
    		case "fire":
    			robot.fire();
    			break;
    		case "heal":
    			robot.heal();
    			break;
    	}
    }
}
