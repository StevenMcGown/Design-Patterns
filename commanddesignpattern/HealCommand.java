/**
 * Class created to represent Heal Command
 * @author xslau
 */
package commanddesignpattern;

public class HealCommand implements Command{

    /**
     * Constructor: Intializes values based on associated class Robot
     * @param robot Robot Instance robot
     */
    public HealCommand(Robot robot){

        super(); 
    }
    
    /**
     * Prints String representation of Heal Command
     */
    @Override
    public void execute() {

        System.out.println("Thanks for healing my wounds"); 
        
    }
}
