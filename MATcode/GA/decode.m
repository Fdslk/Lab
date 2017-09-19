function x = decode(a, low, up, length, d)
% 子函数二解码函数
% a 为解码个体，将个体分成两端后分别解码得到两个变量的值
str = zeros(1, d);
x = zeros(1, d);
for j = 1: d
    for i = 1: length
        if a(j*length + 1 - i)
            str(j) = str(j) + 2^(i - 1);
        end
    end
    x(j) = low + str(j)*((up - low)/(2^length - 1));
end

