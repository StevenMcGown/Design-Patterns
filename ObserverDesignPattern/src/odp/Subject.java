package odp;
/**
 * @author Steven Taylor McGown 2021
 * This interface specifies what roles the subject has to do; to register, 
 * remove and notify observers
 */
public interface Subject {
    public void registerObserver(Observer observer);
    public void removeObserver(Observer observer);
    public void notifyObservers(int strokes, int par);
}