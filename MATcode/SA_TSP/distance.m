function d = distance(inputcities)
%DISTANCE �˴���ʾ�йش˺�����ժҪ
%   ������㺯��
%   ���������
%    inputcities��ԭ���ĵص�˳���λ��
%   ��������� d:˳����ӵľ����
d = 0;
for n = 1:length(inputcities)
    if n == length(inputcities) % ��β�ľ������
        % ����ĳ�������Ͼ��ǳ��ȡ���С���������˼�������￴����norm�����ǲ���x��y�������
        % ��ʵ�������˹��ɶ���
        d = d + norm(inputcities(:,n) - inputcities(:, 1));
    else
        d = d + norm(inputcities(:,n) - inputcities(:,n + 1));%����������ľ���
    end
end
end

