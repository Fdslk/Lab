function s = swapcities( inputcities, n )
%SWAPCITIES �˴���ʾ�йش˺�����ժҪ
%   �����ص�˳��
%   ���������
%   inputcities��ԭ���ĵص�˳���λ��
%   n:Ҫ�����Ĵ����������ٶԵص㽻����
%   ���������s:������ĵص�˳���λ��

s = inputcities;
for i = 1: n
    city_1 = round(length(inputcities)*rand(1));%������������㣨1~30֮�䣩round��������
    if city_1 < 1
        city_1 = 1;
    end
    city_2 = round(length(inputcities)*rand(1));% 30�������������ѡ��һ�����н��н���
    if city_2 < 1
        city_2 = 1;
    end
    temp = s(:,city_1); %�������� 
    s(:,city_1) = s(:,city_2);
    s(:,city_2) = temp;
end

