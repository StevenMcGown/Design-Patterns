package odp;

/**
 * @author Steven Taylor McGown 2021
 * This class records the score for each hole for each golfer
 */
public class HoleScoreDisplay implements Observer {
    private Subject golfer;
    private int strokes;
    private int par;

    /**
     * Creates a display for the hole for each golfer
     * @param golfer The golfer whose score is being recorded
     */
    public HoleScoreDisplay(Subject golfer) {
        this.golfer = golfer;
        golfer.registerObserver(this);
    }

    /**
     * Updates the score for the hole
     * @param strokes The number of strokes taken
     * @param par The par of the hole
     */
    public void update(int strokes, int par) {
        this.strokes = strokes;
        this.par = par;
        displayCurrentScore();
    }

    /**
     * Prints the score for the hole. Returns whether or not the golfer was
     * on par, below par, or over par.
     */
    private void displayCurrentScore() {
        System.out.println("Current Hole stats: ");
        System.out.println("Par: " + par);
        System.out.println("Strokes: " + strokes);

        if(strokes > par) {
            System.out.println(strokes-par + " over par\n");
        } 
        else if (strokes < par) {
            System.out.println(par-strokes + " below par\n");
        }
        else {
            System.out.println("Made par\n");
        }
    }
}