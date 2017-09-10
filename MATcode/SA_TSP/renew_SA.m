%-------------函数说明----------------
%    模拟退火函数
%       输入变量：
%               inputcities:原来的地点顺序和位置
%       initial_temperature：初始温度
%              cooling_rate： 降温比例系数
%               threshold  ： 一个循环次数
%     numberofcitiestoswap ： 每次交换地点的对数  
%---------------------------------------
function  renew_SA(inputcities,initial_temperature,...
    cooling_rate,threshold,numberofcitiestoswap)             %退火算法
global iterations;                    %全局变量--迭代次数--作为循环条件
iterations = 1;
number_interations = 0;             %定义一个迭代次数用于降温操作
best_cities = inputcities ;         %用于记录已经找到的最好解
best_distance = distance(best_cities);    
num2swap_change = 0;    %定义一个变量--交换城市数目
tempeature = initial_temperature;       %初始温度
input_cities = inputcities;             %城市坐标
%while tempeature > 0.01         %循环条件，把降温底线作为条件         
 while iterations < threshold    %新的循环条件--迭代次数

       num2swap_change = num2swap_change + 1;      
       previous_distance = distance(input_cities); %旧距离和
       temp_cities = swapcities(input_cities,numberofcitiestoswap);  %随机n次交换
       current_distance = distance(temp_cities);   %新距离和
       diff = abs(current_distance - previous_distance);  %产生误差
       %-------------------------解变好的情况---------------------------
       if current_distance < previous_distance     %距离变少了，直接接受，不用考虑 
           num2swap_change = 0;                %进入循环后该变量清0
           input_cities = temp_cities;             %接受
          %---------记录最好的解--------------
           if best_distance > current_distance
               best_cities = input_cities;
               best_distance = distance(best_cities);
           end
          %---------------------------------- 
           if number_interations >= 5
              tempeature = tempeature*cooling_rate;      %降温过程
              number_interations = 0;
           end
           numberofcitiestoswap = round(numberofcitiestoswap*exp(-diff/(iterations*tempeature)));
           if numberofcitiestoswap == 0
               numberofcitiestoswap = 1;
           end
           iterations = iterations +1 ;
           number_interations = number_interations + 1;
       %---------------------解不好的情况---------------------------
       else
           if rand(1) < exp(-diff/(tempeature))   %否则，以一定的概率接受
               num2swap_change = 0;
               input_cities = temp_cities;        %概率符合了，进来接受   
               numberofcitiestoswap = round(numberofcitiestoswap*exp(-diff/(iterations*tempeature)));
              if numberofcitiestoswap == 0
                  numberofcitiestoswap = 1;
              end
              iterations = iterations +1 ;
              number_interations = number_interations + 1;
           end
       end
       %--如果一直循环着没有进入if中，就得改变条件让其进入if中-----
       if num2swap_change > 100 
           input_cities = best_cities;   %--把最好解转到input_cities中
           tempeature = tempeature/0.951; %升温--使其进入循环概率变大
           if numberofcitiestoswap > 1    %交换城市数降到1对时停止
              numberofcitiestoswap = numberofcitiestoswap - 1;
              if numberofcitiestoswap == 0
                 numberofcitiestoswap = 1;
              end
            num2swap_change = 0;
           end
       end
end
   fprintf('\t\t\tTempeature = %3.8f\n',tempeature);     %输出结果      
   current_distance = distance(input_cities);
   fprintf('\t\t\tFinal_istance = % 3.8f best_dis =  % 3.8f\n',current_distance,best_distance); 
   plot(best_cities(1,:),best_cities(2,:),'*');
   hold on,plot(best_cities(1,:),best_cities(2,:));