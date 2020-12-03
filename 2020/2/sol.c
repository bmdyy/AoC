#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* PROG_NAME;

void usage()
{
	printf("Usage: %s TASK\n", PROG_NAME);
	printf("Where TASK is 1 or 2\n");
}

int main(int argc, char *argv[])
{
	// Assign global var PROGRAM NAME
	PROG_NAME = argv[0];

	// Check arguments
	int TASK = 0;
	if (argc != 2)
	{
		usage();
		return 1;
	}
	else 
	{
		TASK = atoi(argv[1]);
		if (TASK < 1 || TASK > 2)
		{
			usage();
			return 1;
		}
	}
	
	// Try to open the input file
	FILE *fp;
	fp = fopen("input", "r");
	if (fp == NULL)
	{
		printf("Could not open file");
		return 1;
	}

	// Loop through the lines of the file
	int num_valid = 0;

	char* line = NULL;
	size_t len = 0;
	ssize_t read;
	while ((read = getline(&line, &len, fp)) != -1)
	{
		// Split the string into the indiv. parts
		char* ptr = strtok(line, "-");
		int idx_1 = atoi(ptr);
		
		ptr = strtok(NULL, " ");
		int idx_2 = atoi(ptr);
		
		ptr = strtok(NULL, " ");
		char* letter = ptr;
		
		ptr = strtok(NULL, " ");
		char* password = ptr;

		// TASK 1
		if (TASK == 1)
		{
			// Count number of this letter in the password	
			int num_letter = 0;
			int i = 0;
			size_t length = strlen(password);
			for (; i < length; i++)
				if (password[i] == letter[0])
					num_letter ++;
			
			// Check if it is a valid password
			if (idx_1 <= num_letter && num_letter <= idx_2)
				num_valid ++;	
		}
		// TASK 2
		else
		{
			// Letter is at idx_1 XOR idx_2
			if ((password[idx_1 - 1] == letter[0] || password[idx_2 - 1] == letter[0]) &&
			    (password[idx_1 - 1] != letter[0] || password[idx_2 - 1] != letter[0]))
				num_valid ++;
		}
	}
	if (line) free(line);	

	// Print the answer
	printf("%d\n", num_valid);

	// Close file and exit the program
	fclose(fp);
	return 0;
}
