clear;
num = 4;
len = 5;
% exprand指数分布随机数产生函数
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
xlabel('取值');
ylabel('计数值');