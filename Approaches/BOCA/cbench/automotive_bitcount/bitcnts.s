	.file	"bitcnts.c"
	.text
	.p2align 4
	.type	bit_shifter, @function
bit_shifter:
.LFB62:
	.cfi_startproc
	endbr64
	xorl	%r8d, %r8d
	testq	%rdi, %rdi
	je	.L1
	xorl	%eax, %eax
	.p2align 4,,10
	.p2align 3
.L3:
	movl	%edi, %edx
	addl	$1, %eax
	andl	$1, %edx
	addl	%edx, %r8d
	sarq	%rdi
	je	.L1
	cmpl	$63, %eax
	jbe	.L3
.L1:
	movl	%r8d, %eax
	ret
	.cfi_endproc
.LFE62:
	.size	bit_shifter, .-bit_shifter
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"Usage: bitcnts <iterations>\n"
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align 8
.LC1:
	.string	"Bit counter algorithm benchmark\n"
	.section	.rodata.str1.1
.LC2:
	.string	"%-38s> Bits: %ld\n"
	.text
	.p2align 4
	.globl	main1
	.type	main1, @function
main1:
.LFB61:
	.cfi_startproc
	endbr64
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$24, %rsp
	.cfi_def_cfa_offset 80
	movl	%edx, 8(%rsp)
	cmpl	$1, %edi
	jle	.L30
	movq	8(%rsi), %rdi
	movl	$10, %edx
	xorl	%esi, %esi
	call	strtol@PLT
	movl	8(%rsp), %ecx
	movl	%eax, 12(%rsp)
	movq	%rax, %rbx
	testl	%ecx, %ecx
	jne	.L31
.L13:
	movslq	%ebx, %rax
	leaq	text.4357(%rip), %r13
	leaq	pBitCntFunc.4356(%rip), %r14
	leaq	(%rax,%rax,2), %rdx
	leaq	1(%rax,%rdx,4), %rbp
	.p2align 4,,10
	.p2align 3
.L16:
	movl	12(%rsp), %eax
	xorl	%r12d, %r12d
	testl	%eax, %eax
	jle	.L19
	movq	(%r14), %rbx
	movl	$1, %r15d
	xorl	%r12d, %r12d
	.p2align 4,,10
	.p2align 3
.L14:
	movq	%r15, %rdi
	addq	$13, %r15
	call	*%rbx
	cltq
	addq	%rax, %r12
	cmpq	%rbp, %r15
	jne	.L14
.L19:
	movl	8(%rsp), %edx
	testl	%edx, %edx
	jne	.L32
.L15:
	addq	$8, %r13
	leaq	56+text.4357(%rip), %rax
	addq	$8, %r14
	cmpq	%rax, %r13
	jne	.L16
	addq	$24, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	xorl	%eax, %eax
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L32:
	.cfi_restore_state
	movq	0(%r13), %rdx
	movq	%r12, %rcx
	leaq	.LC2(%rip), %rsi
	xorl	%eax, %eax
	movl	$1, %edi
	call	__printf_chk@PLT
	jmp	.L15
.L31:
	leaq	.LC1(%rip), %rdi
	call	puts@PLT
	jmp	.L13
.L30:
	movq	stderr(%rip), %rcx
	movl	$28, %edx
	movl	$1, %esi
	leaq	.LC0(%rip), %rdi
	call	fwrite@PLT
	movl	$1, %edi
	call	exit@PLT
	.cfi_endproc
.LFE61:
	.size	main1, .-main1
	.section	.rodata.str1.1
.LC3:
	.string	"Optimized 1 bit/loop counter"
.LC4:
	.string	"Ratko's mystery algorithm"
	.section	.rodata.str1.8
	.align 8
.LC5:
	.string	"Recursive bit count by nybbles"
	.align 8
.LC6:
	.string	"Non-recursive bit count by nybbles"
	.align 8
.LC7:
	.string	"Non-recursive bit count by bytes (BW)"
	.align 8
.LC8:
	.string	"Non-recursive bit count by bytes (AR)"
	.section	.rodata.str1.1
.LC9:
	.string	"Shift and count bits"
	.section	.data.rel.ro.local,"aw"
	.align 32
	.type	text.4357, @object
	.size	text.4357, 56
text.4357:
	.quad	.LC3
	.quad	.LC4
	.quad	.LC5
	.quad	.LC6
	.quad	.LC7
	.quad	.LC8
	.quad	.LC9
	.section	.data.rel.ro,"aw"
	.align 32
	.type	pBitCntFunc.4356, @object
	.size	pBitCntFunc.4356, 56
pBitCntFunc.4356:
	.quad	bit_count
	.quad	bitcount
	.quad	ntbl_bitcnt
	.quad	ntbl_bitcount
	.quad	BW_btbl_bitcount
	.quad	AR_btbl_bitcount
	.quad	bit_shifter
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
