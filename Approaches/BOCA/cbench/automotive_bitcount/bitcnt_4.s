	.file	"bitcnt_4.c"
	.text
	.p2align 4
	.globl	ntbl_bitcnt
	.type	ntbl_bitcnt, @function
ntbl_bitcnt:
.LFB50:
	.cfi_startproc
	endbr64
	movq	%rdi, %rax
	leaq	bits(%rip), %rcx
	andl	$15, %eax
	sarq	$4, %rdi
	movsbl	(%rcx,%rax), %eax
	je	.L1
	xorl	%edx, %edx
	.p2align 4,,10
	.p2align 3
.L3:
	addl	%eax, %edx
	movq	%rdi, %rax
	andl	$15, %eax
	sarq	$4, %rdi
	movsbl	(%rcx,%rax), %eax
	jne	.L3
	addl	%edx, %eax
.L1:
	ret
	.cfi_endproc
.LFE50:
	.size	ntbl_bitcnt, .-ntbl_bitcnt
	.p2align 4
	.globl	btbl_bitcnt
	.type	btbl_bitcnt, @function
btbl_bitcnt:
.LFB51:
	.cfi_startproc
	endbr64
	movzbl	%dil, %eax
	leaq	bits(%rip), %rcx
	sarq	$8, %rdi
	movsbl	(%rcx,%rax), %eax
	je	.L9
	xorl	%edx, %edx
	.p2align 4,,10
	.p2align 3
.L11:
	addl	%eax, %edx
	movzbl	%dil, %eax
	sarq	$8, %rdi
	movsbl	(%rcx,%rax), %eax
	jne	.L11
	addl	%edx, %eax
.L9:
	ret
	.cfi_endproc
.LFE51:
	.size	btbl_bitcnt, .-btbl_bitcnt
	.section	.rodata
	.align 32
	.type	bits, @object
	.size	bits, 256
bits:
	.string	""
	.ascii	"\001\001\002\001\002\002\003\001\002\002\003\002\003\003\004"
	.ascii	"\001\002\002\003\002\003\003\004\002\003\003\004\003\004\004"
	.ascii	"\005\001\002\002\003\002\003\003\004\002\003\003\004\003\004"
	.ascii	"\004\005\002\003\003\004\003\004\004\005\003\004\004\005\004"
	.ascii	"\005\005\006\001\002\002\003\002\003\003\004\002\003\003\004"
	.ascii	"\003\004\004\005\002\003\003\004\003\004\004\005\003\004\004"
	.ascii	"\005\004\005\005\006\002\003\003\004\003\004\004\005\003\004"
	.ascii	"\004\005\004\005\005\006\003\004\004\005\004\005\005\006\004"
	.ascii	"\005\005\006\005\006\006\007\001\002\002\003\002\003\003\004"
	.ascii	"\002\003\003\004\003\004\004\005\002\003\003\004\003\004\004"
	.ascii	"\005\003\004\004\005\004\005\005\006\002\003\003\004\003\004"
	.ascii	"\004\005\003\004\004\005\004\005\005\006\003\004\004\005\004"
	.ascii	"\005\005\006\004\005\005\006\005\006\006\007\002\003\003\004"
	.ascii	"\003\004\004\005\003\004\004\005\004\005\005\006\003\004\004"
	.ascii	"\005\004\005\005\006\004\005\005\006\005\006\006\007\003\004"
	.ascii	"\004\005\004\005\005\006\004\005\005\006\005\006\006\007\004"
	.ascii	"\005\005\006\005\006\006\007\005\006\006\007\006\007\007\b"
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1~20.04) 9.4.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
