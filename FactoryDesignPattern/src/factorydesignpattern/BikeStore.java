/**
 * Copyright 2021 Steven Taylor McGown
 * Creates bikes based on request
 */

package factorydesignpattern;

import factorydesignpattern.Bike;
import biketypes.*;

public class BikeStore {

    public BikeStore() {}

    /**
     * Makes user of the createBike function
     * @param type Bicycle object type string (tricycle, kids bike, strider)
     * @return bike object returned from the createBike function
     */
    public Bike orderBike(String type) {
        Bike bike = createBike(type);
        return bike;
    }

    /**
     * Returns a bicycle type based on the string given
     * @param type Bicycle object type string (tricycle, kids bike, strider)
     * @return Bike object
     */
    private Bike createBike(String type){ 
        if(type.equals("tricycle")) {
            return new Tricycle();
        } else if (type.equals("kids bike")) {
            return new KidsBike();
        } else if (type.equals("strider")) {
            return new Strider();
        }

        return null;
    }
}
