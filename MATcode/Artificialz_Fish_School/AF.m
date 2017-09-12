clc;
clear;
N = 50; % NΪ��Ⱥ��ģ�����������
visual = 0.9;% ��ʾ���ӷ�Χ
step = 0.02; % ��������ӵ��������
dim = 2;
maxiter = 300;
lwbnd = -100;
upbnd = 100;
pop = rand(N, dim) * (upbnd - lwbnd) + lwbnd; % ��ʼ����Ⱥ��ǰ����λ��
xspop = pop; 
xfpop = pop;
xpop = pop;
for i = 1:N
    fval = fun(pop(i, :), dim); %����������Ӧ��ֵ
end

[gfval, g] = min(fval);
gbest = pop(g,:); % ȫ������ֵ����λ��
%gfval = inf;
%gbest = pop(1,:);
gf = zeros(1, maxiter); %��¼ÿһ��ѭ���õ������Ž��
%��ʼ����
for iter = 1: maxiter
    for i = 1: N
        nf = 0; % nfΪ��ǰ����Χ���ӷ�Χ�ڵĻ����������������ǰ�㣩
        xcpop = rand(1, dim); % cx ��ǰ����ӷ�Χ�ڻ���������λ��
        for j = 1: N
            for k = 1:dim
                if abs(pop(i, k) - pop(j, k)) > 0 && abs(pop(i, k) - pop(j, k)) < visual;
                    xcpop(1, k) = xcpop(1, k) + pop(j, k);
                    nf = nf + 1;
                end
            end
        end
        if  nf > 0
            nf = nf/N;
            xcpop = xcpop/nf; % �ҵ�����������λ��
        end
        if fun(xcpop(1, :), dim) < fun(pop(i, :), dim)
            for k = 1:dim
                xspop(i, :) = pop(i, :) + rand*step*(xcpop(1,:) - pop(i, :));
            end
        else
            xspop(i, :) = Prey(pop(i, :), dim);
        end % ��Ⱥ��Ϊ����
        if fun(xcpop(1, :),dim ) < gfval
            gfval = fun(xcpop(1, :), dim);
            gbest = xcpop(1, :);
        end
        for j = 1:N
            p2 = 0;
            for k = 1:dim
                if abs(pop(i,k) - pop(j,k)) > 0 && abs(pop(i,k) -pop(j, k)) < visual&&fun(pop(j,:),dim) < gfval;
                    p2 = p2 + 1;
                    gfval = fun(pop(j, :),dim);
                    gbest = pop(j, :);
                end
            end
        end
        if gbest == pop(i, :)
            xfpop(i,:) = pop(i, :) + rand*step*(gbest(1, :) - pop(i, :));
            for m = 1:dim
                if xfpop(i, m) > upbnd
                    xfpop(i, m) = upbnd;
                elseif xfpop(i, m) < lwbnd % �ж��Ƿ�Խ��
                    xfpop(i, m) = lwbnd;
                end
            end
        else
            xfpop(i, :) = Prey(pop(i, :),dim);
        end % ׷β��Ϊ����
            if fun(xspop(i, :),dim) < fun(xfpop(i, :),dim)
                xpop(i,:) = xspop(i,:);
            else
                xpop(i, :) = xfpop(i, :);
            end
            pop(i, :) = xpop(i, :); %������һ�ε����ĳ�ʼֵ
    end %һ�ε�������
    %�ҳ���ǰ��������õģ������ȹ�����ϵļ�¼���ã���������湫����ϵļ�¼
    for i = 1: N
        if fun(xpop(i, :), dim) < gfval
            gfval = fun(xpop(i, :), dim);
            gbest = xpop(i, :);
        end
    end
    iter
    gf(iter) = gfval;
end
t = [1:maxiter];
plot(t, gf, 'b-');


    
            