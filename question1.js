function solver(array) 
	{
		if (typeof(array[0]) === 'number' && typeof(array[1]) === 'string' && typeof(array[2]) === 'number')
		{
			switch(array[1].toUpperCase()) 
			{
				case "PLUS":
					return(array[0]+array[2]);
				case "TIMES":
					return(array[0]*array[2]);
				case "MINUS":
					return(array[0]-array[2]);
				case "DIVIDE":
					return(array[0]/array[2]);
				default:
					return("Unrecognised Operation")
			}
		}
		else
		{
			return("Array in incorrect format. First and last elements must be numbers, middle element must be string.")
		}

}