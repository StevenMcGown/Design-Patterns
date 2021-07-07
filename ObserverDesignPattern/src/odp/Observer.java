package odp;
/**
 * @author Steven Taylor McGown 2021
 * This interface specifies the role that the observer does; to update
 * the score of the golfers
 */
public interface Observer {
    public void update(int strokes, int par);
}