
p：     文件格式 elf64-x86-64


Disassembly of section .init:

0000000000000510 <_init>:
 510:	48 83 ec 08          	sub    $0x8,%rsp
 514:	48 8b 05 c5 0a 20 00 	mov    0x200ac5(%rip),%rax        # 200fe0 <__gmon_start__>
 51b:	48 85 c0             	test   %rax,%rax
 51e:	74 02                	je     522 <_init+0x12>
 520:	ff d0                	callq  *%rax
 522:	48 83 c4 08          	add    $0x8,%rsp
 526:	c3                   	retq   

Disassembly of section .plt:

0000000000000530 <.plt>:
 530:	ff 35 d2 0a 20 00    	pushq  0x200ad2(%rip)        # 201008 <_GLOBAL_OFFSET_TABLE_+0x8>
 536:	ff 25 d4 0a 20 00    	jmpq   *0x200ad4(%rip)        # 201010 <_GLOBAL_OFFSET_TABLE_+0x10>
 53c:	0f 1f 40 00          	nopl   0x0(%rax)

Disassembly of section .plt.got:

0000000000000540 <.plt.got>:
 540:	ff 25 b2 0a 20 00    	jmpq   *0x200ab2(%rip)        # 200ff8 <__cxa_finalize@GLIBC_2.2.5>
 546:	66 90                	xchg   %ax,%ax

Disassembly of section .text:

0000000000000550 <_start>:
 550:	31 ed                	xor    %ebp,%ebp
 552:	49 89 d1             	mov    %rdx,%r9
 555:	5e                   	pop    %rsi
 556:	48 89 e2             	mov    %rsp,%rdx
 559:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
 55d:	50                   	push   %rax
 55e:	54                   	push   %rsp
 55f:	4c 8d 05 ea 01 00 00 	lea    0x1ea(%rip),%r8        # 750 <__libc_csu_fini>
 566:	48 8d 0d 73 01 00 00 	lea    0x173(%rip),%rcx        # 6e0 <__libc_csu_init>
 56d:	48 8d 3d 0c 01 00 00 	lea    0x10c(%rip),%rdi        # 680 <main>
 574:	ff 15 5e 0a 20 00    	callq  *0x200a5e(%rip)        # 200fd8 <__libc_start_main@GLIBC_2.2.5>
 57a:	f4                   	hlt    
 57b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000000580 <deregister_tm_clones>:
 580:	48 8d 3d b1 0a 20 00 	lea    0x200ab1(%rip),%rdi        # 201038 <__TMC_END__>
 587:	48 8d 05 b1 0a 20 00 	lea    0x200ab1(%rip),%rax        # 20103f <__TMC_END__+0x7>
 58e:	55                   	push   %rbp
 58f:	48 29 f8             	sub    %rdi,%rax
 592:	48 89 e5             	mov    %rsp,%rbp
 595:	48 83 f8 0e          	cmp    $0xe,%rax
 599:	76 15                	jbe    5b0 <deregister_tm_clones+0x30>
 59b:	48 8b 05 2e 0a 20 00 	mov    0x200a2e(%rip),%rax        # 200fd0 <_ITM_deregisterTMCloneTable>
 5a2:	48 85 c0             	test   %rax,%rax
 5a5:	74 09                	je     5b0 <deregister_tm_clones+0x30>
 5a7:	5d                   	pop    %rbp
 5a8:	ff e0                	jmpq   *%rax
 5aa:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
 5b0:	5d                   	pop    %rbp
 5b1:	c3                   	retq   
 5b2:	0f 1f 40 00          	nopl   0x0(%rax)
 5b6:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
 5bd:	00 00 00 

00000000000005c0 <register_tm_clones>:
 5c0:	48 8d 3d 71 0a 20 00 	lea    0x200a71(%rip),%rdi        # 201038 <__TMC_END__>
 5c7:	48 8d 35 6a 0a 20 00 	lea    0x200a6a(%rip),%rsi        # 201038 <__TMC_END__>
 5ce:	55                   	push   %rbp
 5cf:	48 29 fe             	sub    %rdi,%rsi
 5d2:	48 89 e5             	mov    %rsp,%rbp
 5d5:	48 c1 fe 03          	sar    $0x3,%rsi
 5d9:	48 89 f0             	mov    %rsi,%rax
 5dc:	48 c1 e8 3f          	shr    $0x3f,%rax
 5e0:	48 01 c6             	add    %rax,%rsi
 5e3:	48 d1 fe             	sar    %rsi
 5e6:	74 18                	je     600 <register_tm_clones+0x40>
 5e8:	48 8b 05 01 0a 20 00 	mov    0x200a01(%rip),%rax        # 200ff0 <_ITM_registerTMCloneTable>
 5ef:	48 85 c0             	test   %rax,%rax
 5f2:	74 0c                	je     600 <register_tm_clones+0x40>
 5f4:	5d                   	pop    %rbp
 5f5:	ff e0                	jmpq   *%rax
 5f7:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
 5fe:	00 00 
 600:	5d                   	pop    %rbp
 601:	c3                   	retq   
 602:	0f 1f 40 00          	nopl   0x0(%rax)
 606:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
 60d:	00 00 00 

0000000000000610 <__do_global_dtors_aux>:
 610:	80 3d 21 0a 20 00 00 	cmpb   $0x0,0x200a21(%rip)        # 201038 <__TMC_END__>
 617:	75 27                	jne    640 <__do_global_dtors_aux+0x30>
 619:	48 83 3d d7 09 20 00 	cmpq   $0x0,0x2009d7(%rip)        # 200ff8 <__cxa_finalize@GLIBC_2.2.5>
 620:	00 
 621:	55                   	push   %rbp
 622:	48 89 e5             	mov    %rsp,%rbp
 625:	74 0c                	je     633 <__do_global_dtors_aux+0x23>
 627:	48 8b 3d f2 09 20 00 	mov    0x2009f2(%rip),%rdi        # 201020 <__dso_handle>
 62e:	e8 0d ff ff ff       	callq  540 <.plt.got>
 633:	e8 48 ff ff ff       	callq  580 <deregister_tm_clones>
 638:	5d                   	pop    %rbp
 639:	c6 05 f8 09 20 00 01 	movb   $0x1,0x2009f8(%rip)        # 201038 <__TMC_END__>
 640:	f3 c3                	repz retq 
 642:	0f 1f 40 00          	nopl   0x0(%rax)
 646:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
 64d:	00 00 00 

0000000000000650 <frame_dummy>:
 650:	48 8d 3d c1 07 20 00 	lea    0x2007c1(%rip),%rdi        # 200e18 <__JCR_END__>
 657:	48 83 3f 00          	cmpq   $0x0,(%rdi)
 65b:	75 0b                	jne    668 <frame_dummy+0x18>
 65d:	e9 5e ff ff ff       	jmpq   5c0 <register_tm_clones>
 662:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
 668:	48 8b 05 79 09 20 00 	mov    0x200979(%rip),%rax        # 200fe8 <_Jv_RegisterClasses>
 66f:	48 85 c0             	test   %rax,%rax
 672:	74 e9                	je     65d <frame_dummy+0xd>
 674:	55                   	push   %rbp
 675:	48 89 e5             	mov    %rsp,%rbp
 678:	ff d0                	callq  *%rax
 67a:	5d                   	pop    %rbp
 67b:	e9 40 ff ff ff       	jmpq   5c0 <register_tm_clones>

0000000000000680 <main>:
 680:	55                   	push   %rbp
 681:	48 89 e5             	mov    %rsp,%rbp
 684:	b8 00 00 00 00       	mov    $0x0,%eax
 689:	e8 07 00 00 00       	callq  695 <swap>
 68e:	b8 00 00 00 00       	mov    $0x0,%eax
 693:	5d                   	pop    %rbp
 694:	c3                   	retq   

0000000000000695 <swap>:
 695:	55                   	push   %rbp
 696:	48 89 e5             	mov    %rsp,%rbp
 699:	48 8d 05 8c 09 20 00 	lea    0x20098c(%rip),%rax        # 20102c <buf+0x4>
 6a0:	48 89 05 99 09 20 00 	mov    %rax,0x200999(%rip)        # 201040 <bufp1>
 6a7:	48 8b 05 82 09 20 00 	mov    0x200982(%rip),%rax        # 201030 <bufp0>
 6ae:	8b 00                	mov    (%rax),%eax
 6b0:	89 45 fc             	mov    %eax,-0x4(%rbp)
 6b3:	48 8b 05 76 09 20 00 	mov    0x200976(%rip),%rax        # 201030 <bufp0>
 6ba:	48 8b 15 7f 09 20 00 	mov    0x20097f(%rip),%rdx        # 201040 <bufp1>
 6c1:	8b 12                	mov    (%rdx),%edx
 6c3:	89 10                	mov    %edx,(%rax)
 6c5:	48 8b 05 74 09 20 00 	mov    0x200974(%rip),%rax        # 201040 <bufp1>
 6cc:	8b 55 fc             	mov    -0x4(%rbp),%edx
 6cf:	89 10                	mov    %edx,(%rax)
 6d1:	90                   	nop
 6d2:	5d                   	pop    %rbp
 6d3:	c3                   	retq   
 6d4:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
 6db:	00 00 00 
 6de:	66 90                	xchg   %ax,%ax

00000000000006e0 <__libc_csu_init>:
 6e0:	41 57                	push   %r15
 6e2:	41 56                	push   %r14
 6e4:	41 89 ff             	mov    %edi,%r15d
 6e7:	41 55                	push   %r13
 6e9:	41 54                	push   %r12
 6eb:	4c 8d 25 16 07 20 00 	lea    0x200716(%rip),%r12        # 200e08 <__frame_dummy_init_array_entry>
 6f2:	55                   	push   %rbp
 6f3:	48 8d 2d 16 07 20 00 	lea    0x200716(%rip),%rbp        # 200e10 <__init_array_end>
 6fa:	53                   	push   %rbx
 6fb:	49 89 f6             	mov    %rsi,%r14
 6fe:	49 89 d5             	mov    %rdx,%r13
 701:	4c 29 e5             	sub    %r12,%rbp
 704:	48 83 ec 08          	sub    $0x8,%rsp
 708:	48 c1 fd 03          	sar    $0x3,%rbp
 70c:	e8 ff fd ff ff       	callq  510 <_init>
 711:	48 85 ed             	test   %rbp,%rbp
 714:	74 20                	je     736 <__libc_csu_init+0x56>
 716:	31 db                	xor    %ebx,%ebx
 718:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
 71f:	00 
 720:	4c 89 ea             	mov    %r13,%rdx
 723:	4c 89 f6             	mov    %r14,%rsi
 726:	44 89 ff             	mov    %r15d,%edi
 729:	41 ff 14 dc          	callq  *(%r12,%rbx,8)
 72d:	48 83 c3 01          	add    $0x1,%rbx
 731:	48 39 dd             	cmp    %rbx,%rbp
 734:	75 ea                	jne    720 <__libc_csu_init+0x40>
 736:	48 83 c4 08          	add    $0x8,%rsp
 73a:	5b                   	pop    %rbx
 73b:	5d                   	pop    %rbp
 73c:	41 5c                	pop    %r12
 73e:	41 5d                	pop    %r13
 740:	41 5e                	pop    %r14
 742:	41 5f                	pop    %r15
 744:	c3                   	retq   
 745:	90                   	nop
 746:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
 74d:	00 00 00 

0000000000000750 <__libc_csu_fini>:
 750:	f3 c3                	repz retq 

Disassembly of section .fini:

0000000000000754 <_fini>:
 754:	48 83 ec 08          	sub    $0x8,%rsp
 758:	48 83 c4 08          	add    $0x8,%rsp
 75c:	c3                   	retq   
