function populnew = select(popul, n, p, best_pos)
% pop为待选择原始种群，q为每个个体适应度值累计概率，即赌轮区间，n为种群个体数
m = 1;
q(1) = p(1);
for i = 2:n
    q(i) = q(i - 1) + p(i); % 累加个体适应度形成赌轮
end
for k = 1: n - 1
    r = rand();
    for l = 2:n
        if(q(l - 1) <= r) && (r <= q(l)) % 度盘轮选择
            m = 1;
            break;
        end
    end
    populnew(k, :) = popul(m, :);
end
populnew(n,:) = best_pos;
end

