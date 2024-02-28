
opt1="1 1 0 0 0 0 1 1 1 0 1 1 0 0 0 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 1 0 1 1 1 0 1 0 0 1 1 0 0 1 0 1 1 1 1 1 0 0 1 1 1 1 1 1 0 1 0 1 1 1 0 0 0 1 1 1 0 0 0 0 0 0 1 1 0 0 0 0 1 0 1"
opt2="0 0 0 0 1 0 0 1 1 0 1 1 1 0 0 0 1 0 0 1 1 0 0 1 1 0 0 0 1 0 1 0 0 1 1 0 0 0 0 1 0 1 0 0 0 0 1 1 1 0 0 0 1 1 0 1 1 0 1 0 1 0 0 0 1 1 0 0 1 1 1 1 1 0 0 1 0 0 1 0 1 0 1 1 1 1"
opt3="1 1 1 1 1 0 1 0 0 0 1 1 1 0 1 1 1 1 0 1 1 0 1 0 0 1 1 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 1 0 1 1 0 1 1 0 1 1 1 1 0 1 0 0 1 1 0 1 0 0 0 0 0 1 1 0 1 0 0 0 0 0 1 1 0 0 0 1 1 0 0 1"
opt4="1 1 1 0 0 1 1 0 0 0 1 1 0 1 1 1 1 0 0 1 0 1 0 1 0 0 1 1 1 0 0 0 0 0 1 0 0 0 0 1 1 1 1 0 1 0 0 0 1 0 1 0 0 0 1 1 0 1 0 1 1 1 1 0 1 1 1 1 1 1 0 1 1 1 0 1 1 0 1 1 1 0 1 1 0 1"
opt5="0 1 1 0 1 1 0 1 0 0 1 1 1 1 1 1 0 0 0 0 0 0 1 0 1 0 1 1 0 0 1 1 0 1 0 1 1 1 0 1 0 1 1 0 1 1 1 1 0 0 1 1 1 0 1 0 0 1 0 0 1 0 0 1 0 0 0 0 1 1 1 0 1 0 1 0 1 0 1 1 0 0 0 1 1 1"
opt6="1 0 1 1 0 1 0 1 1 0 0 1 1 0 1 1 1 0 0 1 1 1 0 1 0 1 0 0 0 0 1 0 0 1 1 1 0 1 0 0 0 1 1 0 0 1 1 1 0 1 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 1 1 0 1 1 1 1 1 1 1 1 1 0 1 0 0 1 1 1 0 0"
opt7="1 0 0 0 0 0 0 0 1 1 1 1 0 1 1 0 0 1 1 1 1 1 0 1 0 1 0 0 1 0 1 0 0 0 1 0 0 1 0 0 0 1 0 0 1 1 0 1 0 1 0 0 0 1 1 0 0 0 0 1 1 1 1 1 1 1 0 0 1 0 0 1 0 1 0 0 0 0 1 1 0 0 0 1 1 0"
opt8="1 1 0 1 0 0 0 0 1 0 0 1 1 1 1 1 1 0 0 1 0 1 0 1 1 0 1 0 0 0 1 0 0 0 1 1 0 1 0 0 1 1 0 0 1 0 0 1 0 1 0 0 1 0 0 1 1 0 1 0 1 1 1 0 0 0 1 1 0 1 0 0 0 0 1 0 1 1 1 0 0 1 1 1 1 1"
opt9="1 0 0 0 1 1 0 0 1 1 1 1 1 0 0 0 0 1 0 1 0 0 0 0 0 0 1 0 0 1 1 1 0 1 0 0 0 0 0 0 0 1 1 0 0 0 0 1 1 1 0 1 0 0 0 1 1 1 0 0 0 1 0 1 1 0 1 1 0 0 0 1 0 0 0 1 0 0 1 1 1 1 1 0 1 0"
opt10="0 0 0 0 0 1 1 1 1 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 1 0 0 1 0 1 1 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 1 1 0 0 1 0 0 1 1 0 0 0 1 0 0 0 1 0 1 0 0 0 1 0 1 1 1 1 0 0 0 1 0 1 1"


tol_opt=[]
tol_opt.append(opt1)
tol_opt.append(opt2)
tol_opt.append(opt3)
tol_opt.append(opt4)
tol_opt.append(opt5)
tol_opt.append(opt6)
tol_opt.append(opt7)
tol_opt.append(opt8)
tol_opt.append(opt9)
tol_opt.append(opt10)


options = ['-fgcse-after-reload','-finline-functions','-fipa-cp-clone','-floop-interchange','-floop-unroll-and-jam','-fpeel-loops','-fpredictive-commoning','-fsplit-loops',
        '-fsplit-paths','-ftree-loop-distribute-patterns','-ftree-loop-distribution','-ftree-loop-vectorize','-ftree-partial-pre','-ftree-slp-vectorize',
        '-funswitch-loops','-fversion-loops-for-strides','-fno-peephole2', '-ffast-math', '-fno-schedule-insns2', '-fno-caller-saves', '-funroll-all-loops',
        '-fno-inline-small-functions', '-finline-functions', '-fno-math-errno', '-fno-tree-pre', '-ftracer', '-fno-reorder-functions', '-fno-dce', '-fipa-cp-clone',
        '-fno-move-loop-invariants', '-fno-regmove', '-funsafe-math-optimizations', '-fno-tree-loop-optimize', '-fno-merge-constants', '-fno-omit-frame-pointer', '-fno-align-labels',
        '-fno-tree-ter', '-fno-tree-dse', '-fwrapv', '-fgcse-after-reload', '-fno-align-jumps', '-fno-asynchronous-unwind-tables', '-fno-cse-follow-jumps', '-fno-ivopts', '-fno-guess-branch-probability',
        '-fprefetch-loop-arrays', '-fno-tree-coalesce-vars', '-fno-common', '-fpredictive-commoning', '-fno-unit-at-a-time', '-fno-cprop-registers','-fno-early-inlining', '-fno-delete-null-pointer-checks',
        '-fselective-scheduling2', '-fno-gcse', '-fno-inline-functions-called-once', '-funswitch-loops', '-fno-tree-vrp', '-fno-tree-dce', '-fno-jump-tables', '-ftree-vectorize', '-fno-argument-alias',
        '-fno-schedule-insns', '-fno-branch-count-reg', '-fno-tree-switch-conversion', '-fno-auto-inc-dec', '-fno-crossjumping', '-fno-tree-fre', '-fno-tree-reassoc', '-fno-align-functions', '-fno-defer-pop',
        '-fno-optimize-register-move', '-fno-strict-aliasing', '-fno-rerun-cse-after-loop', '-fno-tree-ccp', '-fno-ipa-cp', '-fno-if-conversion2', '-fno-tree-sra', '-fno-expensive-optimizations',
        '-fno-tree-copyrename', '-fno-ipa-reference', '-fno-ipa-pure-const', '-fno-thread-jumps', '-fno-if-conversion', '-fno-reorder-blocks', '-falign-loops']

sel_list=[]
sel_options=[]


for opt in tol_opt:
    print("len(options)=",len(options))
    ot=opt.split(" ")
    outputdata=[]
    outputdata.append(86)
    for i in ot:
        temp=int(i)
        outputdata.append(temp)
    print("outputdata=",outputdata)

    sel_list.append(outputdata)


    simple_options=[]
    for i in range(len(outputdata)-1):
        if outputdata[i+1]==1:
            simple_options.append(options[i])

    sel_options.append(simple_options)
    print(simple_options)
    print("len(simple)=",len(simple_options))



print("sel_list=",sel_list)
print("sel_options=",sel_options)