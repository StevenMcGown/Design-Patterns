/**
 * Copyright 2021 Steven Taylor McGown
 * The driver for CSCE 247 Homework #4 - Factory Design Pattern
 * Creates bike objects and manages them
 */

package factorydesignpattern;

public class BikeStoreDriver {

	public void runBikeStore() {
		
		/**
		 * Formats double values into USD
		 */
		java.util.Currency usd = java.util.Currency.getInstance("USD");
		java.text.NumberFormat format = java.text.NumberFormat.getCurrencyInstance(java.util.Locale.US);
		format.setCurrency(usd);

		BikeStore bikeStore = new BikeStore();

		/**
		 * Creating instances of each type of bike. Prices are formatted in USD
		 */
		Bike tricycle = bikeStore.orderBike("tricycle");
		tricycle.createBike();
		System.out.println("Price: " + format.format(tricycle.getPrice()));
		System.out.println("\n-----------------------------------\n");

		Bike strider = bikeStore.orderBike("strider");
		strider.createBike();
		System.out.println("Price: " + format.format(strider.getPrice()));
		System.out.println("\n-----------------------------------\n");

		
		Bike kidsBike = bikeStore.orderBike("kids bike");
		kidsBike.createBike();
		System.out.println("Price: " + format.format(kidsBike.getPrice()));
		System.out.println("\n-----------------------------------\n");

	}
	// Main method
	public static void main(String[] args) {
		BikeStoreDriver driver = new BikeStoreDriver();
		driver.runBikeStore();
	}

}
