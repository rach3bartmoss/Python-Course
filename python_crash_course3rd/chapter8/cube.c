#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int	arr_depth;
	int	cube[5][5][5]; //3*3*3 = 27 items

	int	arr_depth_helper = (sizeof(cube) / sizeof(cube[0]));
	arr_depth = ((sizeof(cube) / sizeof(cube[0])) * arr_depth_helper * arr_depth_helper);
	printf("%d\n", arr_depth);
}