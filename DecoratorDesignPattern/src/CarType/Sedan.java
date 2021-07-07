/**
 * Copyright 2021 Steven Taylor McGown
 * This class defines Sedan Vehicle attributes to be charged and described on
 * its corresponding Vehicle object
 */
package CarType;

import decoratordesignpattern.Vehicle;

public class Sedan extends Vehicle {
    /**
     * Constructor
     */
    public Sedan() {
        this.description = "Sedan";
    }
    /**
     * @return Cost of Sedan
     */
    public double getCost() {
        return 20000;
    }
}
