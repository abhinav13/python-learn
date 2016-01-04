.global  divby
       
        .text
main:
	mov	$2, %rsi 
	mov 	$4, %rdi
        mov     %rdi, %rax              # move dividend to rax
        div     %rsi              # is x less than y?
	#mov 	%rdx, %eax		# remainder will be in eax
        ret                             # the max will be in eax
