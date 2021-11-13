#include "../sample/sample.h"
#include "stdio.h"
int do_more_stuff(point_t p)
{
    printf("doing more than enough!!\n");
    int res = do_stuff(p);
    return res;
}
