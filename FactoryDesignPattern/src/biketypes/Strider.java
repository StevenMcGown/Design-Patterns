/**
 * Copyright 2021 Steven Taylor McGown
 * Strider object extends the base abstract class bike
 */

package biketypes;

import factorydesignpattern.Bike;

/**
 * Pre-determined variable values based on required output
 */
public class Strider extends Bike {
    public Strider() {
        name = "strider";
        price = 65.99;
        numWheels = 2;
        hasPedals = false;
        hasTrainingWheels = false;
    }
}
