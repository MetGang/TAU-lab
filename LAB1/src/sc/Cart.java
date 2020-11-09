package sc;

import java.util.ArrayList;

public class Cart
{
	public ArrayList<Item> items = new ArrayList<>();
	
	public void addItem(Item item)
	{
		items.add(item);
	}

	public void removeItemPiece(Item item)
	{
		if (item.getAmount() < 2)
		{
			removeItem(item);
		}
		else
		{
			item.setAmount(item.getAmount() - 1);
		}
	}

	public void removeItem(Item item)
	{
		items.remove(item);
	}
	
	public int getItemCount()
	{
		int amount = 0;
		
		for (var item : items)
		{
			amount += item.getAmount();
		}
		
		return amount;
	}
	
	public double getFullPrice()
	{
		double price = 0.0;
		
		for (var item : items)
		{
			price += item.getPrice() * item.getAmount();
		}
		
		return price;
	}
}
