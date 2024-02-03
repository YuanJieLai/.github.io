	.file	"loop-wrap.c"
	.text
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"rt"
.LC1:
	.string	"_finfo_dataset"
.LC2:
	.string	"\nError: Can't find dataset!\n"
.LC3:
	.string	"%ld"
	.section	.text.startup,"ax",@progbits
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB23:
	.cfi_startproc
	endbr64
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	pushq	%r12
	.cfi_def_cfa_offset 24
	.cfi_offset 12, -24
	movq	%rsi, %r12
	leaq	.LC0(%rip), %rsi
	pushq	%rbp
	.cfi_def_cfa_offset 32
	.cfi_offset 6, -32
	movl	%edi, %ebp
	leaq	.LC1(%rip), %rdi
	pushq	%rbx
	.cfi_def_cfa_offset 40
	.cfi_offset 3, -40
	subq	$24, %rsp
	.cfi_def_cfa_offset 64
	movq	%fs:40, %rax
	movq	%rax, 8(%rsp)
	xorl	%eax, %eax
	call	fopen@PLT
	testq	%rax, %rax
	je	.L10
	movq	%rax, %rdi
	movq	%rax, %r13
	movq	%rsp, %rdx
	xorl	%eax, %eax
	leaq	.LC3(%rip), %rsi
	call	__isoc99_fscanf@PLT
	movq	%r13, %rdi
	call	fclose@PLT
	movq	(%rsp), %rax
	testq	%rax, %rax
	jle	.L4
	xorl	%ebx, %ebx
	.p2align 4,,10
	.p2align 3
.L5:
	addq	$1, %rbx
	xorl	%edx, %edx
	movq	%r12, %rsi
	movl	%ebp, %edi
	cmpq	%rax, %rbx
	sete	%dl
	call	main1@PLT
	movq	(%rsp), %rax
	cmpq	%rax, %rbx
	jl	.L5
.L4:
	xorl	%eax, %eax
.L1:
	movq	8(%rsp), %rcx
	xorq	%fs:40, %rcx
	jne	.L11
	addq	$24, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 40
	popq	%rbx
	.cfi_def_cfa_offset 32
	popq	%rbp
	.cfi_def_cfa_offset 24
	popq	%r12
	.cfi_def_cfa_offset 16
	popq	%r13
	.cfi_def_cfa_offset 8
	ret
.L10:
	.cfi_restore_state
	movq	stderr(%rip), %rcx
	movl	$28, %edx
	movl	$1, %esi
	leaq	.LC2(%rip), %rdi
	call	fwrite@PLT
	movl	$1, %eax
	jmp	.L1
.L11:
	call	__stack_chk_fail@PLT
	.cfi_endproc
.LFE23:
	.size	main, .-main
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
