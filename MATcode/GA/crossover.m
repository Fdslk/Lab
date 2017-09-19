function populnew = crossover(popul, pcro, n, length, dim)
% 子函数四 交叉函数
    k = 1;
    i = 0;
    while(k <= n)
        rk = rand();
        if rk < pcro
            b(i + 1) = k;
            i = i + 1;
        end
        k = k + 1;
        if i == 2
            pos = fix(rand()*dim*length) + 1; % 随机产生交叉点
            for i = pos:dim*length
                c = popul(b(1), i);
                popul(b(1), i) = popul(b(2), i); % 对交叉点之后的编码进行交换
                popul(b(2), i) = c;
            end
            i = 0;
        end
    end
    populnew = popul;
end

