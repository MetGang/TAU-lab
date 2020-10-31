package task;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.*;

import sc.Cart;
import sc.Item;

public class CartTest
{
	private Cart cart = null;
	
	@Before
	public void Begin()
	{
		cart = new Cart();
	}
	
	@After
	public void End()
	{
		cart = null;
	}

	@Test
	public void Test_0()
	{
		Item item = new Item();
		
		cart.addItem(item);
		
		assertEquals(1, cart.getItemCount());
		
		cart.removeItem(item);
		
		assertEquals(0, cart.getItemCount());
	}
}
