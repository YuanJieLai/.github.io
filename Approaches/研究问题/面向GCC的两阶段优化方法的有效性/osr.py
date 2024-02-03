def opa(Sb_len,opa_inter):
    i_opa=opa_inter/Sb_len
    return i_opa
def osr(Sw_len,osr_inter):
    i_osr=osr_inter/Sw_len
    return i_osr
Sb=['-fno-peephole2', '-fno-schedule-insns2', '-fno-tree-pre', '-ftracer', '-fno-reorder-functions', '-fno-tree-ter', '-fno-ivopts', '-fno-tree-coalesce-vars', '-fno-cprop-registers', '-fno-gcse', '-fno-crossjumping', '-fno-tree-fre', '-fno-if-conversion2', '-fno-expensive-optimizations']



Sw=['-fgcse-after-reload', '-finline-functions', '-fipa-cp-clone', '-floop-interchange', '-floop-unroll-and-jam', '-fpeel-loops', '-fpredictive-commoning', '-fsplit-loops', '-fsplit-paths', '-ftree-loop-distribute-patterns', '-ftree-loop-distribution', '-ftree-loop-vectorize', '-ftree-partial-pre', '-ftree-slp-vectorize', '-funswitch-loops', '-fversion-loops-for-strides', '-ffast-math', '-fno-caller-saves', '-funroll-all-loops', '-fno-inline-small-functions', '-finline-functions', '-fno-math-errno', '-fno-dce', '-fipa-cp-clone', '-fno-move-loop-invariants', '-fno-regmove', '-funsafe-math-optimizations', '-fno-tree-loop-optimize', '-fno-merge-constants', '-fno-omit-frame-pointer', '-fno-align-labels', '-fno-tree-dse', '-fwrapv', '-fgcse-after-reload', '-fno-align-jumps', '-fno-asynchronous-unwind-tables', '-fno-cse-follow-jumps', '-fno-guess-branch-probability', '-fprefetch-loop-arrays', '-fno-common', '-fpredictive-commoning', '-fno-unit-at-a-time', '-fno-early-inlining', '-fno-delete-null-pointer-checks', '-fselective-scheduling2', '-fno-inline-functions-called-once', '-funswitch-loops', '-fno-tree-vrp', '-fno-tree-dce', '-fno-jump-tables', '-ftree-vectorize', '-fno-argument-alias', '-fno-schedule-insns', '-fno-branch-count-reg', '-fno-tree-switch-conversion', '-fno-auto-inc-dec', '-fno-tree-reassoc', '-fno-align-functions', '-fno-defer-pop', '-fno-optimize-register-move', '-fno-strict-aliasing', '-fno-rerun-cse-after-loop', '-fno-tree-ccp', '-fno-ipa-cp', '-fno-tree-sra', '-fno-tree-copyrename', '-fno-ipa-reference', '-fno-ipa-pure-const', '-fno-thread-jumps', '-fno-if-conversion', '-fno-reorder-blocks', '-falign-loops']

op=['-fgcse-after-reload', '-finline-functions', '-fipa-cp-clone', '-floop-interchange', '-floop-unroll-and-jam', '-fpredictive-commoning', '-fsplit-loops', '-fsplit-paths', '-ftree-loop-distribute-patterns', '-ftree-loop-distribution', '-ftree-loop-vectorize', '-ftree-partial-pre', '-ftree-slp-vectorize', '-fversion-loops-for-strides', '-fno-peephole2', '-ffast-math', '-fno-caller-saves', '-funroll-all-loops', '-fno-inline-small-functions', '-finline-functions', '-fno-math-errno', '-fno-tree-pre', '-ftracer', '-fno-reorder-functions', '-fno-dce', '-fipa-cp-clone', '-fno-move-loop-invariants', '-fno-regmove', '-funsafe-math-optimizations', '-fno-tree-loop-optimize', '-fno-merge-constants', '-fno-omit-frame-pointer', '-fno-tree-ter', '-fwrapv', '-fgcse-after-reload', '-fno-align-jumps', '-fno-asynchronous-unwind-tables', '-fno-cse-follow-jumps', '-fno-ivopts', '-fprefetch-loop-arrays', '-fno-tree-coalesce-vars', '-fno-common', '-fpredictive-commoning', '-fno-unit-at-a-time', '-fno-cprop-registers', '-fno-early-inlining', '-fno-delete-null-pointer-checks', '-fselective-scheduling2', '-fno-gcse', '-fno-inline-functions-called-once', '-funswitch-loops', '-fno-tree-dce', '-fno-jump-tables', '-ftree-vectorize', '-fno-argument-alias', '-fno-schedule-insns', '-fno-branch-count-reg', '-fno-tree-switch-conversion', '-fno-auto-inc-dec', '-fno-tree-fre', '-fno-tree-reassoc', '-fno-align-functions', '-fno-defer-pop', '-fno-optimize-register-move', '-fno-strict-aliasing', '-fno-rerun-cse-after-loop', '-fno-ipa-cp', '-fno-ipa-reference', '-fno-thread-jumps', '-fno-reorder-blocks', '-falign-loops']

op_c=['-fpeel-loops', '-funswitch-loops', '-fno-schedule-insns2', '-fno-align-labels', '-fno-tree-dse', '-fno-guess-branch-probability', '-fno-tree-vrp', '-fno-crossjumping', '-fno-tree-ccp', '-fno-if-conversion2', '-fno-tree-sra', '-fno-expensive-optimizations', '-fno-tree-copyrename', '-fno-ipa-pure-const', '-fno-if-conversion']

























inter_b=set(Sb)&set(op)
inter_w=set(Sw)&set(op_c)
print(opa(len(Sb),len(inter_b)))
print(osr(len(Sw),len(inter_w)))
