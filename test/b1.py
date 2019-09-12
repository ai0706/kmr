#! /usr/local/bin/python3
# coding: utf-8
# 事前確率

w1=(1/3);
w2=1/3;
w3=1/3;
# 尤度
L1=3/4;
L2=1/2;
L3=1/3;
#print('{:.2}'.format(w1))
wL1=w1*L1;
wL2=w2*L2;
wL3=w3*L3;

wL =wL1+wL2+wL3;
w1_r = wL1/wL;
w2_r = wL2/wL;
w3_r = wL3/wL;

print('{:.2}'.format(w1_r))
print('{:.2}'.format(w2_r))
print('{:.2}'.format(w3_r))

w1=w1_r;
w2=w2_r;
w3=w3_r;

wL1=w1*L1;
wL2=w2*L2;
wL3=w3*L3;
wL =wL1+wL2+wL3;

w1_r = wL1/wL;
w2_r = wL2/wL;
w3_r = wL3/wL;

print('{:.2}'.format(w1_r))
print('{:.2}'.format(w2_r))
print('{:.2}'.format(w3_r))
