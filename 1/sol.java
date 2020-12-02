import java.io.*;
import java.util.*;

public class sol {

	public static void main(String[] args) {
		String line;
		ArrayList<Integer> entries = new ArrayList<>();
		try {
			BufferedReader reader = new BufferedReader(new FileReader("input"));
			while ((line = reader.readLine()) != null) {
				entries.add(Integer.parseInt(line));
			}
		} catch (IOException e) {
			System.out.println(e);
		}
	
		for (int a : entries) {
			for (int b : entries) {
				if (a + b == 2020)
					System.out.println(a*b);
			}
		}
	}
}
