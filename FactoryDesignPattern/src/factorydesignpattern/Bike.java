/**
 * Copyright 2021 Steven Taylor McGown
 * Creates a bike object which has specific attributes defined in the UML diagram
 */

package factorydesignpattern;

public abstract class Bike {
    protected String name;
    protected Double price;
    protected int numWheels;
    protected boolean hasPedals;
    protected boolean hasTrainingWheels;

    /**
     * Instantiates bike object by making use of all local methods
     */
    public void createBike() {
        createFrame();
        addWheels();
        addTrainingWheels();
        addPedals();
    }

    /**
     * "Assembles the frame"; prints the name of the type of bike created
     */
    private void createFrame() {
        System.out.println("Assembling " + this.name + " frame");
    }

    /**
     * Prints the number of wheels attributed to the bike type
     */
    private void addWheels() {
        System.out.println("Adding " + this.numWheels + " wheel(s)");

    }

    /**
     * Adds training wheels if bike object's hasTrainingWheels boolean is true
     */
    private void addTrainingWheels() {
        if(this.hasTrainingWheels)
            System.out.println("Adding training wheels");
    }

    /**
     * Adds pedals if bike object's hasPedals attribute is true
     */
    private void addPedals() {
        if(this.hasPedals)
            System.out.println("Adding pedals");
    }

    /**
     * Returns the price of the bike
     * @return Price of bike
     */
    public Double getPrice() {
        return this.price;
    }
}
