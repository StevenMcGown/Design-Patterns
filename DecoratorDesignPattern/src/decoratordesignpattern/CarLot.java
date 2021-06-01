/**
 * Copyright 2021 Steven Taylor McGown
 * Driver for the Decorator Design Pattern program, Homework for CSCE 247 
 * Spring 2021
 */

package decoratordesignpattern;

import java.text.NumberFormat;
import java.util.Locale;
import decoratordesignpattern.*;
import CarType.*;
import Decoration.*;

public class CarLot {
		
	public CarLot() {}
	
	//Used in main loop
	public void play() {
		Vehicle sedan = new Sedan();
		sedan = new Paint(sedan);
		sedan = new Rims(sedan);
		
		Vehicle sportsCar = new SportsCar();
		sportsCar = new SoundSystem(sportsCar);
		sportsCar = new Paint(sportsCar);
		
		Vehicle compact = new Compact();
		compact = new Rims(compact);
		
		System.out.println("***** Cars ******");
		System.out.println(sedan + " costs " + getCurrency(sedan.getCost()));
		System.out.println(sportsCar + " costs " + getCurrency(sportsCar.getCost()));
		System.out.println(compact + " costs " + getCurrency(compact.getCost()));
	}
	
	/**
	 * @param amount Price of vechile & decorations previously defined
	 * @return USD value of amount
	 */
	public String getCurrency(double amount) {
		return NumberFormat.getCurrencyInstance(new Locale("en", "US")).format(amount);
	}

	public static void main(String[] args) {
		CarLot carLot = new CarLot();
		carLot.play();
	}
}
