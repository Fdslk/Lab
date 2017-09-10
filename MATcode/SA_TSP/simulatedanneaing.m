function simulatedanneaing( inputcities, initial_temperature,...
    cooling_rate,threshold,numberofcitiestoswap)

%-------------函数说明----------------
%    模拟退火函数
%       输入变量：
%               inputcities:原来的地点顺序和位置
%       initial_temperature：初始温度
%              cooling_rate： 降温比例系数
%               threshold  ： 一个循环次数
%     numberofcitiestoswap ： 每次交换地点的对数  
%---------------------------------------
temperature = initial_temperature; %初始温度
input_cities = inputcities; %城市坐标
plot(input_cities(1,:), input_cities(2,:),'*'); % 画出初始图像，与后面对比
hold on, plot(input_cities(1,:), input_cities(2, :));
figure;
while temperature > 0.01 % 循环条件，把降温底线作为条件
    for i = 1:threshold % 循环次数
        previous_distance = distance(input_cities); %旧距离和
        temp_cities = swapcities(input_cities, numberofcitiestoswap);%随机n次交换
        current_distance = distance(temp_cities); %新距离和
        diff = abs(current_distance - previous_distance); %长生误差
        if current_distance < previous_distance %距离变少了，直接接受，不用考虑
            input_cities  = temp_cities; %接受
        elseif rand(1) < exp(-diff/(temperature)) % 温度降低后，符合到了基态温度，然后变化就会逐渐降低，最后哪些坏的距离被交换的概率就会降低
            input_cities = temp_cities; % 概率符合了，进来接受
        end
    end
    temperature = temperature * cooling_rate; % 降温过程
end
    % 显示结果
fprintf('\t\t\tTemperature = %3.8f\n', temperature);
current_distance = distance(input_cities);
fprintf('\t\t\tFinal_distance = %3.8f\n', current_distance);
plot(input_cities(1,:), input_cities(2, :), '*');
hold on, plot(input_cities(1, :),  input_cities(2, :));
end


