/**
 * Copyright 2021 Steven Taylor McGown
 * Tricycle object extends the base abstract class bike
 */


package biketypes;

import factorydesignpattern.Bike;

/**
 * Pre-determined variable values based on required output
 */
public class Tricycle extends Bike {
    public Tricycle() {
        name = "tricycle";
        price = 54.95;
        numWheels = 3;
        hasPedals = true;
        hasTrainingWheels = false;
    }
}
