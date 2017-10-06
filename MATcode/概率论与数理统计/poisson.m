%λ=1,3,6,10
clear;
lambda = [1,3,6,10];
x = [1:15]';
y1 = [];
y2 = [];
for i = 1:length(lambda)
    y1 = [y1, poisspdf(x, lambda(i))];
    y2 = [y2, poisscdf(x, lambda(i))];
end
subplot(121);plot(x, y1);
title('概率密度曲线');
axis square;
subplot(122);plot(x, y2);
title('分布函数曲线');
axis square;
