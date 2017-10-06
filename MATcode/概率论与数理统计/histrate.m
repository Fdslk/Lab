function s = histrate( x )
%HISTRATE 此处显示有关此函数的摘要
%   此处显示详细说明
if isnumeric(x)
    x = x(:);
    x = x(~isnan(x)); % isnan 判断元素是否为数字
    xid = [];
else
    [x, xid] = grp2idx(x); 
    x = x(~isnan(x));
end
x = sort(x(:));
m = length(x);
x1 = diff(x); % 数组中的前一项减后一项
x1(end+1) = 1;
x1 = find(x1);
Freq = x1/m;
value = x(x1);
x1 = [0; x1];
Freq1 = diff(x1);
Freq2 = Freq1/m;
if nargout == 0
    if isempty(xid)
        fmt1 = '%11s    %8s    %6s        %6s\n';
        fmt2 = '%10d    %8d    %6.2f%%    %6.2f%%\n';
        fprintf(1, fmt1, '取值', '频数', '频率', '累计频率');
        fprintf(1, fmt2, [value'; Freq1'; 100*Freq2'; 100*Freq']);
    else
        head = {'取值', '频数', '频率(%)', '累计频率(%)'};
        [head; xid, num2cell([Freq1, 100*Freq2, 100*Freq])];
    end
else
    if isempty(xid)
        s = [value Freq1 Freq2 Freq];
    else
        s = [xid, num2cell([Freq1, Freq2, Freq])];
    end
end

