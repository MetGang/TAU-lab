package sc;

import java.util.ArrayList;

public class Cart
{
	public ArrayList<Item> items = new ArrayList<>();
	
	public void addItem(Item item)
	{
		items.add(item);
	}

	public void removeItem(Item item)
	{
		items.remove(item);
	}
	
	public int getItemCount()
	{
		return items.size();
	}
	
	public double getFullPrice()
	{
		double price = 0.0;
		
		for (var item : items)
		{
			price += item.getPrice();
		}
		
		return price;
	}
}
