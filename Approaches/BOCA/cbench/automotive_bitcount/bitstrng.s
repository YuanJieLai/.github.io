	.file	"bitstrng.c"
	.text
	.p2align 4
	.globl	bitstring
	.type	bitstring, @function
bitstring:
.LFB50:
	.cfi_startproc
	endbr64
	movl	%edx, %eax
	xorl	%r8d, %r8d
	sarl	$2, %eax
	addl	%edx, %eax
	testb	$3, %dl
	sete	%r8b
	subl	%r8d, %eax
	subl	%eax, %ecx
	testl	%ecx, %ecx
	jle	.L7
	leal	-1(%rcx), %eax
	leaq	1(%rdi,%rax), %r8
	.p2align 4,,10
	.p2align 3
.L3:
	addq	$1, %rdi
	movb	$32, -1(%rdi)
	cmpq	%r8, %rdi
	jne	.L3
.L2:
	subl	$1, %edx
	movl	%edx, %ecx
	jns	.L6
	jmp	.L8
	.p2align 4,,10
	.p2align 3
.L16:
	testl	%ecx, %ecx
	je	.L4
	movb	$32, 1(%r8)
	addq	$2, %r8
.L5:
	subl	$1, %ecx
	cmpl	$-1, %ecx
	je	.L8
.L6:
	movq	%rsi, %rax
	leaq	1(%r8), %rdx
	sarq	%cl, %rax
	andl	$1, %eax
	addl	$48, %eax
	movb	%al, (%r8)
	testb	$3, %cl
	je	.L16
	movq	%rdx, %r8
	jmp	.L5
	.p2align 4,,10
	.p2align 3
.L8:
	movq	%r8, %rdx
.L4:
	movb	$0, (%rdx)
	ret
	.p2align 4,,10
	.p2align 3
.L7:
	movq	%rdi, %r8
	jmp	.L2
	.cfi_endproc
.LFE50:
	.size	bitstring, .-bitstring
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
