/**
 * Copyright 2021 Steven McGown
 * WishList.java: Creates a wishlist object that makes uses of the WishListIterator file.
 * Items can be added to the list and the total price of all objects can be returned.
 */

package iteratordesignpattern;

public class WishList {

    private String name;
    private Item[] items = {};
    private int count;

    /**
     * Wishlist constructor
     * @param name The given name of the wishlist
     */
    public WishList(String name) {
        this.name = name;
    }

    /**
     * Adds item to the wishlist, makes use of the growArray() function
     * 
     * @param title Title of the item, will be surrounded in ****Asterisks****
     * @param description Describes the item added to the wishlist
     * @param price double value price of the wishlist item
     */
    public void addItem(String title, String description, double price) {
        Item i = new Item(title, description, price);
        items = growArray(items);
        items[items.length-1] = i;
        //System.out.println
    }

    /**
     * Overloaded addItem method allows for int price instead of double price
     * Adds item to the wishlist, makes use of the growArray() function
     * 
     * @param title Title of the item, will be surrounded in ****Asterisks****
     * @param description Describes the item added to the wishlist
     * @param price Integer value price of the wishlist item
     */
    public void addItem(String title, String description, int price) {
        Item i = new Item(title, description, price);
        items = growArray(items);
        items[items.length-1] = i;
    }

    /**
     * Creates an iterator to cycle through the wishlist
     * @return WishListIterator object
     */
    public WishListIterator createIterator() {
        return new WishListIterator(items);
    }

    /**
     * Returns the price of all of the items on the wishlist
     * @return Total price summation
     */
    public double getTotalCost() {
        double price = 0;
        for(Item i : items) {
            price += i.getPrice();
        }
        return price;
    }

    /**
     * Increases the size of the items array by 1 so a new item can be added to
     * the WishList
     * @param items The items in the items array which will act as a wish list
     * @return returns an array 1 index larger than given
     */
    private Item[] growArray(Item[] items) {
        // Empty array handling
        if(items.length == 0) {
            count++;
            return new Item[1];
        } else {
            //Create new array with extra index, put all element of old array in new one
            Item[] newArray = new Item[count + 1];
            for(int i = 0; i < items.length; i++) {
                newArray[i] = items[i];
            }
            count++;
            return newArray;
        }
    }
}
