package sc;

public class Item
{
    private String name;
    private double price;
    private int amount;

	public Item(String name, double price, int amount)
	{
		super();
		setName(name);
		setPrice(price);
		setAmount(amount);
	}

	public String getName()
	{
		return name;
	}

	public void setName(String name)
	{
		this.name = name;
	}

	public double getPrice()
	{
		return price;
	}

	public void setPrice(double price) throws IllegalArgumentException 
	{
		if (price < 0.0)
		{
			throw new IllegalArgumentException();
		}
		else
		{
			this.price = price;
		}
	}

	public int getAmount()
	{
		return amount;
	}

	public void setAmount(int amount) throws IllegalArgumentException 
	{
		if (amount < 0)
		{
			throw new IllegalArgumentException();
		}
		else
		{
			this.amount = amount;
		}
	}

}
