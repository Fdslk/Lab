function x = Prey(x, dim)
%第二个子涵数
Trynumber = 3; % 可输入（改变）
visual = 1; % 可输入（改变）
step = 0.01;
p = zeros(1, dim);

for i = 1: Trynumber
    for j = 1: dim
        xt(1, j) = x(1, j) + rand*step*visual;
    end
    if fun(xt(1,:), dim) > fun(x(1, :), dim)
        for j = 1: dim
            xnext(1, j) = x(1, j) + rand*step*(xt(1,j) - x(1,j));
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

