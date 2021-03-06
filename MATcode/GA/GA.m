% 遗传算适用于求解正数和最大值
clc;
clear;
pcro = 0.8; % 交叉概率
pmut = 0.085; % 变异概率
maxiter = 200; % 迭代次数
up = 100; % 函数上界
low = -100; % 函数下界
dim = 2; 
prec = 0.0001; % 要求结果的精度
n = 50; % 种群个数
length = ceil(log2((up - low)/prec + 1)); % 求得单个变量编码长度，ceil是向正无穷取整
popul = encode(length, n, dim); % 用编码函数求得初始种群，n为种群个体个数2
iter = 1;
minf = inf;
best_pos = popul(1, :);
gf = zeros(1, maxiter); % 初始化函数值
while(iter <= maxiter)
    fval = zeros(1, n); % 初始化函数值
    fit = zeros(1, n); % c初始化适应度值
        for i = 1:n
            x = decode(popul(i, :), low, up, length, dim); % 利用解码函数解码个体
            fval(i) = fun(x, dim); % 求个体的函数值
            pop(i, :) = x;
            if fval(i) < minf % 最优点及得到最终种群中的最优值
                minf = fval(i);
                best_pos = popul(i, :); % 全局最优值对应的位置
                xmin = x;
            end
        end
        % 求个体的适应度值
        maxfval = max(fval);
        Fsum = sum(fval);
        fs = n * maxfval - Fsum;
        fit = (maxfval - fval) / fs;
        sum_val = 0;
        for j = 1: n - 1
            sum_val = sum_val + fval(j);
        end
        sum_val = sum_val + minf;
        fval_ave = sum_val/n; % 求适应度平均值
        fval_min = minf; % 适应度最小值
        popul = select(popul, n, fit, best_pos); % 选择比例
        popul = crossover(popul, pcro, n, length, dim); %交叉
        popul = mutation(popul, pmut, n, length, dim); % 变异
        popul(n, :) = best_pos;
        bestfval(iter) = minf;
        bestx = minf;
        gf(iter) = fval_min;
        iter = iter + 1; 
end
t = [1: maxiter];
plot(t, gf);
minf;
bestfval;
        
        
            
        
        
                
            
