/**
 * Copyright 2021 Steven Taylor McGown
 * This is the abstract class for the vehicle object. This class can create any vehicle object
 * with a defined description and cost.
 */

package decoratordesignpattern;

public abstract class Vehicle {
    protected String description;

    /**
     * @return The defined description of the Vehicle object defined from inherited class
     */
    public String toString() {
        return this.description;
    }

    /**
     * @return The cost of the Vehicle object defined from inherited class
     */
    public abstract double getCost();
}
