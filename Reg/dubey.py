import pandas
z=input("Enter that u wat to pridict")
z=float(z)
ds=pandas.read_csv("Salary_Data.csv")
x=ds["YearsExperience"].values
x=x.reshape(-1,1)
y=ds["Salary"]
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x,y)
p=model.predict([[z]])
print(p)