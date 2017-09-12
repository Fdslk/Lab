clc;
clear;
N = 50; % N为鱼群规模，即鱼的条数
visual = 0.9;% 表示可视范围
step = 0.02; % 步长，即拥挤度因子
dim = 2;
maxiter = 300;
lwbnd = -100;
upbnd = 100;
pop = rand(N, dim) * (upbnd - lwbnd) + lwbnd; % 初始化鱼群当前所处位置
xspop = pop; 
xfpop = pop;
xpop = pop;
for i = 1:N
    fval = fun(pop(i, :), dim); %计算粒子适应度值
end

[gfval, g] = min(fval);
gbest = pop(g,:); % 全局最优值及其位置
%gfval = inf;
%gbest = pop(1,:);
gf = zeros(1, maxiter); %记录每一次循环得到的最优结果
%开始迭代
for iter = 1: maxiter
    for i = 1: N
        nf = 0; % nf为当前鱼周围可视范围内的伙伴鱼条数（不含当前鱼）
        xcpop = rand(1, dim); % cx 当前与可视范围内伙伴鱼的中心位置
        for j = 1: N
            for k = 1:dim
                if abs(pop(i, k) - pop(j, k)) > 0 && abs(pop(i, k) - pop(j, k)) < visual;
                    xcpop(1, k) = xcpop(1, k) + pop(j, k);
                    nf = nf + 1;
                end
            end
        end
        if  nf > 0
            nf = nf/N;
            xcpop = xcpop/nf; % 找到伙伴鱼的中心位置
        end
        if fun(xcpop(1, :), dim) < fun(pop(i, :), dim)
            for k = 1:dim
                xspop(i, :) = pop(i, :) + rand*step*(xcpop(1,:) - pop(i, :));
            end
        else
            xspop(i, :) = Prey(pop(i, :), dim);
        end % 聚群行为结束
        if fun(xcpop(1, :),dim ) < gfval
            gfval = fun(xcpop(1, :), dim);
            gbest = xcpop(1, :);
        end
        for j = 1:N
            p2 = 0;
            for k = 1:dim
                if abs(pop(i,k) - pop(j,k)) > 0 && abs(pop(i,k) -pop(j, k)) < visual&&fun(pop(j,:),dim) < gfval;
                    p2 = p2 + 1;
                    gfval = fun(pop(j, :),dim);
                    gbest = pop(j, :);
                end
            end
        end
        if gbest == pop(i, :)
            xfpop(i,:) = pop(i, :) + rand*step*(gbest(1, :) - pop(i, :));
            for m = 1:dim
                if xfpop(i, m) > upbnd
                    xfpop(i, m) = upbnd;
                elseif xfpop(i, m) < lwbnd % 判断是否越界
                    xfpop(i, m) = lwbnd;
                end
            end
        else
            xfpop(i, :) = Prey(pop(i, :),dim);
        end % 追尾行为结束
            if fun(xspop(i, :),dim) < fun(xfpop(i, :),dim)
                xpop(i,:) = xspop(i,:);
            else
                xpop(i, :) = xfpop(i, :);
            end
            pop(i, :) = xpop(i, :); %跟新下一次迭代的初始值
    end %一次迭代结束
    %找出当前迭代中最好的，如果其比公告板上的记录还好，就用其代替公告板上的记录
    for i = 1: N
        if fun(xpop(i, :), dim) < gfval
            gfval = fun(xpop(i, :), dim);
            gbest = xpop(i, :);
        end
    end
    iter
    gf(iter) = gfval;
end
t = [1:maxiter];
plot(t, gf, 'b-');


    
            