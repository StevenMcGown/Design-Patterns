/**
 * Copyright 2021 Steven Taylor McGown
 * Hulu State class implements the state interface to be used by TV.java
 */
package States;

import Program.State;
import Program.TV;

public class HuluState implements State {

    private TV tv;

    //Default constructor
    public HuluState(TV tv) {
        this.tv = tv;
    }

    //Runs when user selects the home button
    @Override
    public void pressHomeButton() {
        tv.setState(tv.getHomeState());
    }

    //Runs when user selects the Netflix button
    @Override
    public void pressNetflixButton() {
        tv.setState(tv.getNetflixState());
    }

    /**
     * Runs when user selects the movie button
     * Displays hulu movies
     */
    @Override
    public void pressMovieButton() {
        System.out.println("Hulu movies");
        System.out.println("- sesame street\n- care bears\n- loney tunes\n");
    }

    //Runs when user selects the Hulu button
    @Override
    public void pressHuluButton() {
        System.out.println("Loading Hulu...\n");
        tv.setState(tv.getHuluState());
    }
    
    /**
     * Runs when user selects the TV button
     * Displays hulu tv shows
     */
    @Override
    public void pressTVButton() {
        System.out.println("Hulu Tv shows");
        System.out.println("- Cars\n- Cinderella\n- Wall-E\n- ET\n");
    }
}
