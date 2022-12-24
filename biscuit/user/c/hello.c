#include <litc.h>

int main(int argc, char **argv)
{
	int i;
	for (i = 0; i < 3; i++) {
		printf("hello world!\n");
		int j;
		for (j = 0; j < 100000000; j++)
			asm volatile("":::"memory");
	}
	// stack addresses
	char buf[20] =  {0,};
	// register size_t stackptr asm("rsp");
	printf("i at: %p buf at: %p\n", &i, &buf);



	return 0;
}
