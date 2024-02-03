	.file	"bstr_i.c"
	.text
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"01"
	.text
	.p2align 4
	.globl	bstr_i
	.type	bstr_i, @function
bstr_i:
.LFB50:
	.cfi_startproc
	endbr64
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	movq	%rdi, %r13
	pushq	%r12
	.cfi_def_cfa_offset 24
	.cfi_offset 12, -24
	xorl	%r12d, %r12d
	pushq	%rbp
	.cfi_def_cfa_offset 32
	.cfi_offset 6, -32
	leaq	.LC0(%rip), %rbp
	pushq	%rbx
	.cfi_def_cfa_offset 40
	.cfi_offset 3, -40
	subq	$8, %rsp
	.cfi_def_cfa_offset 48
	testq	%rdi, %rdi
	jne	.L2
	jmp	.L1
	.p2align 4,,10
	.p2align 3
.L13:
	movsbl	%al, %ebx
	movq	%rbp, %rdi
	movl	%ebx, %esi
	call	strchr@PLT
	testq	%rax, %rax
	je	.L1
	movl	%ebx, %eax
	addl	%r12d, %r12d
	addq	$1, %r13
	andl	$1, %eax
	orl	%eax, %r12d
.L2:
	movzbl	0(%r13), %eax
	testb	%al, %al
	jne	.L13
.L1:
	addq	$8, %rsp
	.cfi_def_cfa_offset 40
	movl	%r12d, %eax
	popq	%rbx
	.cfi_def_cfa_offset 32
	popq	%rbp
	.cfi_def_cfa_offset 24
	popq	%r12
	.cfi_def_cfa_offset 16
	popq	%r13
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE50:
	.size	bstr_i, .-bstr_i
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
