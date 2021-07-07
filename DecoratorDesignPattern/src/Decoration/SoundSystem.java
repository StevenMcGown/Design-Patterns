/**
 * Copyright 2021 Steven Taylor McGown
 * This class defines SoundSystem attributes to be charged and described on
 * its corresponding Vehicle object
 */
package Decoration;

import decoratordesignpattern.Vehicle;
import decoratordesignpattern.VehicleDecorator;

public class SoundSystem extends VehicleDecorator {
    private Vehicle vehicle;

    /**
     * Constructor
     * @param vehicle Sound system for vehicle
     */
    public SoundSystem(Vehicle vehicle) {
        this.vehicle = vehicle;
    }
    /**
     * @return Apends string value "Awesome sound" to Vehicle description
     */
    public String toString(){
        return vehicle.toString() + ", awesome sound";
    }
    /**
     * @return Cost of SoundSystem
     */
    public double getCost() {
        return vehicle.getCost() + 350;
    }
}
