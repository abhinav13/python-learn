#include <stdio.h>

static __attribute__((used)) int var1;
int func1(void)
{
    int out;
    asm("mov var1, %0" : "=r" (out));
    return out;
}

int main()
{
    func1();
    return 0;

}
