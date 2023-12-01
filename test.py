import pandas as pd  
info = pd.DataFrame({'data1': [2, 4, 8, 0],  
'data2': [2, 0, 0, 0],  
'data3': [10, 2, 1, 8]},  
index=['John', 'Parker', 'Smith', 'William'])  
info  
info['data1'].sample(n=3, random_state=1)  
info.sample(frac=0.5, replace=True, random_state=1)  
info.sample(n=2, weights='data3', random_state=1)  
import pandas as pd   
# define data frame from csv file    
data = pd.read_csv("aa.csv")   
 # randomly select one row    
row1 = data.sample(n = 1)     
# display row  
row1  
# randomly select another row   
row2 = data.sample(n = 2)   
# display  row  
row2  