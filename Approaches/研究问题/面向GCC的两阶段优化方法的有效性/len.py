A=['-fgcse-after-reload', '-finline-functions', '-fipa-cp-clone', '-fpeel-loops', '-fsplit-loops', '-fsplit-paths', '-ftree-loop-vectorize', '-ftree-partial-pre', '-funswitch-loops', '-fno-peephole2', '-ffast-math', '-fno-schedule-insns2', '-fno-caller-saves', '-funroll-all-loops', '-fno-inline-small-functions', '-finline-functions', '-fno-tree-pre', '-ftracer', '-fno-reorder-functions', '-fno-dce', '-fipa-cp-clone', '-fno-move-loop-invariants', '-funsafe-math-optimizations', '-fno-tree-loop-optimize', '-fno-merge-constants', '-fno-omit-frame-pointer', '-fno-tree-ter', '-fwrapv', '-fgcse-after-reload', '-fno-align-jumps', '-fno-asynchronous-unwind-tables', '-fno-cse-follow-jumps', '-fno-ivopts', '-fno-guess-branch-probability', '-fprefetch-loop-arrays', '-fno-tree-coalesce-vars', '-fno-common', '-fno-unit-at-a-time', '-fno-cprop-registers', '-fselective-scheduling2', '-fno-gcse', '-fno-inline-functions-called-once', '-funswitch-loops', '-fno-tree-vrp', '-fno-tree-dce', '-ftree-vectorize', '-fno-crossjumping', '-fno-tree-fre', '-fno-tree-reassoc', '-fno-align-functions', '-fno-defer-pop', '-fno-rerun-cse-after-loop', '-fno-tree-ccp', '-fno-ipa-cp', '-fno-if-conversion2', '-fno-expensive-optimizations', '-fno-if-conversion']
B='0 1 1 0 0 0 0 1 1 1 1 0 0 1 1 0 1 0 0 0 1 1 0 1 1 1 1 0 1 1 1 0 1 1 0 0 0 1 0 1 1 1 1 0 0 1 0 1 0 1 1 1 1 0 0 0 1 0 1 0 1 0 0 1 1 0 1 1 0 1 1 1 1 0 0 1 0 0 0 0 1 0 1 1 0 1'
C=[]
D=[]#把B转为’1，0’
E=[]
flag=0
z=0
C=B.split(' ')
for i in C:
    num=int(i)
    D.append(num)
for k in D:
    if (k==1):
        z+=1
        E.append(A[flag])#得到最优选项集
    else:
        pass
    flag+=1
if len(A)==len(D) and len((E))==z:
    print(E)
else:
    print("长度不对！")
