function x = decode(a, low, up, length, d)
% �Ӻ��������뺯��
% a Ϊ������壬������ֳ����˺�ֱ����õ�����������ֵ
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

