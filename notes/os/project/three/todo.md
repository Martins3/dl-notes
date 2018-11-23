
# code 


# operation
1. 将 hello 添加到 文件夹 中间
2. cd arch/x86/syscalls
gedit syscall_32.tbl
添加354    i386    hello    sys_my_copy_file

3. cd  include/linux/

gedit syscalls.h

asmlinkage long sys_my_copy_file(char * dest, char * source);

4. 编译内核
