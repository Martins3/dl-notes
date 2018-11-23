#include <stdio.h>
#include <stdlib.h>
#define IDENT 0
#define OP +

/* Create abstract data type for vector */
typedef int data_t;
typedef struct {
long int len;
data_t *data;
} vec_rec, *vec_ptr;

int main(int argc, char const *argv[]) {
  /* code */

  return 0;
}

//P477
void twiddle1(int *xp, int *yp)
{
*xp += *yp;
*xp += *yp;
}
void twiddle2(int *xp, int *yp)
{
*xp += 2* *yp;
}


/* Create vector of specified length */
vec_ptr new_vec(long int len)
{
/* Allocate header structure */
  vec_ptr result = (vec_ptr) malloc(sizeof(vec_rec));
  if (!result)
    return NULL; /* Couldn’t allocate storage */
  result->len = len;
/* Allocate array */
  if (len > 0) {
  data_t *data = (data_t *)calloc(len, sizeof(data_t));
    if (!data) {
      free((void *) result);
      return NULL; /* Couldn’t allocate storage */
    }
    result->data = data;
  }
  else
  result->data = NULL;
return result;
}
/*
* Retrieve vector element and store at dest.
* Return 0 (out of bounds) or 1 (successful)
*/
int get_vec_element(vec_ptr v, long int index, data_t *dest)
{
  if (index < 0 || index >= v->len)
    return 0;
  *dest = v->data[index];
  return 1;
}
/* Return length of vector */
long int vec_length(vec_ptr v)
{
  return v->len;
}

void combine1(vec_ptr v, data_t *dest)
{
  long int i;
  *dest = IDENT;
  for (i = 0; i < vec_length(v); i++) {
    data_t val;
    get_vec_element(v, i, &val);
    *dest = *dest OP val;
  }
}
/* Move call to vec_length out of loop */
// and see why the repeated bounds checking by combine2 does not
// make its performance much worse.

void combine2(vec_ptr v, data_t *dest)
{
long int i;
long int length = vec_length(v);
*dest = IDENT;
for(i = 0; i < length; i++) {
  data_t val;
  get_vec_element(v, i, &val);
  *dest = *dest OP val;
  }
}
data_t *get_vec_start(vec_ptr v)
{
return v->data;
}

void combine3(vec_ptr v, data_t *dest)
{
long int i;
long int length = vec_length(v);
data_t *data = get_vec_start(v);
*dest = IDENT;
for (i = 0; i < length; i++) {
*dest = *dest OP data[i];
}
}

/* Accumulate result in local variable */
void combine4(vec_ptr v, data_t *dest)
{
long int i;
long int length = vec_length(v);
data_t *data = get_vec_start(v);
data_t acc = IDENT;
for (i = 0; i < length; i++) {
acc = acc OP data[i];
}
*dest = acc;
}
