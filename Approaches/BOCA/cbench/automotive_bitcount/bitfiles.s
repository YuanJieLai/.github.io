	.file	"bitfiles.c"
	.text
	.p2align 4
	.globl	bfopen
	.type	bfopen, @function
bfopen:
.LFB50:
	.cfi_startproc
	endbr64
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	movq	%rsi, %r13
	pushq	%r12
	.cfi_def_cfa_offset 24
	.cfi_offset 12, -24
	pushq	%rbp
	.cfi_def_cfa_offset 32
	.cfi_offset 6, -32
	movq	%rdi, %rbp
	movl	$16, %edi
	call	malloc@PLT
	movq	%rax, %r12
	testq	%rax, %rax
	je	.L1
	movq	%r13, %rsi
	movq	%rbp, %rdi
	call	fopen@PLT
	movq	%rax, (%r12)
	testq	%rax, %rax
	je	.L9
	movb	$0, 9(%r12)
	movb	$0, 11(%r12)
.L1:
	movq	%r12, %rax
	popq	%rbp
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%r12
	.cfi_def_cfa_offset 16
	popq	%r13
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L9:
	.cfi_restore_state
	movq	%r12, %rdi
	xorl	%r12d, %r12d
	call	free@PLT
	jmp	.L1
	.cfi_endproc
.LFE50:
	.size	bfopen, .-bfopen
	.p2align 4
	.globl	bfread
	.type	bfread, @function
bfread:
.LFB51:
	.cfi_startproc
	endbr64
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
	movzbl	9(%rdi), %edx
	movq	%rdi, %rbx
	testb	%dl, %dl
	je	.L11
	movsbl	8(%rdi), %eax
	subl	$1, %edx
	movsbl	%dl, %ecx
	movb	%dl, 9(%rbx)
	popq	%rbx
	.cfi_remember_state
	.cfi_def_cfa_offset 8
	sarl	%cl, %eax
	andl	$1, %eax
	ret
	.p2align 4,,10
	.p2align 3
.L11:
	.cfi_restore_state
	movq	(%rdi), %rdi
	call	fgetc@PLT
	movl	$7, %ecx
	movl	%eax, %edx
	movsbl	%al, %eax
	movb	%dl, 8(%rbx)
	sarl	%cl, %eax
	movl	$7, %edx
	movb	%dl, 9(%rbx)
	andl	$1, %eax
	popq	%rbx
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE51:
	.size	bfread, .-bfread
	.p2align 4
	.globl	bfwrite
	.type	bfwrite, @function
bfwrite:
.LFB52:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsi, %rbp
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	movl	%edi, %ebx
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	movzbl	11(%rsi), %eax
	movsbl	10(%rsi), %edi
	cmpb	$8, %al
	je	.L15
	addl	$1, %eax
.L16:
	addl	%edi, %edi
	andl	$1, %ebx
	movb	%al, 11(%rbp)
	orl	%edi, %ebx
	movb	%bl, 10(%rbp)
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L15:
	.cfi_restore_state
	movq	(%rsi), %rsi
	call	fputc@PLT
	movsbl	10(%rbp), %edi
	movl	$1, %eax
	jmp	.L16
	.cfi_endproc
.LFE52:
	.size	bfwrite, .-bfwrite
	.p2align 4
	.globl	bfclose
	.type	bfclose, @function
bfclose:
.LFB53:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rdi, %rbp
	movq	(%rdi), %rdi
	call	fclose@PLT
	movq	%rbp, %rdi
	popq	%rbp
	.cfi_def_cfa_offset 8
	jmp	free@PLT
	.cfi_endproc
.LFE53:
	.size	bfclose, .-bfclose
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
