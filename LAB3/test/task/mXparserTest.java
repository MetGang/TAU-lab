package task;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.Test;

import org.mariuszgromada.math.mxparser.*;

public class mXparserTest
{
	@Test
	public void test_0()
	{
		Expression exp = new Expression("0");
		
		assertEquals(0, exp.calculate());
	}

	@Test
	public void test_1()
	{
		Expression exp = new Expression("2*2");
		
		assertEquals(4.0, exp.calculate());
	}

	@Test
	public void test_2()
	{
		Expression eh = new Expression("5^2 * 7^3 * 11^1 * 67^1 * 49201^1");
		Expression ew = new Expression("71^1 * 218549^1 * 6195547^1");
		String h = mXparser.numberToAsciiString(eh.calculate());
		String w = mXparser.numberToAsciiString(ew.calculate());
		
		assertEquals("Hello World!", h + " " + w);
	}
}
