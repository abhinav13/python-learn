#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <limits.h>




int main()
{

	uint64_t i = LLONG_MAX;
	uint64_t divisor = 7;
	uint64_t sum = 1;
	uint64_t count = divisor;
		
	printf("sizeof int %d, value = %llu\n", sizeof(int64_t), i);
	
	while (count < i)
	{
		count = count << 1;
		sum = sum << 1;
	
		/*if (count > LLONG_MAX)
			printf("%llu",count -LLONG_MAX);*/
	}

	if (count == i){
		printf("output = %llu", sum);
		return 0;
	}
	////if we got here then we over shot our target 
	count = count >> 1;
	sum = sum >> 1;
	while (count < i){
		count = count + divisor;
		sum = sum + 1;
	}
	
	printf("output = %llu", sum);
	return 0;
}
