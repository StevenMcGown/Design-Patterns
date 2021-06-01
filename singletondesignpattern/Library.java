/**
 * Copyright 2021 Steven Taylor McGown
 * This class allows users to add books to an instantiated library object, check them out and
 * print the inventory of the library object. Hash maps are used to search for objects by key.
 */
package singletondesignpattern;

import java.util.HashMap;

public class Library {

	private HashMap<String,Integer> books = new HashMap<String,Integer>();
	private static Library library;

	// Constructor
	private Library() {}

	/**
	 * If there is not an instance of the library, a new one is created.
	 * @return library object
	 */
	public static Library getInstance() {
		if(library == null){
			System.out.println("Creating our Library. Time to begin reading");
			library = new Library();
		}
		return library;
	}

	/**
	 * Checks in books to the library. If there are no instances of the book, the
	 * system indicates that a new copy has been added. 
	 * @param string Key for the hashmap (name of the book)
	 * @param numToAdd number of copies of books added to the library
	 */
	public void checkInBook(String string, int numToAdd) {
		if(books.containsKey(string)) {
			System.out.println("A new copy of " + string + " was added to the library");
			books.put(string, numToAdd + books.get(string));
		} else {
			books.putIfAbsent(string, numToAdd);
			System.out.println(string + " was added to the library");
		}
	}

	/**
	 * Checks out books from the library. When this method is called, the hashmap is 
	 * queried to see if there are copies of books in the library. If this number
	 * is greater than zero, the number of books is decremented by 1 and the system
	 * indicates that the book has been checked out. If the book is not in stock, the
	 * system indicates the book is not in stock.
	 * @param string Key for the hashmap (name of the book)
	 * @return True or false (if book is in stock), indicated in UML diagram
	 */
	public boolean checkoutBook(String string) {
		if(books.get(string) > 0) {
			System.out.println(string + " was succesfully checked out");
			books.put(string, books.get(string) -1);
			return true;
		} else {
			System.out.println("Sorry, " + string + " is not in stock");
		}
		return false;
	}

	/**
	 * Prints the inventory of the library
	 */
	public void displayBooks() {
		System.out.println("\nInventory:");
		books.forEach((key,value) -> System.out.println("\t- " + key + ", copies: " + value));
	}
    
}
