clear;
p1 = binopdf(45, 100, 0.5)
p2 = binocdf(45, 100, 0.5)
x = 1:100;
% 二项分布中事件A恰好发生k次的概率
p = binopdf(x, 100, 0.5);
px = binopdf(x, 100, 0.5);
subplot(121);
plot(x, p, 'rp');
xlabel('x'); ylabel('p'); title('分布函数');
axis square;
subplot(122); plot(x, px, '+');
xlabel('x'); ylabel('y');title('概率密度函数');
axis square;