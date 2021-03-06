function x = Prey(x, dim)
%子函数一 觅食函数 模拟人工鱼的觅食行为
%Trynumber表表人工鱼在视野范围内多次尝试来寻找食物浓度更大的位置，
%它就表示人工鱼在移动钱的最大试探次数
Trynumber = 3; % 可输入（改变）
visual = 1; % 可输入（改变）
step = 0.01;
p = zeros(1, dim);

for i = 1: Trynumber
    for j = 1: dim
        xt(1, j) = x(1, j) + rand*step*visual;
        % xt 表示实时的视野变化
    end
    if fun(xt(1,:), dim) > fun(x(1, :), dim)
        for j = 1: dim
            xnext(1, j) = x(1, j) + rand*step*(xt(1,j) - x(1,j));
            % xnext 表示下一步可能移动的位置
            if xnext(1, j) > 10
                xnext(1, j) = 10;
            elseif xnext(1, j) < 0
                xnext(1, j) = 0;
            end
            p(j) = 1;
            break;
        end
    end
end
% 随机行为
for k = 1:dim
    if p(j) == 0
        xnext(1, j) = x(1, j) + rand*step*visual;
        if xnext(1, j) > 10
            xnext(1, j) = 10;
        elseif xnext(1, j) < 0
            xnext(1, j) = 0;
        end
    end
end

