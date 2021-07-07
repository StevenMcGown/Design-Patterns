/**
 * Class created to represent Fire Command
 * @author Xzavian Slaughter
 */

package commanddesignpattern;

public class FireCommand implements Command{

    /**
     * Constructor: Initialzies value based on associated class Robot
     * @param robot Robot Instance robot
     */
    public FireCommand(Robot robot) {

        super(); 

    }

    /**
     * Prints string representation of Fire Command
     */
    @Override
    public void execute() {

        System.out.println("Bad guys! Fire my blow torch at them"); 

    }
    
}
