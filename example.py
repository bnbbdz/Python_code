# imports
import random
import time
import os
import pandas as pd
import seaborn as sns
import numpy as np
from scipy import stats as sts
import matplotlib.pyplot as plt
a4_dims = (11.7, 8.27)
plt.rcParams['figure.figsize'] = a4_dims
import warnings
warnings.filterwarnings('ignore')

#to display all rows columns 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)  
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

# to remove scientific notation
pd.set_option('display.float_format', lambda x: '%.3f' % x)

#timing your program?
import time
start = time.time()
# your code here
end = time.time()
print(end - start)

# working with date time
# convert a col to datetime pandas
df['date'] = pd.to_datetime(df['date'])

#Change working directory
import os
os.getcwd()
os.chdir("directory")
%pwd
%cd folder

# get df value
df['col'][1].item()

# create empty df with n cols & m rows

#read excel
pd.read_excel('.xlsx', sheet_name = 'Sheet1')

# remove index while exporting
df.to_csv('csv', index = False)

#importing multiple files in a directory
l = [pd.read_csv(filename) for filename in glob.glob("path\*.csv")]
df = pd.concat(l, axis = 0)
df = pd.concat(l, axis = 1)
df = df1.append(df2)
#axis - 0 row - 1 col
df = pd.merge(df1, df2, on = 'com_col', how = 'outer')

#index reset
df.reset_index(drop = True, inplace = True)

#change dtype
df.Weight = df.Weight.astype('int64')

#replace blanks with NaN
df.replace(r'^\s*$', np.nan, regex=True)

#accepts only 1D , get all unique elements in a column 
pd.unique(df['col1'])
df['col1'].unique()

#to flat 2D into 1D
df[['col1', 'col2']].values.ravel()

#to flat 2D into 1D & get only unique values
pd.unique(df[['col1', 'col2']].values.ravel())

#number of unique elements in one column
df['col1'].value_counts()

#number of unique elements in all columns
df.nunique()

#missing values
sns.heatmap(df.isnull())

# NaNs by col
df.isnull().sum(axis = 0)

#drop a column in df
df.drop(['colname'], axis = 1)

#percentile
df['col'].quantile(0.1)  #top 10 percentile

#filter columns based on names
col_list = list(df.filter(like = 'Avg_').columns)

#create a sample dataframe
df = pd.DataFrame({'col1': [1,2,3], 'col2': [11,22,33]})
df = pd.DataFrame({'x': [1,2,3], 'y':[11,22,33]}, columns = ['x1', 'y1'])

#with n cols & rows
pd.DataFrame(index=np.arange(1), columns=np.arange(8))

#sorting values by 1 col
df.sort_values(by = ['col1'], ascending = True)

#sorting values by more columns
df.sort_values(by = ['col1', 'col2', 'col3'], ascending = True)

#renaming the columns
df.rename(columns = {'col1':'rnm1', 'col2':'rnm2'}, inplace = True)

#column slicing
all = df.columns
except last one = df.columns[:-1]
mirror columns = df.columns[::-1]

#filter function
df.filter(['col1', 'col2', 'col3'])
df.filter(regex = '/d')

#upto 2 place decimal
 "{:.2f}".format(x)

#row slicing
#top 4 rows
df[:4]

#col slicing
df[(cond1) | (cond2) & (cond3)]    #where cond1 = df['col1'] > 2

#iloc & loc
df.iloc[<index>, <index>]
df.loc[(cond1), ['col1', 'col2']] #where cond1 = df['col1'] > 2

#groupby
df.groupby(by = ['col1'])['reqcols'].mean()

#replacing nan with space
df['col1'] = df['col1'].replace('whattoreplace', 'replacewith')
df = df.replace('','')
df = df.fillna('')

#drop rows with nan
df.dropna()

#converting string to datetime
df['col1'] = pd.to_datetime(df['col1'])

#summary & transpose
df.describe().transpose()

#check for null values in a column
df.isnull().any()
df.isnull().all()
df['col1'].isnull()
df['col2'].notnull()

#null values in each col
df.isna().sum()

#check for non-null values
pd.notnull()

#isin in andas
df['col1'].isin('somelist')

#dropping duplicates
#drops duplicates excluding first occurence
df.drop_duplicates()

#drops duplicates excluding last occurence
df.drop_duplicates(keep = 'last')

#drops duplicates by col
df.drop_duplicates(['col1'])
df.drop_duplicates(['col1'], keep = 'last')
df.drop_duplicates(subset = 'Col1')

#joining dataframes
#Creating a pivot
df.pivot('A', 'B', 'C') - [A - vertical, B - Horizontal, C - values]
pd.pivot_table(df, values = '', index = ['',''], columns = [''], aggfunc = np.sum)

#Unpivot
pd.DataFrame(pivoted.to_records())

#replace infinity with nan
df.replace([np.inf, -np.inf], np.nan)

#check for infinite values 
np.isfinite(df).any()

#data types of all columns
df.dtypes

#data type of a single column
df.colname.dtypes

#convert dtypes
df['col'].astype(str).astype(int)

#lambda function
lambda x : x + 10

#applying functions to a dataframe
df.apply(lambda x: x + 3)

#apply function referencing multiple columns
df['Value'] = df.apply(lambda row: my_test(row['a'], row['c']), axis=1)

#if else loop in a lambda function
df.apply(lambda x: 1 if x == 'W' else 0)

#List Comprehensions
ls = [i for i in ls1 if i not in ls2]

#numpy array methods
np.zeros((shape))
np.ones((shape))
np.full(5, -1)
np.full((2,5), -1)

#list methods
list.sort()
list.sort(reverse = true)
ls = ['a','b','c']
"".join(ls) = abc
"-".join(ls) = a-b-c
#reverse a list
list.reverse()
#remove list items
list.clear()
#remove - removes the element from the list
ls.remove(element)
list.pop[0]
#pop - last element
ls.pop()
#pop at index
ls.pop(0)
del list[0]
#get list index
list_name.index('element')
#append - adds an element to the list
ls.append(element)
#extend - adds ls2 to the end of ls1
ls1.extend(ls2)
#insert
ls.insert(position, element)
#delete - deletes the element at that index
del ls[0]
del ls[:] #deletes all elements from the list

#enumerate
enumerate(iterable, start)
li = ['a','b','c']
ob = enumerate(li)

#String methods
str.endswith('pattern')


#JUPYTER MARKDOWN
HEADERS
#h1
##h2
######h6
LISTS
*item1
*item2
 *item3
 *item4
IMAGES
![alt text](url)
EMPHASIS
*italic*
_italic_
**bold**
__bold__
*italic **bold** combine*
ORDERED LIST
1. item
2. item
 *item
 *item
LINKS
[text](url)
BLOCKQUOTES
>line 1
>line 2
BACKSLASH ESCAPES
\* literal asterisks\*
MATHEMATICAL SYMBOLS
$symbol$

https://www.google.com/search?q=python+bitwise+operators&rlz=1C1CHWL_viVN969VN969&sxsrf=APq-WBs9hd2GGd-b3uVyWlBe78JecPsgCQ:1646151243719&source=lnms&tbm=isch&sa=X&ved=2ahUKEwitk4Ohp6X2AhVRIqYKHQ73A8IQ_AUoAnoECAEQBA&biw=1858&bih=977&dpr=1#imgrc=eWdcDCHfvFm57M
https://www.google.com.vn/search?q=python+Arithmetic+Operations&sxsrf=APq-WBsZt7y-6wb8zbsniu29RQTjOuFy1Q:1646151392865&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjrsJLop6X2AhURQfUHHX0HDyUQ_AUoAXoECAEQAw&biw=1858&bih=977&dpr=1#imgrc=ePcJLbef-zI8dM
https://docs.microsoft.com/en-us/sql/machine-learning/python/python-libraries-and-data-types?view=sql-server-ver15

#SQL -> Python

Hàm Select
select all
-- SQL
select * from table
# python
table
select column
-- SQL
select col1 from table
# python
table.col1
select distinct
-- SQL
select distinct * from table
# python
table1.drop_duplicates()
Hàm Where
Where = x
-- SQL
select * from table1 where col1 = 5
# python
table.loc[table['column_name'] == 5]
Where <> x
-- SQL
select * from table1 where col1 <> 5
# python
table.loc[table['column_name'] != 5]
Where > x
-- SQL
select * from table1 where col1 > 5
# python
table1[col1 > 5]
Where chứa string
-- SQL
select * from table1 where col1 like '%string%'
# python
table[‘col1’].str.contains('string')]
Where bắt đầu bằng string
-- SQL
select * from table1 where col1 like 'string%'
# python
table.loc[.str.startswith('string')]
Where kết thúc bằng string
-- SQL
select * from table1 where col1 like '%string'
# python
table.loc[.str.endsswith('string')]
Where null
-- SQL
select * from table1 where col1 is null
# python
table[‘col1’].isna()
Where not null
-- SQL
select * from table1 where col1 is not null
# python
table[‘col1’].notna()
Hàm Update
Update 1 cột có điều kiện
-- SQL
update table set col2 = 'Y' where col1 > 10
# python
table.loc[table.col1 > 10, ‘col2’] = ‘Y’
Update 1 cột nhiều điều kiện
-- SQL
update table set col3 = 'Y' where col1 > 10 and col2 = 'x'
# python
table.loc[(table.col1 > 10) & (table.col2 == ‘x’), ‘col3’] = ‘Y’
Thay bằng 0 khi null
-- SQL
update table set col1 = 0 where col1 is null
# python
table.loc[table[‘col1’].isnull(), ‘col1’] = 0
Thay giá trị cột này bằng cột khác
-- SQL
update table set col2 = col1*100 where col1 > 10
# python
table.loc[table.col1 > 10, ‘col2’] = table.col*100
Hàm Join
Join left một điều kiện
-- SQL
select * from table1 a left join table2 b 
on a.name = b.name
# python
table = pd.merge(table1, table2, left_on = ['name'], right_on = ['name'], how = 'left')
Join right nhiều điều kiện
-- SQL
select * from table1 a right join table2 b 
on a.name = b.name and a.id = b.id
# python
table = pd.merge(table1, table2, left_on = ['name', 'id' ], right_on = ['name', 'id'], how = 'right')
Join Inner nhiều bảng nhiều điều kịen
select * from table1 a inner join table2 b 
on a.name = b.name
inner join table3 c 
on a.name = c.name
# python
table = pd.merge(table1, table2, left_on = ['name'], right_on = ['name'], how = 'inner')
table = pd.merge(table, table3, left_on = ['name'], right_on = ['name'], how = 'inner')
Sort
Sort bảng theo 1 cột
-- SQL
select * from table sort by id asc
# python
table.sort_values(by=[‘id’], inplace=True, ascending = True)
Sort bảng theo nhiều cột
-- SQL
select * from table sort by id, name
# python
table.sort_values(by=[‘id’, ‘name’], inplace=True, ascending = False)

https://towardsdatascience.com/8-popular-sql-window-functions-replicated-in-python-e17e6b34d5d7
https://towardsdatascience.com/pandas-equivalent-of-10-useful-sql-queries-f79428e60bd9