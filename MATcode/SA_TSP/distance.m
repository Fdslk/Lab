function d = distance(inputcities)
%DISTANCE 此处显示有关此函数的摘要
%   距离计算函数
%   输入变量：
%    inputcities：原来的地点顺序和位置
%   输出变量： d:顺序相加的距离和
d = 0;
for n = 1:length(inputcities)
    if n == length(inputcities) % 首尾的距离计算
        % 范数某种意义上就是长度、大小、距离的意思，在这里看看，norm里面是不是x和y的坐标差
        % 其实就是用了勾股定理
        d = d + norm(inputcities(:,n) - inputcities(:, 1));
    else
        d = d + norm(inputcities(:,n) - inputcities(:,n + 1));%相邻两个点的距离
    end
end
end

