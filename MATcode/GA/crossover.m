function populnew = crossover(popul, pcro, n, length, dim)
% �Ӻ����� ���溯��
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
            pos = fix(rand()*dim*length) + 1; % ������������
            for i = pos:dim*length
                c = popul(b(1), i);
                popul(b(1), i) = popul(b(2), i); % �Խ����֮��ı�����н���
                popul(b(2), i) = c;
            end
            i = 0;
        end
    end
    populnew = popul;
end

