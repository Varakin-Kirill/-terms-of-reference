import pandas as pd

df = pd.DataFrame({
    'w': [1,1,2,2,2,3,3,3,4,4,4], 
    'user': ['User2', 'User3', 'User1', 'User1', 'User2', 'User2', 'User2', 'User3', 'User1', 'User1', 'User3'],
    'c': [7,2,3,1,2,5,4,6,9,8,7]
})

pivot_df = df.pivot_table(index='w', columns='user', values='c', aggfunc='sum', fill_value=0)

output_df = pivot_df.reset_index().melt(id_vars='w', var_name='user', value_name='cnt')

output_df = output_df.sort_values(by=['w', 'user'])

output_df['sum'] = output_df.groupby('user')['cnt'].cumsum()

print(output_df)
