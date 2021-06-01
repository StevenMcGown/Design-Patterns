/**
 * Copyright 2021 Steven Taylor McGown
 * Makes use of all state classes by switching between them when called
 */

package Program;

import States.HomeState;
import States.HuluState;
import States.NetflixState;

public class TV {

   private State homeState;
   private State netflixState;
   private State huluState;

   private State state;

   //Default constructor
   public TV() {
      homeState = new HomeState(this);
      netflixState = new NetflixState(this);
      huluState = new HuluState(this);

      state = homeState;

   }
   
   //Runs when user selects the home button
   public void pressHomeButton() {
      state.pressHomeButton();
   }

   //Runs when user selects the Netflix button
   public void pressNetflixButton() {
      state.pressNetflixButton();
   }

   //Runs when user selects the Movie button
   public void pressMovieButton() {
      state.pressMovieButton();
   }

   //Runs when user selects the Hulu button
   public void pressHuluButton() {
      state.pressHuluButton();
   }
   
   //Runs when user selects the TV button
   public void pressTVButton() {
      state.pressTVButton();
   }

   //Sets the state of the TV
   public void setState(State state) {
      this.state = state;
   }
   /**
    * Gets the home state
    * @return Home state
    */
   public State getHomeState() {
      return homeState;
   }

   /**
    * Gets the netflix state
    * @return Netflix state
    */
   public State getNetflixState() {
      return netflixState;
   }

   /**
    * Gets the hulu state
    * @return Hulu state
    */
   public State getHuluState() {
      return huluState;
   }
}
