import matplotlib.pyplot as plt
plt.style.use('ggplot')
customers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']
customers_index = range(len(customers))
sales_amounts = [127, 90, 201, 111, 232]
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.bar(customers_index, sales_amounts, align='center', color='darkblue')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xticks(customers_index, sales_amounts, rotation=45, fontsize='small')
plt.xlabel('Customer Name')
plt.ylabel('sales Amount')
plt.title('Sales Amount per Customer')
plt.savefig('bar_plot.png', dpi=400, bbox_inches='tight')
plt.show()