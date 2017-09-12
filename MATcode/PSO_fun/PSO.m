clc;
clear;
maxiter = 300;
lwbnd = -100;
upbnd = 100;
GM = 0;
PopSize = 50;
iter = 1;
c1 = 2;
c2 = 2;
w = 1;
vmax = 0.5;
dim = 2;
pop = rand(PopSize, dim)*(upbnd - lwbnd) + lwbnd;
vel = rand(PopSize, dim);

for i = 1:PopSize
    fval(i) = fun(pop(i,:), dim);
end
bestpos = pop;
fbestpos = fval;
[fbestval, g] = min(fval);
gbestval = fbestval;
gbest = pop(g, :);
gf = zeros(1, maxiter);
for i = 1:PopSize;
    vel(i,:) = w * vel(i, :) + c1*rand*(bestpos(i, :)-pop(i,:)) + c2*rand*(gbest - pop(i,:));
    for j = 1:dim
        if vel(i, j) > vmax
            vel(i, j) = vmax;
        elseif vel(i, j) < -vmax
            vel(i, j) = -vmax
        end
    end
    pop(i, :) = pop(i,:) + vel(i,:);
end
sum = 0.0;
while (iter < maxiter)
    for i = 1:PopSize
        fval(i) = fun(pop(i,:), dim);
        if fval(i) < fbestpos(i)
            fbestpos(i) = fval(i);
            bestpos(i,:) = pop(i,:);
        end
    end
    [fbestval, g] = min(fval);
    if fbestval < fbestval
        gbestval = fbestval;
        gbest = pop(g,:);
    end
    for i = 1:PopSize
        vel(i,:) = w*vel(i,:) + c1*rand*(bestpos(i,:) - pop(i,:)) + c2*rand*(gbest - pop(i,:));
        for j = 1:dim
            if vel(i,j) > vmax
                vel(i, j) = vmax;
            elseif vel(i,j) < -vmax
                vel(i, j) = -vmax;
            end
        end
        pop(i,:) = pop(i,:) + vel(i,:);
    end
    for i = 1:PopSize
        for j = 1:dim
            if pop(i,j) < lwbnd
                pop(i,j) = lwbnd;
            elseif pop(i,j) > upbnd
                pop(i,j) = upbnd;
            end
        end
    end
    fmin = gbestval;
    sum = sum + fmin;
    bestval(iter) = gbestval;
    bestx = pop(g,:);
    gf(iter) = gbestval;
    iter = iter + 1;
end
sum = sum/maxiter;
t = [1:maxiter];
plot(t, gf);