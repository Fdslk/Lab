% �Ŵ���������������������ֵ
clc;
clear;
pcro = 0.8; % �������
pmut = 0.085; % �������
maxiter = 200; % ��������
up = 100; % �����Ͻ�
low = -100; % �����½�
dim = 2; 
prec = 0.0001; % Ҫ�����ľ���
n = 50; % ��Ⱥ����
length = ceil(log2((up - low)/prec + 1)); % ��õ����������볤�ȣ�ceil����������ȡ��
popul = encode(length, n, dim); % �ñ��뺯����ó�ʼ��Ⱥ��nΪ��Ⱥ�������2
iter = 1;
minf = inf;
best_pos = popul(1, :);
gf = zeros(1, maxiter); % ��ʼ������ֵ
while(iter <= maxiter)
    fval = zeros(1, n); % ��ʼ������ֵ
    fit = zeros(1, n); % c��ʼ����Ӧ��ֵ
        for i = 1:n
            x = decode(popul(i, :), low, up, length, dim); % ���ý��뺯���������
            fval(i) = fun(x, dim); % �����ĺ���ֵ
            pop(i, :) = x;
            if fval(i) < minf % ���ŵ㼰�õ�������Ⱥ�е�����ֵ
                minf = fval(i);
                best_pos = popul(i, :); % ȫ������ֵ��Ӧ��λ��
                xmin = x;
            end
        end
        % ��������Ӧ��ֵ
        maxfval = max(fval);
        Fsum = sum(fval);
        fs = n * maxfval - Fsum;
        fit = (maxfval - fval) / fs;
        sum_val = 0;
        for j = 1: n - 1
            sum_val = sum_val + fval(j);
        end
        sum_val = sum_val + minf;
        fval_ave = sum_val/n; % ����Ӧ��ƽ��ֵ
        fval_min = minf; % ��Ӧ����Сֵ
        popul = select(popul, n, fit, best_pos); % ѡ�����
        popul = crossover(popul, pcro, n, length, dim); %����
        popul = mutation(popul, pmut, n, length, dim); % ����
        popul(n, :) = best_pos;
        bestfval(iter) = minf;
        bestx = minf;
        gf(iter) = fval_min;
        iter = iter + 1; 
end
t = [1: maxiter];
plot(t, gf);
minf;
bestfval;
        
        
            
        
        
                
            