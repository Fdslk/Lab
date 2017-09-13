function y = fun(x, dim)
% Rosenbrock的测试函数（-5.12，5.12）测试函数有两个未知数
y = 0;
for i = 1: (dim - 1)
y = y + 100*(x(i+1).^2 - x(i)).^2 + (1 - x(i)).^2;
end
end

