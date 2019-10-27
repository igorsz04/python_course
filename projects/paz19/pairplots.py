from scipy import stats

import seaborn as sns
import matplotlib.pyplot as plt


sns.set(style='ticks')

tips = sns.load_dataset("tips")
print(tips.describe())
print(tips.head())

# g = sns.FacetGrid(tips, col='time', hue='smoker')
# g.map(plt.scatter, 'total_bill', 'tip')
# g.add_legend()
#
# g = sns.FacetGrid(tips,row='smoker', col='time', margin_titles=True,hue='day')
# g.map(sns.regplot, 'size','total_bill',fit_reg=False, x_jitter=.1)
# g.add_legend()
#
# g = sns.FacetGrid(tips, col='day', height=4, aspect=.5)
# g.map(sns.barplot, 'sex', 'total_bill')


# print('\nordered days:')
# ordered_days = tips.day.value_counts().index
# g=sns.FacetGrid(tips, row='day', row_order=ordered_days, height=1.7, aspect=4)
# g.map(sns.distplot, 'total_bill',hist=False, rug=True)
# print(ordered_days)


# def quantile_plot(x,**kwargs):
#     qntls, xr=stats.probplot(x, fit=False)
#     plt.scatter(xr, qntls, **kwargs)
#
# g=sns.FacetGrid(tips,col='sex',height=4)
# g.map(quantile_plot,'total_bill', "tip")
# g.add_legend()


iris = sns.load_dataset("iris")
g = sns.PairGrid(iris, hue='species')
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)

sns.pairplot(iris, hue='species')

plt.show()

