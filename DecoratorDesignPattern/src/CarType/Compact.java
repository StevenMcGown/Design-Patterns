/**
 * Copyright 2021 Steven Taylor McGown
 * This class defines Compact Vehicle attributes to be charged and described on
 * its corresponding Vehicle object
 */
package CarType;

import decoratordesignpattern.Vehicle;

public class Compact extends Vehicle {
    /**
     * Constructor
     */
    public Compact() {
        this.description = "Compact car";
    }
    /**
     * @return Cost of compact car
     */
    public double getCost() {
        return 15000;
    }
}
