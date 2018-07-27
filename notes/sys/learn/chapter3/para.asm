
a.out：     文件格式 elf64-x86-64


Disassembly of section .init:

00000000000004f8 <_init>:
 4f8:	48 83 ec 08          	sub    $0x8,%rsp
 4fc:	48 8b 05 dd 0a 20 00 	mov    0x200add(%rip),%rax        # 200fe0 <__gmon_start__>
 503:	48 85 c0             	test   %rax,%rax
 506:	74 02                	je     50a <_init+0x12>
 508:	ff d0                	callq  *%rax
 50a:	48 83 c4 08          	add    $0x8,%rsp
 50e:	c3                   	retq   

Disassembly of section .plt:

0000000000000510 <.plt>:
 510:	ff 35 f2 0a 20 00    	pushq  0x200af2(%rip)        # 201008 <_GLOBAL_OFFSET_TABLE_+0x8>
 516:	ff 25 f4 0a 20 00    	jmpq   *0x200af4(%rip)        # 201010 <_GLOBAL_OFFSET_TABLE_+0x10>
 51c:	0f 1f 40 00          	nopl   0x0(%rax)

Disassembly of section .plt.got:

0000000000000520 <.plt.got>:
 520:	ff 25 d2 0a 20 00    	jmpq   *0x200ad2(%rip)        # 200ff8 <__cxa_finalize@GLIBC_2.2.5>
 526:	66 90                	xchg   %ax,%ax

Disassembly of section .text:

0000000000000530 <_start>:
 530:	31 ed                	xor    %ebp,%ebp
 532:	49 89 d1             	mov    %rdx,%r9
 535:	5e                   	pop    %rsi
 536:	48 89 e2             	mov    %rsp,%rdx
 539:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
 53d:	50                   	push   %rax
 53e:	54                   	push   %rsp
 53f:	4c 8d 05 da 01 00 00 	lea    0x1da(%rip),%r8        # 720 <__libc_csu_fini>
 546:	48 8d 0d 63 01 00 00 	lea    0x163(%rip),%rcx        # 6b0 <__libc_csu_init>
 54d:	48 8d 3d 2d 01 00 00 	lea    0x12d(%rip),%rdi        # 681 <main>
 554:	ff 15 7e 0a 20 00    	callq  *0x200a7e(%rip)        # 200fd8 <__libc_start_main@GLIBC_2.2.5>
 55a:	f4                   	hlt    
 55b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000000560 <deregister_tm_clones>:
 560:	48 8d 3d c1 0a 20 00 	lea    0x200ac1(%rip),%rdi        # 201028 <__TMC_END__>
 567:	48 8d 05 c1 0a 20 00 	lea    0x200ac1(%rip),%rax        # 20102f <__TMC_END__+0x7>
 56e:	55                   	push   %rbp
 56f:	48 29 f8             	sub    %rdi,%rax
 572:	48 89 e5             	mov    %rsp,%rbp
 575:	48 83 f8 0e          	cmp    $0xe,%rax
 579:	76 15                	jbe    590 <deregister_tm_clones+0x30>
 57b:	48 8b 05 4e 0a 20 00 	mov    0x200a4e(%rip),%rax        # 200fd0 <_ITM_deregisterTMCloneTable>
 582:	48 85 c0             	test   %rax,%rax
 585:	74 09                	je     590 <deregister_tm_clones+0x30>
 587:	5d                   	pop    %rbp
 588:	ff e0                	jmpq   *%rax
 58a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
 590:	5d                   	pop    %rbp
 591:	c3                   	retq   
 592:	0f 1f 40 00          	nopl   0x0(%rax)
 596:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
 59d:	00 00 00 

00000000000005a0 <register_tm_clones>:
 5a0:	48 8d 3d 81 0a 20 00 	lea    0x200a81(%rip),%rdi        # 201028 <__TMC_END__>
 5a7:	48 8d 35 7a 0a 20 00 	lea    0x200a7a(%rip),%rsi        # 201028 <__TMC_END__>
 5ae:	55                   	push   %rbp
 5af:	48 29 fe             	sub    %rdi,%rsi
 5b2:	48 89 e5             	mov    %rsp,%rbp
 5b5:	48 c1 fe 03          	sar    $0x3,%rsi
 5b9:	48 89 f0             	mov    %rsi,%rax
 5bc:	48 c1 e8 3f          	shr    $0x3f,%rax
 5c0:	48 01 c6             	add    %rax,%rsi
 5c3:	48 d1 fe             	sar    %rsi
 5c6:	74 18                	je     5e0 <register_tm_clones+0x40>
 5c8:	48 8b 05 21 0a 20 00 	mov    0x200a21(%rip),%rax        # 200ff0 <_ITM_registerTMCloneTable>
 5cf:	48 85 c0             	test   %rax,%rax
 5d2:	74 0c                	je     5e0 <register_tm_clones+0x40>
 5d4:	5d                   	pop    %rbp
 5d5:	ff e0                	jmpq   *%rax
 5d7:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
 5de:	00 00 
 5e0:	5d                   	pop    %rbp
 5e1:	c3                   	retq   
 5e2:	0f 1f 40 00          	nopl   0x0(%rax)
 5e6:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
 5ed:	00 00 00 

00000000000005f0 <__do_global_dtors_aux>:
 5f0:	80 3d 31 0a 20 00 00 	cmpb   $0x0,0x200a31(%rip)        # 201028 <__TMC_END__>
 5f7:	75 27                	jne    620 <__do_global_dtors_aux+0x30>
 5f9:	48 83 3d f7 09 20 00 	cmpq   $0x0,0x2009f7(%rip)        # 200ff8 <__cxa_finalize@GLIBC_2.2.5>
 600:	00 
 601:	55                   	push   %rbp
 602:	48 89 e5             	mov    %rsp,%rbp
 605:	74 0c                	je     613 <__do_global_dtors_aux+0x23>
 607:	48 8b 3d 12 0a 20 00 	mov    0x200a12(%rip),%rdi        # 201020 <__dso_handle>
 60e:	e8 0d ff ff ff       	callq  520 <.plt.got>
 613:	e8 48 ff ff ff       	callq  560 <deregister_tm_clones>
 618:	5d                   	pop    %rbp
 619:	c6 05 08 0a 20 00 01 	movb   $0x1,0x200a08(%rip)        # 201028 <__TMC_END__>
 620:	f3 c3                	repz retq 
 622:	0f 1f 40 00          	nopl   0x0(%rax)
 626:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
 62d:	00 00 00 

0000000000000630 <frame_dummy>:
 630:	48 8d 3d e1 07 20 00 	lea    0x2007e1(%rip),%rdi        # 200e18 <__JCR_END__>
 637:	48 83 3f 00          	cmpq   $0x0,(%rdi)
 63b:	75 0b                	jne    648 <frame_dummy+0x18>
 63d:	e9 5e ff ff ff       	jmpq   5a0 <register_tm_clones>
 642:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
 648:	48 8b 05 99 09 20 00 	mov    0x200999(%rip),%rax        # 200fe8 <_Jv_RegisterClasses>
 64f:	48 85 c0             	test   %rax,%rax
 652:	74 e9                	je     63d <frame_dummy+0xd>
 654:	55                   	push   %rbp
 655:	48 89 e5             	mov    %rsp,%rbp
 658:	ff d0                	callq  *%rax
 65a:	5d                   	pop    %rbp
 65b:	e9 40 ff ff ff       	jmpq   5a0 <register_tm_clones>

0000000000000660 <para>:
 660:	55                   	push   %rbp
 661:	48 89 e5             	mov    %rsp,%rbp
 664:	89 7d fc             	mov    %edi,-0x4(%rbp)
 667:	89 75 f8             	mov    %esi,-0x8(%rbp)
 66a:	83 7d fc 01          	cmpl   $0x1,-0x4(%rbp)
 66e:	7e 04                	jle    674 <para+0x14>
 670:	83 45 fc 01          	addl   $0x1,-0x4(%rbp)
 674:	83 7d f8 02          	cmpl   $0x2,-0x8(%rbp)
 678:	7e 04                	jle    67e <para+0x1e>
 67a:	83 45 f8 02          	addl   $0x2,-0x8(%rbp)
 67e:	90                   	nop
 67f:	5d                   	pop    %rbp
 680:	c3                   	retq   

0000000000000681 <main>:
 681:	55                   	push   %rbp
 682:	48 89 e5             	mov    %rsp,%rbp
 685:	48 83 ec 10          	sub    $0x10,%rsp
 689:	89 7d fc             	mov    %edi,-0x4(%rbp)
 68c:	48 89 75 f0          	mov    %rsi,-0x10(%rbp)
 690:	be 02 00 00 00       	mov    $0x2,%esi
 695:	bf 01 00 00 00       	mov    $0x1,%edi
 69a:	e8 c1 ff ff ff       	callq  660 <para>
 69f:	b8 00 00 00 00       	mov    $0x0,%eax
 6a4:	c9                   	leaveq 
 6a5:	c3                   	retq   
 6a6:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
 6ad:	00 00 00 

00000000000006b0 <__libc_csu_init>:
 6b0:	41 57                	push   %r15
 6b2:	41 56                	push   %r14
 6b4:	41 89 ff             	mov    %edi,%r15d
 6b7:	41 55                	push   %r13
 6b9:	41 54                	push   %r12
 6bb:	4c 8d 25 46 07 20 00 	lea    0x200746(%rip),%r12        # 200e08 <__frame_dummy_init_array_entry>
 6c2:	55                   	push   %rbp
 6c3:	48 8d 2d 46 07 20 00 	lea    0x200746(%rip),%rbp        # 200e10 <__init_array_end>
 6ca:	53                   	push   %rbx
 6cb:	49 89 f6             	mov    %rsi,%r14
 6ce:	49 89 d5             	mov    %rdx,%r13
 6d1:	4c 29 e5             	sub    %r12,%rbp
 6d4:	48 83 ec 08          	sub    $0x8,%rsp
 6d8:	48 c1 fd 03          	sar    $0x3,%rbp
 6dc:	e8 17 fe ff ff       	callq  4f8 <_init>
 6e1:	48 85 ed             	test   %rbp,%rbp
 6e4:	74 20                	je     706 <__libc_csu_init+0x56>
 6e6:	31 db                	xor    %ebx,%ebx
 6e8:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
 6ef:	00 
 6f0:	4c 89 ea             	mov    %r13,%rdx
 6f3:	4c 89 f6             	mov    %r14,%rsi
 6f6:	44 89 ff             	mov    %r15d,%edi
 6f9:	41 ff 14 dc          	callq  *(%r12,%rbx,8)
 6fd:	48 83 c3 01          	add    $0x1,%rbx
 701:	48 39 dd             	cmp    %rbx,%rbp
 704:	75 ea                	jne    6f0 <__libc_csu_init+0x40>
 706:	48 83 c4 08          	add    $0x8,%rsp
 70a:	5b                   	pop    %rbx
 70b:	5d                   	pop    %rbp
 70c:	41 5c                	pop    %r12
 70e:	41 5d                	pop    %r13
 710:	41 5e                	pop    %r14
 712:	41 5f                	pop    %r15
 714:	c3                   	retq   
 715:	90                   	nop
 716:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
 71d:	00 00 00 

0000000000000720 <__libc_csu_fini>:
 720:	f3 c3                	repz retq 

Disassembly of section .fini:

0000000000000724 <_fini>:
 724:	48 83 ec 08          	sub    $0x8,%rsp
 728:	48 83 c4 08          	add    $0x8,%rsp
 72c:	c3                   	retq   
