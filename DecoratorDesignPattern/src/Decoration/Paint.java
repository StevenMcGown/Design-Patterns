/**
 * Copyright 2021 Steven Taylor McGown
 * This class defines Paint attributes to be charged and described on
 * its corresponding Vehicle object
 */
package Decoration;

import decoratordesignpattern.Vehicle;
import decoratordesignpattern.VehicleDecorator;

public class Paint extends VehicleDecorator {
    private Vehicle vehicle;

    /**
     * Constructor
     * @param vehicle Paint for vehicle
     */
    public Paint(Vehicle vehicle) {
        this.vehicle = vehicle;
    }
    /**
     * @return Appends "Fancy paint" to Vehicle description
     */
    public String toString(){
        return vehicle.toString() + ", fancy paint";
    }
    /**
    * 
    * @return Cost of Paint
    */
    public double getCost() {
        return vehicle.getCost() + 150;
    }
}
