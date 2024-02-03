A=['-fgcse-after-reload', '-fsplit-paths', '-ftree-partial-pre', '-funswitch-loops', '-fno-peephole2', '-fno-schedule-insns2', '-fno-caller-saves', '-funroll-all-loops', '-fno-tree-pre', '-ftracer', '-fno-reorder-functions', '-fno-dce', '-fno-move-loop-invariants', '-fno-tree-loop-optimize', '-fno-merge-constants', '-fno-omit-frame-pointer', '-fno-tree-ter', '-fgcse-after-reload', '-fno-align-jumps', '-fno-asynchronous-unwind-tables', '-fno-cse-follow-jumps', '-fno-ivopts', '-fno-guess-branch-probability', '-fno-tree-coalesce-vars', '-fno-common', '-fno-unit-at-a-time', '-fno-cprop-registers', '-fselective-scheduling2', '-fno-gcse', '-funswitch-loops', '-fno-tree-vrp', '-fno-tree-dce', '-fno-crossjumping', '-fno-tree-fre', '-fno-align-functions', '-fno-rerun-cse-after-loop', '-fno-tree-ccp', '-fno-if-conversion2', '-fno-tree-sra', '-fno-expensive-optimizations', '-fno-if-conversion']
B='0 0 1 1 1 1 0 0 1 1 1 0 0 0 0 0 1 0 0 0 0 1 0 1 0 0 1 1 1 1 0 0 1 1 0 0 0 1 0 1 0'
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
if len(A)==len(D) and len(E)==z:
    print(E)
else:
    print("长度不对！")
print(len(E))