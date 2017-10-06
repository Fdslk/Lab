clear;
n  = 1000;
t1 = 0;
t0 = 0;
result = [];
for i = 1:n
    % unifrnd 函数创建均匀分布
    result(i) = unifrnd(0, 1);
    if result(i) > 0.5
        t1 = t1 + 1;
    else
        t0 = t0 + 1;
    end
end
p1 = t1/n
p0 = t0/n
