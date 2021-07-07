/**
 * Copyright 2021 Steven McGown
 * WishListIterator.java: Iterates through a WishList object. Checks to see if there
 * is another item next on the wishlist and prints it.
 */
package iteratordesignpattern;

import java.util.Iterator;

public class WishListIterator implements Iterator {
    // Objects in wishlist
    private Item[] items;
    private int position = 0;

    // WishListIterator constructor
    public WishListIterator(Item[] items) {
        this.items = items;
    }

    /**
     * Increments the position of the wishlist
     */
    public Item next() {
        if(hasNext()) {
            Item wishListItem = items[position];
            position += 1;
            return wishListItem;
        }
        return null;
    }

    /**
     * If there is another element in the wishlist and then return true
     */
    public boolean hasNext() {
        if(position >= items.length || items[position] == null) {
            return false;
        } else {
            return true;
        }
    }
}
