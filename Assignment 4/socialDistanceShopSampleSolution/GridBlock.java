package socialDistanceShopSampleSolution;

import java.util.concurrent.atomic.*;
import java.util.concurrent.Semaphore;
// GridBlock class to represent a block in the shop.

public class GridBlock {
	private AtomicBoolean isOccupied; // CHANGED
	private final boolean isExit; 
	private final boolean isCheckoutCounter;
   private Semaphore lockGrid; // ADDED
	private int [] coords; // the coordinate of the block.
	private int ID;
	
	public static int classCounter=0;
	
	GridBlock(boolean exitBlock, boolean checkoutBlock) throws InterruptedException {
		isExit=exitBlock;
		isCheckoutCounter=checkoutBlock;
		isOccupied= new AtomicBoolean(false); // CHANGED
		ID=classCounter;
		classCounter++;
      lockGrid = new Semaphore(1); // ADDED
	}
	
	GridBlock(int x, int y, boolean exitBlock, boolean refreshBlock) throws InterruptedException {
		this(exitBlock,refreshBlock);
		coords = new int [] {x,y};
	}
	
	//getter
	public  int getX() {return coords[0];}  
	
	//getter
	public  int getY() {return coords[1];}
	
	//for customer to move to a block
   // CHANGED THIS METHOD
	synchronized public boolean get() throws InterruptedException {
      if (isOccupied.get()){
         return false;
      }
      lockGrid.acquire();
  		isOccupied.set(true);
		return true;
	}
		
	//for customer to leave a block
   // CHANGED THIS METHOD
	synchronized public void release() {
      lockGrid.release();
		isOccupied.set(false);
	}
	
	//getter
	public boolean occupied() {
		return isOccupied.get(); // CHANGED
	}
	
	//getter
	public  boolean isExit() {
		return isExit;	
	}

	//getter
	public  boolean isCheckoutCounter() {
		return isCheckoutCounter;
	}
	
	//getter
	public int getID() {return this.ID;}
}
