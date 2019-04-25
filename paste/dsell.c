#include <stdio.h>
#include <math.h>

const int eval_limit = 500;

int main()
{
    int sold = dsell();
    printf("sold = %d", sold);
    return 0;
}

int dsell()
{
    /* location (default, 'pouch', 'here') doesn't really matter 
        for this, as I'm just generating a list of items
    */
    int total_items = (int)(pow(2,20));
    int items[total_items];
    for(int item = 0; item < total_items; ++item) {
        items[item] = 1;
    }
    
    int length = (int)(sizeof(items)/sizeof(items[0]));
    
    /* essentially, all that's needed for this is:
        global eval_limit
        items list
        length of items list
    */
    
    int total = 0;
    int start = 0;
    int stop = length;
    if (length > eval_limit){
        int subsets = length / eval_limit + 1;
        for(int i = 0; i < subsets; i++){
            start = 0 + (eval_limit * i);
            if ((start + eval_limit) > length){
                stop = length;
            } else {
                stop = start + eval_limit;
            }
            for(int j = start; j < stop; j++){
                total = total + sell(items[j]);
            }
        }
    } else {
        for(int k = 0; k < length; k++){
            total = total + sell(items[k]);
        }
    }
    
    return total;
}

int sell(int item)
{
    /* sell magic happens here, for now, my array of items is 
        stupid simple and each item is just set to int 1
    */
    int sold = item;
    return sold;
}
