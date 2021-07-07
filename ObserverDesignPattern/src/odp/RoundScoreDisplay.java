package odp;

/**
 * @author Steven Taylor McGown 2021
 * This class records the score for the round for each golfer
 */
public class RoundScoreDisplay implements Observer {
    private Subject golfer;
    private int strokesTotal;
    private int parTotal;

    /**
     * Creates a display for the round for each golfer
     * @param golfer The golfer whose score is being recorded
     */
    public RoundScoreDisplay(Subject golfer) {
        this.golfer = golfer;
        golfer.registerObserver(this);
    }

    /**
     * Updates the score for the whole golfing round
     * @param strokes The number of strokes taken
     * @param par The par total of the round
     */
    public void update(int strokes, int par) {
        strokesTotal += strokes;
        parTotal += par;
        displayRoundScore();
    }

    /**
     * Prints the score for the round. Returns whether or not the golfer was
     * on par, below par, or over par.
     */
    public void displayRoundScore() {

        System.out.println("Round stats: ");
        System.out.println("Par: " + parTotal);
        System.out.println("Strokes: " + strokesTotal);

        if(strokesTotal > parTotal) {
            System.out.println(strokesTotal-parTotal + " over par\n");
        } 
        else if (strokesTotal < parTotal) {
            System.out.println(parTotal-strokesTotal + " under par\n");
        }
        else {
            System.out.println("Making par\n");
        }
    }
}