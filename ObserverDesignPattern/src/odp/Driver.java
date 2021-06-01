/**
 * @author Steven Taylor McGown 2021
 * This program is assignment for CSCE 247 for the spring semester of 2021 at USC.
 * Golfers are instantiated to which scores are given and recorded by observers.
 * 
 */
package odp;

public class Driver {

	public static void main(String[] args) {

		Golfer georgy = new Golfer("Georgy");
		Observer HoleScoreDisplay = new HoleScoreDisplay(georgy);
		Observer RoundScoreDisplay = new RoundScoreDisplay(georgy);

		
		System.out.println("***** " + georgy.getName() + " is starting his round *****");
		georgy.enterScore(5, 3);
		georgy.enterScore(2, 2);
		georgy.enterScore(1, 3);
		georgy.enterScore(3, 3);
		georgy.enterScore(3, 2);
	}
}
