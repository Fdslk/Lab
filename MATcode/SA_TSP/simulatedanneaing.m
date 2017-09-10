function simulatedanneaing( inputcities, initial_temperature,...
    cooling_rate,threshold,numberofcitiestoswap)

%-------------����˵��----------------
%    ģ���˻���
%       ���������
%               inputcities:ԭ���ĵص�˳���λ��
%       initial_temperature����ʼ�¶�
%              cooling_rate�� ���±���ϵ��
%               threshold  �� һ��ѭ������
%     numberofcitiestoswap �� ÿ�ν����ص�Ķ���  
%---------------------------------------
temperature = initial_temperature; %��ʼ�¶�
input_cities = inputcities; %��������
plot(input_cities(1,:), input_cities(2,:),'*'); % ������ʼͼ�������Ա�
hold on, plot(input_cities(1,:), input_cities(2, :));
figure;
while temperature > 0.01 % ѭ���������ѽ��µ�����Ϊ����
    for i = 1:threshold % ѭ������
        previous_distance = distance(input_cities); %�ɾ����
        temp_cities = swapcities(input_cities, numberofcitiestoswap);%���n�ν���
        current_distance = distance(temp_cities); %�¾����
        diff = abs(current_distance - previous_distance); %�������
        if current_distance < previous_distance %��������ˣ�ֱ�ӽ��ܣ����ÿ���
            input_cities  = temp_cities; %����
        elseif rand(1) < exp(-diff/(temperature)) % �¶Ƚ��ͺ󣬷��ϵ��˻�̬�¶ȣ�Ȼ��仯�ͻ��𽥽��ͣ������Щ���ľ��뱻�����ĸ��ʾͻή��
            input_cities = temp_cities; % ���ʷ����ˣ���������
        end
    end
    temperature = temperature * cooling_rate; % ���¹���
end
    % ��ʾ���
fprintf('\t\t\tTemperature = %3.8f\n', temperature);
current_distance = distance(input_cities);
fprintf('\t\t\tFinal_distance = %3.8f\n', current_distance);
plot(input_cities(1,:), input_cities(2, :), '*');
hold on, plot(input_cities(1, :),  input_cities(2, :));
end


