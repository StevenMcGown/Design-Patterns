/**
 * Copyright 2021 Steven Taylor McGown
 * Driver for the State Design Pattern
 */
package Program;

public class Driver {
	public void runTV() {
		TV tv = new TV();
		tv.pressHomeButton();
		tv.pressNetflixButton();
		tv.pressMovieButton();
		tv.pressTVButton();
		tv.pressHuluButton();
		tv.pressMovieButton();
		tv.pressTVButton();
		tv.pressHomeButton();
	}
	
	public static void main(String[] args) {
		Driver tvDriver = new Driver();
		tvDriver.runTV();
	}
}
