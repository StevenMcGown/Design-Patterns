/**
 * Copyright 2021 Steven Taylor McGown
 * Home State class implements the state interface to be used by TV.java
 */
package States;

import Program.State;
import Program.TV;

public class HomeState implements State {
    
    private TV tv;

    //Default constructor
    public HomeState(TV tv) {
        this.tv = tv;
    }

    //Runs when user selects the home button
    @Override
    public void pressHomeButton() {
        System.out.println("TV is already on the home screen\n");
        tv.setState(tv.getHomeState());
    }

    //Runs when user selects the Netflix button
    @Override
    public void pressNetflixButton() {
        System.out.println("Loading Netflix...\n");
        tv.setState(tv.getNetflixState());
    }

    /**
     * Runs when user selects the Movie button
     * Displays home movies
     */
    @Override
    public void pressMovieButton() {
        System.out.println("Home movies");
    }

    //Runs when user selects the Hulu button
    @Override
    public void pressHuluButton() {
        System.out.println("Loading Hulu...");
        tv.setState(tv.getHuluState());

    }
    
    /**
     * Runs when user selects the TV button
     * Displays home tv shows
     */
    @Override
    public void pressTVButton() {
        System.out.println("Home TV shows");
    }
}
