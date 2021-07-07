/**
 * Copyright 2021 Steven Taylor McGown
 * This is an abstract class extends the Vehicle class. Vehicle decorator
 * returns the string value of the decoration values defined in inherited classes.
 */

package decoratordesignpattern;

public abstract class VehicleDecorator extends Vehicle {

    /**
     * @return The string value of the decoration values defined in inherited classes
     */
    public abstract String toString();
}