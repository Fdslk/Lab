clear;
num = 4;
len = 5;
% exprandָ���ֲ��������������
y1 = exprnd(num, [1 len]);
P = 3;
Q = 4;
y2 = exprnd(num, P, Q);
M = 1000;
y3 = exprnd(num, [1, M]);
figure(3);
t = 0:0.2:max(y3);
hist(y3, t);
axis([0, max(y3) 0 100]);
xlabel('ȡֵ');
ylabel('����ֵ');