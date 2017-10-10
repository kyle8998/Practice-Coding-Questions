        /* Declare second integer, double, and String variables. */
        int a;
        double b;
        String c;
        /* Read and save an integer, double, and String to your variables.*/
        // Note: If you have trouble reading the entire String, please go back and review the Tutorial closely.
        a = scan.hasNextInt()? scan.nextInt():null;
        b = scan.hasNextDouble()? scan.nextDouble():null;
        // Skips to next line because HasDouble does not go to the next line.
        scan.nextLine();
        c = scan.hasNextLine()? scan.nextLine():null;
        /* Print the sum of both integer variables on a new line. */
        System.out.println(i+a);
        /* Print the sum of the double variables on a new line. */
		System.out.println(d+b);
        /* Concatenate and print the String variables on a new line; 
        	the 's' variable above should be printed first. */
        System.out.println(s+c);