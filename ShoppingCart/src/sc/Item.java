package sc;

public class Item
{
    private String name;

	public Item()
	{
		super();

		this.name = "";
	}

	public Item(String name)
	{
		super();

		this.name = name;
	}

	public String getName()
	{
		return name;
	}

	public void setName(String name)
	{
		this.name = name;
	}
}
