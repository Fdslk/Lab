clear;
p1 = binopdf(45, 100, 0.5)
p2 = binocdf(45, 100, 0.5)
x = 1:100;
% ����ֲ����¼�Aǡ�÷���k�εĸ���
p = binopdf(x, 100, 0.5);
px = binopdf(x, 100, 0.5);
subplot(121);
plot(x, p, 'rp');
xlabel('x'); ylabel('p'); title('�ֲ�����');
axis square;
subplot(122); plot(x, px, '+');
xlabel('x'); ylabel('y');title('�����ܶȺ���');
axis square;