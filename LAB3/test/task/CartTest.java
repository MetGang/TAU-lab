package task;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.Before;
import org.junit.After;
import org.junit.Test;

import sc.Cart;
import sc.Item;

public class CartTest
{
	private Cart cart = null;
	
	@Before
	public void begin()
	{
		cart = new Cart();
	}
	
	@After
	public void end()
	{
		cart = null;
	}

	@Test
	public void test_0()
	{
		Item item = new Item("Baguette", 1.05, 1);
		
		cart.addItem(item);
		
		assertEquals(1, cart.getItemCount());
		
		cart.removeItem(item);
		
		assertEquals(0, cart.getItemCount());
	}
	
	@Test
	public void test_1()
	{
		Item item0 = new Item("Baguette", 1.05, 1);
		Item item1 = new Item("Chocolattio", 2.40, 1);
		
		cart.addItem(item0);
		cart.addItem(item1);
		
		assertEquals(3.45, cart.getFullPrice());
	}
	
	@Test
	public void test_2()
	{
		Item item0 = new Item("Baguette", 1.05, 3);
		Item item1 = new Item("Chocolattio", 2.40, 2);
		
		cart.addItem(item0);
		cart.addItem(item1);
		
		assertTrue(cart.getFullPrice() == 7.95);
	}
	
	@Test
	public void test_3()
	{
		Item item = new Item("Baguette", 1.05, 3);
		
		cart.addItem(item);
		
		assertEquals(3, cart.getItemCount());
		
		cart.removeItemPiece(item);
		
		assertEquals(2, cart.getItemCount());
		
		cart.removeItemPiece(item);
		
		assertEquals(1, cart.getItemCount());
		
		cart.removeItemPiece(item);
		
		assertEquals(0, cart.getItemCount());
	}

	@Test
	public void test_4()
	{
		Item item = new Item("Baguette", 1.05, 3);
		
		cart.addItem(item);
		
		assertEquals(3, cart.getItemCount());
		
		cart.removeItem(item);
		
		assertNotEquals(3, cart.getItemCount());
	}

	@Test
	public void test_5()
	{
		try
		{
			@SuppressWarnings("unused")
			Item item = new Item("Baguette", -1.05, 3);
			
		    fail("Should have thrown an exception");
		}
		catch(IllegalArgumentException e)
		{
			assertTrue(true);
		}
	}

	@Test
	public void test_6()
	{
		try
		{
			@SuppressWarnings("unused")
			Item item = new Item("Baguette", 1.05, -3);
			
		    fail("Should have thrown an exception");
		}
		catch(IllegalArgumentException e)
		{
			assertTrue(true);
		}
	}
}
