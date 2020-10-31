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
}
