clear;
mu0 = log(1000);
sigma0 = 1;
len = 5;
% normrnd����������̫�ֲ��������
y1 = normrnd(mu0, sigma0, [1 len]);
P = 3;
Q = 4;
y2 = normrnd(mu0, sigma0, P, Q);
M = 1000;
y3 = normrnd(mu0, sigma0, [1, M]);
figure;
t = 0:0.1:max(y3);
hist(y3, t);
% axis �涨x����y��ķ�Χ
axis([0, max(y3), 0, 50]);