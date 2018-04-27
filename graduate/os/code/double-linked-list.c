#include <stdio.h>
typedef struct list_entry {
    struct list_entry *prev, *next;
} list_entry_t;


typedef struct {
    list_entry_t free_list;         // the list header
    unsigned int nr_free;           // # of free pages in this free list
} free_area_t;


static inline void list_init(list_entry_t *elm) {
    elm->prev = elm->next = elm;
}

static inline void __list_add(list_entry_t *elm, list_entry_t *prev, list_entry_t *next) {
    prev->next = next->prev = elm;
    elm->next = next;
    elm->prev = prev;
}

static inline void __list_del(list_entry_t *prev, list_entry_t *next) {
    prev->next = next;
    next->prev = prev;
}


static inline void list_del(list_entry_t *listelm) {
    __list_del(listelm->prev, listelm->next);
}

/**
 * 访问宿主
 * macro offset 首先将地址0 转化为 type *　类型，然后获取对应的mem的类型，
 * 然后就是该相对地址
 */
/* Return the offset of 'member' relative to the beginning of a struct type */
#define offsetof(type, member)                                      \
((size_t)(&((type *)0)->member))

/* *
 * to_struct - get the struct from a ptr
 * @ptr:    a struct pointer of member
 * @type:   the type of the struct this is embedded in
 * @member: the name of the member within the struct
 * */
#define to_struct(ptr, type, member)                               \
((type *)((char *)(ptr) - offsetof(type, member)))

// convert list entry to page
#define le2page(le, member)                 \
to_struct((le), struct Page, member)


int main(int argc, char *argv[]){

    return 0;
}
