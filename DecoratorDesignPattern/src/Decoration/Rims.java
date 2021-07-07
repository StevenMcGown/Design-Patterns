/**
 * Copyright 2021 Steven Taylor McGown
 * This class defines Rims attributes to be charged and described on
 * its corresponding Vehicle object
 */
package Decoration;

import decoratordesignpattern.Vehicle;
import decoratordesignpattern.VehicleDecorator;

public class Rims extends VehicleDecorator{
    private Vehicle vehicle;

    /**
     * Constructor
     * @param vehicle Rims for Vehicle
     */
    public Rims(Vehicle vehicle){
        this.vehicle = vehicle;
    }
    /**
     * @return Appends string value of "Cool rims"
     */
    public String toString(){
        return vehicle.toString() + ", cool rims";
    }

    /**
     * @return Cost of Rims
     */
    public double getCost() {
        return vehicle.getCost() + 200;
    }
}
