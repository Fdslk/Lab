import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm
import sys
input_file = sys.argv[1]
wine = pd.read_csv(input_file, sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')
print(wine.head())
print(wine.describe())
print(sorted(wine.quality.unique()))
print(wine.quality.value_counts())
print(wine.groupby('type')[['quality']].describe().unstack('type'))
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))
red_wine = wine.loc[wine['type']=='red', 'quality']
white_wine = wine.loc[wine['type']=='white', 'quality']
sns.set_style('dark')
print(sns.distplot(red_wine, norm_hist=True, kde=False, color="red", label="Red Wine"))
print(sns.distplot(white_wine, norm_hist=True, kde=False, color="white", label="White Wine"))
# sns.axlabel('Quality Score', 'Density')
plt.title('Distribution of Quality by wine type')
plt.legend()
plt.savefig('red_white_quality.png')
plt.show()

print(wine.groupby(['type'])[['quality']].agg(['std']))
tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
print('tstat: %.3f pvalue: %.4f'%(tstat, pvalue))
print(wine.corr())
def take_sample(data_frame, replace=False, n=200):
	return data_frame.loc[np.random.choice(data_frame.index, replace=replace, size=n)]

reds_sample = take_sample(wine.loc[wine['type']=='red', :])
whites_sample = take_sample(wine.loc[wine['type']=='white', :])
wine_sample = pd.concat([reds_sample, whites_sample])
wine['in_sample'] = np.where(wine.index.isin(wine_sample.index), 1., 0.)
print(pd.crosstab(wine.in_sample, wine.type, margins=True))
sns.set_style("dark")
g = sns.pairplot(wine_sample, kind='reg', plot_kws={"ci":False,\
"x_jitter":0.25, "y_jitter":0.25}, hue = 'type', diag_kind='hist',\
diag_kws={"bins":10, "alpha":1.0}, palette=dict(red="red", white="white"),
markers=["o", "s"], vars=['quality', 'alcohol', 'residual_sugar'])
print(g)
plt.suptitle('Histograms and Scatter Plots of Quality, Alcohol, and Residual Sugar', fontsize=14, \
		horizontalalignment='center', verticalalignment='top',
		x=0.5, y=0.999)
plt.show()

my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
#formula_all = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol'
#formula = 'quality ~ residual_sugar + alcohol'
lm = ols(my_formula, data=wine).fit()
#lm = glm(my_formula, data=wine, family=sm.families.Gaussian()).fit()
#lm = smf.glm(formula_all, data=wine_standardized, family=sm.families.Gaussian()).fit()
print(lm.summary())
print("\nQuantities you can extract from the result:\n%s" % dir(lm))
print("\nCoefficients:\n%s" % lm.params)
print("\nCoefficient Std Errors:\n%s" % lm.bse)
print("\nAdj. R-squared:\n%.2f" % lm.rsquared_adj)
print("\nF-statistic: %.1f  P-value: %.2f" % (lm.fvalue, lm.f_pvalue))
print("\nNumber of obs: %d  Number of fitted values: %s" % (lm.nobs, len(lm.fittedvalues)))