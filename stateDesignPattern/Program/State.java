/**
 * Copyright 2021 Steven Taylor McGown
 * State interface for NetflixState, HuluState, and HomeState
 */
package Program;

public interface State {
    public void pressHomeButton();
    public void pressNetflixButton();
    public void pressMovieButton();
    public void pressHuluButton();
    public void pressTVButton();
}
