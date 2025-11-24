import pandas as pd
df=pd.read_csv('titanic.csv')
pd.set_option('display.max_columns',None)
df['Age'].fillna(df['Age'].median(), inplace=True)
df['FamilySize']=df['Parch']+1+df['SibSp']
#1 print(df.info())
#2 print(len(df['Sex']=='male'))
#4 print(df.groupby('Pclass')['Survived'].mean())
#5 print(df['Age'].median())
#6 print(df['FamilySize'][15:16])

#8.1print(len(df[ (df['Sex']=='female') & (df['Survived']==1) & (df['Pclass']==1)]))
#8.2print(len(df[(df['Parch']==0)&(df['Age']<18)]))