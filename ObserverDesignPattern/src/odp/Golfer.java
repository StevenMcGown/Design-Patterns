package odp;

import java.util.ArrayList;

public class Golfer implements Subject {
	/*
	 * This class creates the golfer object. A golfer can be assigned an observer which keeps track of
	 * the golfer's score.
	 * 
	 */
	public String name;
	private ArrayList<Observer> observers = new ArrayList<Observer>();
	
	/**
	 * Instantiates the golfer object
	 * @param name
	 */
	public Golfer(String name) {
		this.name = name;
		observers = new ArrayList<Observer>();
	}
	/**
	 * registers an observer for the golfer
	 * @param Observer The observer for the golfer
	 */
	@Override
	public void registerObserver(Observer observer) {
		observers.add(observer);
	}

	/**
	 * removes an observer from the golfer
	 * @param Observer The observer for the golfer
	 */
	@Override
	public void removeObserver(Observer observer) {
		observers.remove(observer);
	}

	/**
	 * Notifies the observers the golfer's score per round
	 * @param strokes The number of strokes taken
	 * @param par The par for the hole
	 */
	@Override
	public void notifyObservers(int strokes, int par) {
		//Loop through each observer
		for(Observer o : observers) {
			o.update(strokes, par);
		}
	}

	/**
	 * Enters the score for each round the golfer plays
	 * @param strokes The number of strokes taken
	 * @param par The par of the hole 
	 */
	public void enterScore(int strokes, int par) {
		notifyObservers(strokes, par);
	}
	// Returns the golfer's name
	public String getName() {
		return this.name;
	}

}
