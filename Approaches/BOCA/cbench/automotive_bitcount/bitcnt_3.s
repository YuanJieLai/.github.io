	.file	"bitcnt_3.c"
	.text
	.p2align 4
	.globl	ntbl_bitcount
	.type	ntbl_bitcount, @function
ntbl_bitcount:
.LFB50:
	.cfi_startproc
	endbr64
	movq	%rdi, %rax
	movq	%rdi, %rcx
	leaq	bits(%rip), %rdx
	shrq	$4, %rax
	andl	$15, %ecx
	andl	$15, %eax
	movsbl	(%rdx,%rcx), %ecx
	movsbl	(%rdx,%rax), %eax
	addl	%ecx, %eax
	movq	%rdi, %rcx
	shrq	$8, %rcx
	andl	$15, %ecx
	movsbl	(%rdx,%rcx), %ecx
	addl	%ecx, %eax
	movq	%rdi, %rcx
	shrq	$12, %rcx
	andl	$15, %ecx
	movsbl	(%rdx,%rcx), %ecx
	addl	%ecx, %eax
	movq	%rdi, %rcx
	shrq	$16, %rcx
	andl	$15, %ecx
	movsbl	(%rdx,%rcx), %ecx
	addl	%ecx, %eax
	movq	%rdi, %rcx
	shrq	$20, %rcx
	andl	$15, %ecx
	movsbl	(%rdx,%rcx), %ecx
	addl	%ecx, %eax
	movq	%rdi, %rcx
	shrl	$28, %edi
	shrq	$24, %rcx
	andl	$15, %ecx
	movsbl	(%rdx,%rcx), %ecx
	movsbl	(%rdx,%rdi), %edx
	addl	%ecx, %eax
	addl	%edx, %eax
	ret
	.cfi_endproc
.LFE50:
	.size	ntbl_bitcount, .-ntbl_bitcount
	.p2align 4
	.globl	BW_btbl_bitcount
	.type	BW_btbl_bitcount, @function
BW_btbl_bitcount:
.LFB51:
	.cfi_startproc
	endbr64
	movq	%rdi, %rdx
	leaq	bits(%rip), %rcx
	movzbl	%dil, %eax
	movzbl	%dh, %esi
	movsbl	(%rcx,%rax), %eax
	shrq	$16, %rdx
	movsbl	(%rcx,%rsi), %esi
	movzbl	%dl, %edx
	movsbl	(%rcx,%rdx), %edx
	addl	%esi, %eax
	movl	%edi, %esi
	shrl	$24, %esi
	movsbl	(%rcx,%rsi), %esi
	addl	%esi, %eax
	addl	%edx, %eax
	ret
	.cfi_endproc
.LFE51:
	.size	BW_btbl_bitcount, .-BW_btbl_bitcount
	.p2align 4
	.globl	AR_btbl_bitcount
	.type	AR_btbl_bitcount, @function
AR_btbl_bitcount:
.LFB52:
	.cfi_startproc
	endbr64
	movq	%rdi, %rdx
	leaq	bits(%rip), %rcx
	movzbl	%dil, %eax
	movzbl	%dh, %esi
	movsbl	(%rcx,%rax), %eax
	shrl	$24, %edx
	movsbl	(%rcx,%rsi), %esi
	addl	%eax, %esi
	movq	%rdi, %rax
	shrq	$16, %rax
	movzbl	%al, %eax
	movsbl	(%rcx,%rax), %eax
	addl	%eax, %esi
	movsbl	(%rcx,%rdx), %eax
	addl	%esi, %eax
	ret
	.cfi_endproc
.LFE52:
	.size	AR_btbl_bitcount, .-AR_btbl_bitcount
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
