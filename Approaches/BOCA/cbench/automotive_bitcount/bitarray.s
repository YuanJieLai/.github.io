	.file	"bitarray.c"
	.text
	.p2align 4
	.globl	alloc_bit_array
	.type	alloc_bit_array, @function
alloc_bit_array:
.LFB50:
	.cfi_startproc
	endbr64
	addq	$7, %rdi
	movl	$1, %esi
	shrq	$3, %rdi
	jmp	calloc@PLT
	.cfi_endproc
.LFE50:
	.size	alloc_bit_array, .-alloc_bit_array
	.p2align 4
	.globl	getbit
	.type	getbit, @function
getbit:
.LFB51:
	.cfi_startproc
	endbr64
	testl	%esi, %esi
	leal	7(%rsi), %eax
	movl	%esi, %edx
	cmovns	%esi, %eax
	sarl	$31, %edx
	shrl	$29, %edx
	sarl	$3, %eax
	leal	(%rsi,%rdx), %ecx
	cltq
	andl	$7, %ecx
	movsbl	(%rdi,%rax), %eax
	subl	%edx, %ecx
	sarl	%cl, %eax
	andl	$1, %eax
	ret
	.cfi_endproc
.LFE51:
	.size	getbit, .-getbit
	.p2align 4
	.globl	setbit
	.type	setbit, @function
setbit:
.LFB52:
	.cfi_startproc
	endbr64
	testl	%esi, %esi
	movq	%rdi, %r8
	leal	7(%rsi), %edi
	movl	$1, %eax
	cmovns	%esi, %edi
	sarl	$3, %edi
	movslq	%edi, %rdi
	addq	%r8, %rdi
	movl	%esi, %r8d
	sarl	$31, %r8d
	movzbl	(%rdi), %r9d
	shrl	$29, %r8d
	leal	(%rsi,%r8), %ecx
	andl	$7, %ecx
	subl	%r8d, %ecx
	sall	%cl, %eax
	movl	%r9d, %ecx
	orl	%eax, %ecx
	notl	%eax
	andl	%r9d, %eax
	testl	%edx, %edx
	cmovne	%ecx, %eax
	movb	%al, (%rdi)
	ret
	.cfi_endproc
.LFE52:
	.size	setbit, .-setbit
	.p2align 4
	.globl	flipbit
	.type	flipbit, @function
flipbit:
.LFB53:
	.cfi_startproc
	endbr64
	testl	%esi, %esi
	leal	7(%rsi), %eax
	movl	%esi, %edx
	cmovns	%esi, %eax
	sarl	$31, %edx
	shrl	$29, %edx
	leal	(%rsi,%rdx), %ecx
	sarl	$3, %eax
	andl	$7, %ecx
	cltq
	subl	%edx, %ecx
	movl	$1, %edx
	sall	%cl, %edx
	xorb	%dl, (%rdi,%rax)
	ret
	.cfi_endproc
.LFE53:
	.size	flipbit, .-flipbit
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
