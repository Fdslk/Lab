function populnew = select(popul, n, p, best_pos)
% popΪ��ѡ��ԭʼ��Ⱥ��qΪÿ��������Ӧ��ֵ�ۼƸ��ʣ����������䣬nΪ��Ⱥ������
m = 1;
q(1) = p(1);
for i = 2:n
    q(i) = q(i - 1) + p(i); % �ۼӸ�����Ӧ���γɶ���
end
for k = 1: n - 1
    r = rand();
    for l = 2:n
        if(q(l - 1) <= r) && (r <= q(l)) % ������ѡ��
            m = 1;
            break;
        end
    end
    populnew(k, :) = popul(m, :);
end
populnew(n,:) = best_pos;
end

