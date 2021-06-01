/**
 * Copyright 2021 Steven Taylor McGown
 * Driver class for the Library java program for CSCE 247
 * This driver checks in books, checks them out, and makes use of the display function to list
 * the current inventory of the library. 
 */
package singletondesignpattern;

public class LibraryDriver {

	public void runLibrary() {
		Library library = Library.getInstance();
		
		System.out.println("\n*********Populating the library****************\n");
		
		//Populate initial library
		library.checkInBook("Anna Karenina", 1);
		library.checkInBook("Madame Bovary", 2);
		library.checkInBook("War and Peace", 4);
		library.checkInBook("The Great Gatsby", 3);
		library.checkInBook("Lolita", 1);
		library.checkInBook("Middlemarch", 1);
		library.checkInBook("The Adventures of Huckleberry Finn", 2);
		library.checkInBook("The Stories of Anton Chekhov", 1);
		library.checkInBook("In Search of Lost Time", 3);
		library.checkInBook("Hamlet", 1);
		
		System.out.println("\n*********Performing operations on the library****************\n");
		
		//checkout books
		library.checkoutBook("The Great Gatsby");
		library.checkoutBook("The Adventures of Huckleberry Finn");
		library.checkoutBook("The Adventures of Huckleberry Finn");
		library.checkoutBook("Anna Karenina");
		library.checkoutBook("Anna Karenina");
		library.checkInBook("In Search of Lost Time", 2);
		
		library.displayBooks();
		
	}

	
	public static void main(String[] args) {
		LibraryDriver lDriver = new LibraryDriver();
		lDriver.runLibrary();
		
		
	}
}
