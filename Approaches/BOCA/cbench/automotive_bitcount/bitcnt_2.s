	.file	"bitcnt_2.c"
	.text
	.p2align 4
	.globl	bitcount
	.type	bitcount, @function
bitcount:
.LFB50:
	.cfi_startproc
	endbr64
	movq	%rdi, %rcx
	andl	$1431655765, %edi
	sarq	%rcx
	movq	%rcx, %rax
	andl	$1431655765, %eax
	leaq	(%rax,%rdi), %rcx
	movq	%rcx, %rax
	andl	$858993459, %ecx
	sarq	$2, %rax
	andl	$858993459, %eax
	addq	%rax, %rcx
	movq	%rcx, %rdx
	andl	$252645135, %ecx
	sarq	$4, %rdx
	movq	%rdx, %rax
	andl	$252645135, %eax
	leaq	(%rax,%rcx), %rdx
	movq	%rdx, %rcx
	andl	$16711935, %edx
	sarq	$8, %rcx
	andl	$16711935, %ecx
	addq	%rcx, %rdx
	movq	%rdx, %rax
	movzwl	%dx, %edx
	sarq	$16, %rax
	addq	%rdx, %rax
	ret
	.cfi_endproc
.LFE50:
	.size	bitcount, .-bitcount
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
