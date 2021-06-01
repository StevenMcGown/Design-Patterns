/**
 * Copyright 2021 Steven Taylor McGown
 * This class defines SportsCar Vehicle attributes to be charged and described on
 * its corresponding Vehicle object
 */
package CarType;

import decoratordesignpattern.Vehicle;

public class SportsCar extends Vehicle {
    /**
     * Constructor
     */
    public SportsCar() {
        this.description = "Sports car";
    }
    /**
     * @return Cost of sports car
     */
    public double getCost() {
        return 30000;
    }
}
