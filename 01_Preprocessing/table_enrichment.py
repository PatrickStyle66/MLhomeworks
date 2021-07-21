import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
#carregando a base
data = pd.read_csv('diabetes_dataset.csv')


print(data)
#exibindo informações da base
data.info()
#checando quantos dados nulos temos em cada coluna
print(data.isnull().sum())

#faz a média dos dados de cada atributo que possui valores nulos, tanto para o resultado positivo quanto negativo
print('média de glucose para positivo:'+ str(data.Glucose[data.Outcome == 1].mean()))
print('média de glucose para negativo:'+ str(data.Glucose[data.Outcome == 0].mean())+'\n')
print('média de pressão sanguínea para positivo:'+ str(data.BloodPressure[data.Outcome == 1].mean()))
print('média de pressão sanguínea para negativo:'+ str(data.BloodPressure[data.Outcome == 0].mean())+'\n')
print('média de grossura da pele para positivo:'+ str(data.SkinThickness[data.Outcome == 1].mean()))
print('média de grossura da pele para negativo:'+ str(data.SkinThickness[data.Outcome == 0].mean())+'\n')
print('média de insulina para positivo:'+ str(data.Insulin[data.Outcome == 1].mean()))
print('média de insulina para negativo:'+ str(data.Insulin[data.Outcome == 0].mean())+'\n')
print('média de BMI para positivo:'+ str(data.BMI[data.Outcome == 1].mean()))
print('média de BMI para negativo:'+ str(data.BMI[data.Outcome == 0].mean())+'\n')

#substitui os valores nulos por suas respectivas médias de atributo
data.Glucose[(data.Glucose.isnull()) & (data.Outcome == 1) ] = data.Glucose[data.Outcome == 1].mean()
data.Glucose[(data.Glucose.isnull()) & (data.Outcome == 0) ] = data.Glucose[data.Outcome == 0].mean()
data.BloodPressure[(data.BloodPressure.isnull()) & (data.Outcome == 1) ] = data.BloodPressure[data.Outcome == 1].mean()
data.BloodPressure[(data.BloodPressure.isnull()) & (data.Outcome == 0) ] = data.BloodPressure[data.Outcome == 0].mean()
data.SkinThickness[(data.SkinThickness.isnull()) & (data.Outcome == 1) ] = data.SkinThickness[data.Outcome == 1].mean()
data.SkinThickness[(data.SkinThickness.isnull()) & (data.Outcome == 0) ] = data.SkinThickness[data.Outcome == 0].mean()
data.Insulin[(data.Insulin.isnull()) & (data.Outcome == 1) ] = data.Insulin[data.Outcome == 1].mean()
data.Insulin[(data.Insulin.isnull()) & (data.Outcome == 0) ] = data.Insulin[data.Outcome == 0].mean()
data.BMI[(data.BMI.isnull()) & (data.Outcome == 1) ] = data.BMI[data.Outcome == 1].mean()
data.BMI[(data.BMI.isnull()) & (data.Outcome == 0) ] = data.BMI[data.Outcome == 1].mean()
#checa novamente se ainda existem dados nulos
print(data.isnull().sum())

#cria uma árvore de decisão para ajudar a escolher os atributos mais importantes
clf = DecisionTreeClassifier(random_state=1234)
attrs = data.drop(data.columns[[0,9]], axis=1, inplace=False)
Dtree = clf.fit(attrs,data.Outcome)
#determina a importância de cada atributo
importance = Dtree.feature_importances_
for i,v in enumerate(importance):
    print('atributo: %0d, Score: %.5f' % (i,v))
#remove os atributos considerados menos importantes
data.drop(data.columns[[0,1,3,6,7]],axis=1, inplace=True)
#Recria o csv com as novas informações
data.to_csv('diabetes_dataset.csv')