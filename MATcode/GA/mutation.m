function populnew = mutation(popul, pmut, n, length, dim)
% �Ӻ���5 ���캯��
k = 1;
while k <= n
    rk = rand();
    if rk < rand()
        pos = fix(rand*(dim * length - 1)) + 1; % ������������
        % popul(k, pos) = popul(k, pos); % �Ա������б���
        % �������
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

