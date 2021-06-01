/**
 * Copyright 2021 Steven McGown
 * Item.java: Item object to be added to a wishlist
 */

package iteratordesignpattern;

public class Item {
    // Each item gets a title, description and price attribute
    private String title;
    private String description;
    private Double price;

    /**
     * Item constructor
     * @param title Title of the item, will be surrounded in ****Asterisks****
     * @param description Describes the item added to the wishlist
     * @param price double value price of the wishlist item
     */
    public Item(String title, String description, Double price) {
        this.title = title;
        this.description = description;
        this.price = price;
    }

    /**
     * Item constrcutor overloaded to accept int parameters.
     * @param title Title of the item, will be surrounded in ****Asterisks****
     * @param description Describes the item added to the wishlist
     * @param price double value price of the wishlist item
     */
    public Item(String title, String description, int price) {
        this.title = title;
        this.description = description;
        this.price = Double.valueOf(price);
    }

    /**
     * Returns the item in string form to be printed
     * @return Item to string
     */
    public String toString() {
        return "***** "+ title + " *****\n" + description + "\n" + "$" + price + "\n";
    }

    /**
     * Returns the price of the item
     * @return Price of item
     */
    public Double getPrice() {
        return price;
    }

    /**
     * Prints the string value of the item
     */
    public void print() {
        System.out.println(this.toString());
    }
}
