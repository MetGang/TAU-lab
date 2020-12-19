package task;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.Before;
import org.junit.After;
import org.junit.Test;

import com.google.gson.Gson;

public class GsonTest
{
	private Gson gson = null;
	
	@Before
	public void begin()
	{
		gson = new Gson();
	}
	
	@After
	public void end()
	{
		gson = null;
	}

	@Test
	public void test_0()
	{
		var j = gson.toJson("Hello World!");
		
		assertEquals("\"Hello World!\"", j.toString());
	}

	@Test
	public void test_1()
	{
		var j = gson.toJson(0);
		
		assertEquals("0", j.toString());
	}

	@Test
	public void test_2()
	{
		var j = gson.toJson(1.5f);
		
		assertEquals("1.5", j.toString());
	}
}
