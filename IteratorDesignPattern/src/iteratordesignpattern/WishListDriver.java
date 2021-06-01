/**
 * Copyright 2021 Steven McGown
 * Driver for the Iterator Design Pattern program for CSCE 247 Homework 4
 * Adds items to a wishlist and then prints them
 */

package iteratordesignpattern;

public class WishListDriver {
	public static void main(String[] args) {
		WishList myWishes = new WishList("Things to get me!");
		myWishes.addItem("Flowers", "Daiseys of all colors", 16.99);
		myWishes.addItem("Photo Album", "With pictures of me!", 7.99);
		myWishes.addItem("Ring", "Why don't I have one yet?", 500);
		myWishes.addItem("Chocolate", "The fancy kind", 20.99);
		myWishes.addItem("Birds", "The chirpy kind", 200);
		
		WishListIterator wishListIterator = myWishes.createIterator();
		
		System.out.println("Wish List:");
		while(wishListIterator.hasNext()) {
			Item item = wishListIterator.next();
			item.print();
		}
	}
}
