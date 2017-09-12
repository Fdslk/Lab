function y = fun(x, dim)
%²âÊÔº¯Êý
y = 0;
for i = 1:dim - 1
y = y + 100*(x(i+1).^2 - x(i)).^2 + (1-x(i)).^2;
end

