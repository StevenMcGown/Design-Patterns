/**
 * Copyright 2021 Steven Taylor McGown
 * Netflix State class implements the state interface to be used by TV.java
 */
package States;

import Program.State;
import Program.TV;

public class NetflixState implements State {
    
    private TV tv;

    //Default constructor
    public NetflixState(TV tv) {
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
        System.out.println("TV is already on Netflix\n");
        tv.setState(tv.getNetflixState());
    }

    /**
     * Runs when user selects the Movie button
     * Displays netflix movies
     */
    @Override
    public void pressMovieButton() {
        System.out.println("Netflix movies:");
        System.out.println("- The Land Before Time\n- Frozen\n- The Little Mermaid\n- Ice Age\n");
    }

    //Runs when user selects the Hulu button
    @Override
    public void pressHuluButton() {
        System.out.println("Loading Hulu...\n");
        tv.setState(tv.getHuluState());
    }
    
    /**
     * Runs when user selects the TV button
     * Displays netflix tv shows
     */
    @Override
    public void pressTVButton() {
        System.out.println("Netflix tv shows:");
        System.out.println("- Peppa Pig\n- My Little Pony\n- Garfield\n- Teenage Mutant Ninja Turtles\n");
    }
}
