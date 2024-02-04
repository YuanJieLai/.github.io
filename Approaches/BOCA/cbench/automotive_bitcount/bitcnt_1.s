	.file	"bitcnt_1.c"
	.text
	.p2align 4
	.globl	bit_count
	.type	bit_count, @function
bit_count:
.LFB50:
	.cfi_startproc
	endbr64
	xorl	%r8d, %r8d
	testq	%rdi, %rdi
	jne	.L3
.L1:
	movl	%r8d, %eax
	ret
	.p2align 4,,10
	.p2align 3
.L3:
	leaq	-1(%rdi), %rax
	addl	$1, %r8d
	andq	%rax, %rdi
	je	.L1
	leaq	-1(%rdi), %rax
	addl	$1, %r8d
	andq	%rax, %rdi
	jne	.L3
	jmp	.L1
	.cfi_endproc
.LFE50:
	.size	bit_count, .-bit_count
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
