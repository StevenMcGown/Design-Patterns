/**
 * Robot class to execute robot commands
 * @author StevenMcGown
 */

package commanddesignpattern;

 public class Robot {
    /**
     * Instantiates a Robot object
     * @param name Name of the robot
     */
    public Robot(String name) {
      System.out.println("Welcome, my name is " + name + ", I'm a friendly robot");
    }

    /**
     * Calls the pick up command
     */
    public void pickUp() {
		new PickupCommand(this).execute();
    }
    /**
     * Calls the jump command
     */
    public void jump() {
    	new JumpCommand(this).execute();
    }
    /**
     * Calls the fire command
     */
    public void fire() {
    	new FireCommand(this).execute();;
    }
    /**
     * Calls the heal command
     */
    public void heal() {
    	new HealCommand(this).execute();
    }

 }
