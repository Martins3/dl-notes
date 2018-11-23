# only the last important !

## one

1. fread fwrite

## two
1. 添加系统调用
    1. linux 系统调用机制
1. todo
    1. 编写源代码
    2. 连接新的系统调用函数
    3. 重装
    4. 重启
    5. 在函数中间添加
    
    // 添加简单的系统调用
    https://tssurya.wordpress.com/2014/08/19/adding-a-hello-world-system-call-to-linux-kernel-3-16-0/

    // 编译内核
    https://www.binss.me/blog/how-to-compile-and-install-linux-kernel/
    
## three
1. 注册设备
register_chrdev
主设备号用来表示一个特定的驱动程序。次设备号用来表示使用该驱动程序的各设备
https://www.fsl.cs.sunysb.edu/kernel-api/re941.html
register_blkdev
https://www.kernel.org/doc/htmldocs/kernel-api/API-register-blkdev.html

2. 注销设备
unregister_chrdev
unregister_blkdev

3. Linux系统采用一组固定的入口点来实现驱动设备的功能。

4. 内核模块(Loadable Kernel module)
    1. 注销 和 添加
    init_module cleanup_module
    2. 卸载
    3. 查询
    4. 重新分配  sys_create_module

    模块的添加 查看 删除


添加程序


1. LKM 和 驱动的的关系是什么 ？
    1. 使用LKM的方式添加
    2. 
2. 添加的驱动 和 添加LKM
3. 模块 的初始化函数， 卸载函数是唯一的， 后面几个函数有什么用途 ？
4. 

## four

proc 文件的使用


## five
包含文件/目录创建/删除，目录显示等基本功能(可自行扩充文件读/写、用户登录、权限控制、读写保护等其他功能)


