clc;
clear
dim = 2;
N = 10; %细菌数目
Nc = 20; % 趋向性操作的执行次数
Ns = 4; % 细菌最大游动次数
Nre = 4; % 复制操作的执行次数
Ned = 2; % 迁徙操作的执行次数
Sr = N/2; % 细菌在每带复制个体的数目
Ped = 0.25; % 细菌在迁徙概率
c(:, 1) = 0.5*ones(N,1); % 游动长度

iter = 1; % 迭代次数初始化
maxiter = 100; % 最大迭代次数
gf = zeros(1, maxiter); % 最大迭代次数
%细菌位置初始化
lwbnd = -100; % 函数下界
upbnd = 100; % 函数上界
pop = rand(N, dim)*(upbnd - lwbnd) + lwbnd; %粒子位置初始化
for i = 1:N
    fval(i) = fun(pop(i,:),dim); % 计算粒子适应度值
end
[gfval, g] = min(fval); 
gbest = pop(g, :); %最优适应度值和位置
while iter <= maxiter
    for l = 1:Ned % 迁徙操作
        for k = 1: Nre % 复制性操作
            for j = 1: Nc % 趋向性操作
                for i = 1:N 
                    if rand > 0.5
                        cpop(1, :) = pop(i, :) + c(i)*pop(i, :);
                    else
                        cpop(1,:) = pop(i, :) - c(i)*pop(i, :);
                    end
                    cfval = fun(cpop(1,:), dim);
                end
                for i = 1:N
                    m = 0; %激活游动长度
                    while m < Ns
                        if cfval < gfval
                            pop(i, :) = cpop;
                            fval(i) = cfval;
                            gfval = cfval;
                            gbest = cpop;
                        end
                        m = m + 1;
                    end
                end
                % 复制性操作
                [so_fval, loc] = sort(fval);
                for i = 1:(N/2)
                    pop(loc(i + N/2), :) = pop(loc(i), :);
                end
                % 迁徙操作
                for i = 1:N
                    if Ped > rand
                        pop(i, :) = rand(1, dim)*(upbnd - lwbnd) + lwbnd;
                    end
                end
            end
        end
    end
    for i = 1: N
        fval(i) = fun(pop(i, :),dim); % 计算适应度值
    end
    [pfval, g] = min(fval);
    pbest = pop(g, :); % 最优适应度值和位置
    if pfval < gfval
        gfval = pfval;
        gbest = pbest;
    end
    gf(iter) = gfval;
    iter = iter + 1;
    iter
end
t = [1: maxiter];
plot(t, gf);
