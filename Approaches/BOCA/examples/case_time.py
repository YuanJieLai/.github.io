#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 10:11:00 2022

@author: usr
"""
import os, sys
import time
import random
import numpy as np
import copy
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from scipy.stats import norm
import math
#random.seed(456)
iters = 60
begin2end = 5
md = int(os.environ.get('MODEL', 1))
fnum = int(os.environ.get('FNUM', 8))
decay = float(os.environ.get('DECAY', 0.5))
scale = float(os.environ.get('SCALE', 10))
offset = float(os.environ.get('OFFSET', 20))

#案例2mm
# cmd2 = ' -I ../polybench/utilities -I ../polybench/linear-algebra/kernels/2mm ../polybench/utilities/polybench.c ../polybench/linear-algebra/kernels/2mm/2mm.c -lm -DPOLYBENCH_TIME -o 2mm_time'
# cmd3 = 'gcc -O2 -funswitch-loops -ftree-vectorize -fpredictive-commoning -fipa-cp-clone -finline-functions -fgcse-after-reload -I ../polybench/utilities -I ../polybench/linear-algebra/kernels/2mm ../polybench/utilities/polybench.c ../polybench/linear-algebra/kernels/2mm/2mm.c -lm -DPOLYBENCH_TIME -o 2mm_time'
# cmd4 = 'rm -rf *.o *.I *.s a.out'
# cmd5 = './2mm_time'


#案例 heat-3d
# cmd2 = ' -I ../polybench/utilities -I ../polybench/stencils/heat-3d ../polybench/utilities/polybench.c ../polybench/stencils/heat-3d/heat-3d.c -lm -DPOLYBENCH_TIME -o heat-3d'
# cmd3 = 'gcc -O2 -funswitch-loops -ftree-vectorize -fpredictive-commoning -fipa-cp-clone -finline-functions -fgcse-after-reload -I ../polybench/utilities -I ../polybench/utilities -I ../polybench/stencils/heat-3d ../polybench/utilities/polybench.c ../polybench/stencils/heat-3d/heat-3d.c -lm -DPOLYBENCH_TIME -o heat-3d'
# cmd4 = 'rm -rf *.o *.I *.s a.out'
# cmd5 = './heat-3d'

#案例3mm
# cmd2 = ' -I ../polybench/utilities -I ../polybench/linear-algebra/kernels/3mm ../polybench/utilities/polybench.c ../polybench/linear-algebra/kernels/3mm/3mm.c -lm -DPOLYBENCH_TIME -o 3mm_time'
# cmd3 = 'gcc -O2 -funswitch-loops -ftree-vectorize -fpredictive-commoning -fipa-cp-clone -finline-functions -fgcse-after-reload -I ../polybench/utilities -I ../polybench/linear-algebra/kernels/3mm ../polybench/utilities/polybench.c ../polybench/linear-algebra/kernels/3mm/3mm.c -lm -DPOLYBENCH_TIME -o 3mm_time'
# cmd4 = 'rm -rf *.o *.I *.s a.out'
# cmd5 = './3mm_time'

#案例symm
# cmd2 = ' -I ../polybench/utilities -I ../polybench/linear-algebra/blas/symm ../polybench/utilities/polybench.c ../polybench/linear-algebra/blas/symm/symm.c -lm -DPOLYBENCH_TIME -o symm'
# cmd3 = 'gcc -O2 -funswitch-loops -ftree-vectorize -fpredictive-commoning -fipa-cp-clone -finline-functions -fgcse-after-reload -I ../polybench/utilities -I ../polybench/linear-algebra/blas/symm/ ../polybench/utilities/polybench.c ../polybench/linear-algebra/blas/symm/symm.c -lm -DPOLYBENCH_TIME -o symm'
# cmd4 = 'rm -rf *.o *.I *.s a.out'
# cmd5 = './symm'

#案例cholesky
cmd2 = ' -I ../polybench/utilities -I ../polybench/linear-algebra/solvers/cholesky ../polybench/utilities/polybench.c ../polybench/linear-algebra/solvers/cholesky/cholesky.c -lm -DPOLYBENCH_TIME -o a.out'
cmd3 = 'gcc -O2 -funswitch-loops -ftree-vectorize -fpredictive-commoning -fipa-cp-clone -finline-functions -fgcse-after-reload -I ../polybench/utilities -I ../polybench/linear-algebra/solvers/cholesky ../polybench/utilities/polybench.c ../polybench/linear-algebra/solvers/cholesky/cholesky.c -lm -DPOLYBENCH_TIME -o a.out'
cmd4 = 'rm -rf *.o *.I *.s a.out'
cmd5 = './a.out'

#大的搜索空间
#options = ['-fno-peephole2', '-ffast-math', '-fno-schedule-insns2', '-fno-caller-saves', '-funroll-all-loops', '-fno-inline-small-functions', '-finline-functions', '-fno-math-errno', '-fno-tree-pre', '-ftracer', '-fno-reorder-functions', '-fno-dce', '-fipa-cp-clone', '-fno-move-loop-invariants', '-fno-regmove', '-funsafe-math-optimizations', '-fno-tree-loop-optimize', '-fno-merge-constants', '-fno-omit-frame-pointer', '-fno-align-labels', '-fno-tree-ter', '-fno-tree-dse', '-fwrapv', '-fgcse-after-reload', '-fno-align-jumps', '-fno-asynchronous-unwind-tables', '-fno-cse-follow-jumps', '-fno-ivopts', '-fno-guess-branch-probability', '-fprefetch-loop-arrays', '-fno-tree-coalesce-vars', '-fno-common', '-fpredictive-commoning', '-fno-unit-at-a-time', '-fno-cprop-registers', ' ', '-fno-early-inlining', '-fno-delete-null-pointer-checks', '-fselective-scheduling2', '-fno-gcse', '-fno-inline-functions-called-once', '-funswitch-loops', '-fno-tree-vrp', '-fno-tree-dce', '-fno-jump-tables', '-ftree-vectorize', '-fno-argument-alias', '-fno-schedule-insns', '-fno-branch-count-reg', '-fno-tree-switch-conversion', '-fno-auto-inc-dec', '-fno-crossjumping', '-fno-tree-fre', '-fno-tree-reassoc', '-fno-align-functions', '-fno-defer-pop', '-fno-optimize-register-move', '-fno-strict-aliasing', '-fno-rerun-cse-after-loop', '-fno-tree-ccp', '-fno-ipa-cp', '-fno-if-conversion2', '-fno-tree-sra', '-fno-expensive-optimizations', '-fno-tree-copyrename', '-fno-ipa-reference', '-fno-ipa-pure-const', '-fno-thread-jumps', '-fno-if-conversion', '-fno-reorder-blocks', '-falign-loops']

#约简的搜索空间
options=['-fno-peephole2', '-ffast-math', '-fno-schedule-insns2', '-fno-caller-saves', '-funroll-all-loops', '-fno-inline-small-functions', '-finline-functions', '-fno-tree-pre', '-ftracer', '-fno-reorder-functions', '-fno-dce', '-fno-move-loop-invariants', '-funsafe-math-optimizations', '-fno-tree-loop-optimize', '-fno-merge-constants', '-fno-omit-frame-pointer', '-fno-tree-ter', '-fwrapv', '-fgcse-after-reload', '-fno-align-jumps', '-fno-asynchronous-unwind-tables', '-fno-cse-follow-jumps', '-fno-ivopts', '-fno-guess-branch-probability', '-fprefetch-loop-arrays', '-fno-tree-coalesce-vars', '-fno-common', '-fpredictive-commoning', '-fno-unit-at-a-time', '-fno-cprop-registers', '-fselective-scheduling2', '-fno-gcse', '-fno-inline-functions-called-once', '-funswitch-loops', '-fno-tree-vrp', '-fno-tree-dce', '-ftree-vectorize', '-fno-crossjumping', '-fno-tree-fre', '-fno-tree-reassoc', '-fno-align-functions', '-fno-rerun-cse-after-loop', '-fno-tree-ccp', '-fno-ipa-cp', '-fno-if-conversion2', '-fno-expensive-optimizations', '-fno-ipa-pure-const', '-fno-if-conversion']



nu=0.0
speedups = []
step = 0
while(len(speedups) < 6):
    os.system(cmd4)
    os.system(cmd3)
    print(cmd3)
    
    begin = time.time()
    os.system(cmd5)
    end = time.time()
    nu = end - begin
    
    speedups.append(nu)
nu=0.0
for i in range(len(speedups)):
    nu=nu+speedups[i]
nu=nu/6


def generate_opts(independent):
    result = []
    for k, s in enumerate(independent):
        if s == 1:
            result.append(options[k])
    independent = result

    return independent

def get_objective_score(independent):
    independent = generate_opts(independent)
    
    speedups = []
    step = 0
    while (len(speedups) < 6):
        step += 1
        if step > 10:
            print('failed configuration!')
            sys.exit(0)
        os.system(cmd4)
        print('gcc -O2 ' + ' '.join(independent) + cmd2)
        os.system('gcc -O2 ' + ' '.join(independent) + cmd2)
        
        begin = time.time()
        print(cmd5)
        ret = os.system(cmd5)
        if ret != 0:
            continue
        print(ret)
        end = time.time()
        de = end - begin
        #*******************
        #de表示编译序列优化后所需的时间
        #********************
        # os.system(cmd4)
        # os.system(cmd3)

        # begin = time.time()
        # os.system(cmd5)
        # end = time.time()
        # nu = end - begin
        #***********************
        #nu 表示O2所需要的运行时间
        #***********************
        print('nu:' + str(nu) + ' de:' + str(de) + ' val:' + str(nu / de))
        speedups.append(nu / de)
        #speedup指的是o2/seq，这个值越大表示seq优化效果越好 
    print(speedups)
    #返回的取平均值，且加了负号，这表示值都为负数，其值越小表示seq优化效果越好
    return -np.median(speedups)
    
def generate_conf(x):
    comb = bin(x).replace('0b', '')
    comb = '0' * (len(options) - len(comb)) + comb
    conf = []
    for k, s in enumerate(comb):
        if s == '1':
            conf.append(1)
        else:
            conf.append(0)
    return conf





#获得BOCA 规定迭代次数的解信息
if __name__ == '__main__':
    a=time.time()
    training_indep = []
    
    while len(training_indep) < 1:
        x = random.randint(0, 2 ** len(options))
        x = generate_conf(x)
        training_indep.append(x)
    training_dep = [get_objective_score(r) for r in training_indep]
    
    b=time.time()
    
    print("time=",b-a)
    
    
    
    