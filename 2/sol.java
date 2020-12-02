import java.io.*;

public class sol
{
	public static void usage()
	{
		System.out.println("Usage: java sol TASK");
		System.out.println("Where TASK is 1 or 2");
		System.exit(1);
	}

	public static void main(String[] args)
	{
		if (args.length != 1) usage();

		int TASK = Integer.parseInt(args[0]);
		if (TASK < 1 || TASK > 2) usage();

		try
		{
			BufferedReader in = new BufferedReader(new FileReader("input"));
			String line;
			int num_valid = 0;
			while ((line = in.readLine()) != null)
			{
				String[] tmp = line.split("-");
				int idx_1 = Integer.parseInt(tmp[0]);
				int idx_2 = Integer.parseInt(tmp[1].split(" ")[0]);
				
				tmp = line.split(" ");
				char letter = tmp[1].charAt(0);

				char[] password = tmp[2].toCharArray();

				if (TASK == 1)
				{
					int num_letter = 0;
					for (char c : password)
						if (c == letter)
							num_letter += 1;

					if (idx_1 <= num_letter && num_letter <= idx_2)
						num_valid += 1;		
				}
				else
				{
					if ((password[idx_1 - 1] == letter || password[idx_2 - 1] == letter) &&
						(password[idx_1 - 1] != letter || password[idx_2 - 1] != letter))
							num_valid += 1;
				}
			}
			System.out.println(num_valid);
			
			in.close();
		}
		catch (IOException e)
		{
			e.printStackTrace();
		}
	}
}
