clc;
clear
dim = 2;
N = 10; %ϸ����Ŀ
Nc = 20; % �����Բ�����ִ�д���
Ns = 4; % ϸ������ζ�����
Nre = 4; % ���Ʋ�����ִ�д���
Ned = 2; % Ǩ�������ִ�д���
Sr = N/2; % ϸ����ÿ�����Ƹ������Ŀ
Ped = 0.25; % ϸ����Ǩ�����
c(:, 1) = 0.5*ones(N,1); % �ζ�����

iter = 1; % ����������ʼ��
maxiter = 100; % ����������
gf = zeros(1, maxiter); % ����������
%ϸ��λ�ó�ʼ��
lwbnd = -100; % �����½�
upbnd = 100; % �����Ͻ�
pop = rand(N, dim)*(upbnd - lwbnd) + lwbnd; %����λ�ó�ʼ��
for i = 1:N
    fval(i) = fun(pop(i,:),dim); % ����������Ӧ��ֵ
end
[gfval, g] = min(fval); 
gbest = pop(g, :); %������Ӧ��ֵ��λ��
while iter <= maxiter
    for l = 1:Ned % Ǩ�����
        for k = 1: Nre % �����Բ���
            for j = 1: Nc % �����Բ���
                for i = 1:N 
                    if rand > 0.5
                        cpop(1, :) = pop(i, :) + c(i)*pop(i, :);
                    else
                        cpop(1,:) = pop(i, :) - c(i)*pop(i, :);
                    end
                    cfval = fun(cpop(1,:), dim);
                end
                for i = 1:N
                    m = 0; %�����ζ�����
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
                % �����Բ���
                [so_fval, loc] = sort(fval);
                for i = 1:(N/2)
                    pop(loc(i + N/2), :) = pop(loc(i), :);
                end
                % Ǩ�����
                for i = 1:N
                    if Ped > rand
                        pop(i, :) = rand(1, dim)*(upbnd - lwbnd) + lwbnd;
                    end
                end
            end
        end
    end
    for i = 1: N
        fval(i) = fun(pop(i, :),dim); % ������Ӧ��ֵ
    end
    [pfval, g] = min(fval);
    pbest = pop(g, :); % ������Ӧ��ֵ��λ��
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