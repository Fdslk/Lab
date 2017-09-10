function s = swapcities( inputcities, n )
%SWAPCITIES 此处显示有关此函数的摘要
%   交换地点顺序
%   输入变量：
%   inputcities：原来的地点顺序和位置
%   n:要交换的次数（即多少对地点交换）
%   输出变量：s:交换后的地点顺序和位置

s = inputcities;
for i = 1: n
    city_1 = round(length(inputcities)*rand(1));%生成随机交换点（1~30之间）round四舍五入
    if city_1 < 1
        city_1 = 1;
    end
    city_2 = round(length(inputcities)*rand(1));% 30个城市中随机挑选出一个城市进行交换
    if city_2 < 1
        city_2 = 1;
    end
    temp = s(:,city_1); %交换操作 
    s(:,city_1) = s(:,city_2);
    s(:,city_2) = temp;
end

