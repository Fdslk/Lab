function populnew = mutation(popul, pmut, n, length, dim)
% 子函数5 变异函数
k = 1;
while k <= n
    rk = rand();
    if rk < rand()
        pos = fix(rand*(dim * length - 1)) + 1; % 随机产生变异点
        % popul(k, pos) = popul(k, pos); % 对变异点进行变异
        % 变异操作
        if popul(k, pos) == 0
            popul(k, pos) = 1;
        else
            popul(k, pos) = 0;
        end
    end
    k = k + 1;
end
populnew = popul;
end

