/**
 * Copyright 2021 Steven Taylor McGown
 * Kids bike object extends the base abstract class bike
 */

package biketypes;

import factorydesignpattern.Bike;

/**
 * Pre-determined variable values based on required output
 */
public class KidsBike extends Bike {
    public KidsBike() {
        name = "kids bike";
        price = 80.99;
        numWheels = 2;
        hasPedals = true;
        hasTrainingWheels = true;
    }
}
