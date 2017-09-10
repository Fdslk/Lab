%-------------����˵��----------------
%    ģ���˻���
%       ���������
%               inputcities:ԭ���ĵص�˳���λ��
%       initial_temperature����ʼ�¶�
%              cooling_rate�� ���±���ϵ��
%               threshold  �� һ��ѭ������
%     numberofcitiestoswap �� ÿ�ν����ص�Ķ���  
%---------------------------------------
function  renew_SA(inputcities,initial_temperature,...
    cooling_rate,threshold,numberofcitiestoswap)             %�˻��㷨
global iterations;                    %ȫ�ֱ���--��������--��Ϊѭ������
iterations = 1;
number_interations = 0;             %����һ�������������ڽ��²���
best_cities = inputcities ;         %���ڼ�¼�Ѿ��ҵ�����ý�
best_distance = distance(best_cities);    
num2swap_change = 0;    %����һ������--����������Ŀ
tempeature = initial_temperature;       %��ʼ�¶�
input_cities = inputcities;             %��������
%while tempeature > 0.01         %ѭ���������ѽ��µ�����Ϊ����         
 while iterations < threshold    %�µ�ѭ������--��������

       num2swap_change = num2swap_change + 1;      
       previous_distance = distance(input_cities); %�ɾ����
       temp_cities = swapcities(input_cities,numberofcitiestoswap);  %���n�ν���
       current_distance = distance(temp_cities);   %�¾����
       diff = abs(current_distance - previous_distance);  %�������
       %-------------------------���õ����---------------------------
       if current_distance < previous_distance     %��������ˣ�ֱ�ӽ��ܣ����ÿ��� 
           num2swap_change = 0;                %����ѭ����ñ�����0
           input_cities = temp_cities;             %����
          %---------��¼��õĽ�--------------
           if best_distance > current_distance
               best_cities = input_cities;
               best_distance = distance(best_cities);
           end
          %---------------------------------- 
           if number_interations >= 5
              tempeature = tempeature*cooling_rate;      %���¹���
              number_interations = 0;
           end
           numberofcitiestoswap = round(numberofcitiestoswap*exp(-diff/(iterations*tempeature)));
           if numberofcitiestoswap == 0
               numberofcitiestoswap = 1;
           end
           iterations = iterations +1 ;
           number_interations = number_interations + 1;
       %---------------------�ⲻ�õ����---------------------------
       else
           if rand(1) < exp(-diff/(tempeature))   %������һ���ĸ��ʽ���
               num2swap_change = 0;
               input_cities = temp_cities;        %���ʷ����ˣ���������   
               numberofcitiestoswap = round(numberofcitiestoswap*exp(-diff/(iterations*tempeature)));
              if numberofcitiestoswap == 0
                  numberofcitiestoswap = 1;
              end
              iterations = iterations +1 ;
              number_interations = number_interations + 1;
           end
       end
       %--���һֱѭ����û�н���if�У��͵øı������������if��-----
       if num2swap_change > 100 
           input_cities = best_cities;   %--����ý�ת��input_cities��
           tempeature = tempeature/0.951; %����--ʹ�����ѭ�����ʱ��
           if numberofcitiestoswap > 1    %��������������1��ʱֹͣ
              numberofcitiestoswap = numberofcitiestoswap - 1;
              if numberofcitiestoswap == 0
                 numberofcitiestoswap = 1;
              end
            num2swap_change = 0;
           end
       end
end
   fprintf('\t\t\tTempeature = %3.8f\n',tempeature);     %������      
   current_distance = distance(input_cities);
   fprintf('\t\t\tFinal_istance = % 3.8f best_dis =  % 3.8f\n',current_distance,best_distance); 
   plot(best_cities(1,:),best_cities(2,:),'*');
   hold on,plot(best_cities(1,:),best_cities(2,:));