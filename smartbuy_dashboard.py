import plotly.express as px
import pandas as pd

#data and dataframes:
def parse_dataset(number):
    
    path = f'./data/pis_{number}.csv'
    df = pd.read_csv(path, names=['category', 'month', 'year', 'clicks'], skiprows=1)
    return df

df_all = pd.DataFrame(columns=['category', 'month', 'year', 'clicks'])

for number in range(1, 101):
    df_temp=pd.DataFrame(parse_dataset(number))
    df_all=pd.concat([df_all, df_temp], ignore_index=True)

df=df_all.dropna(inplace=True)
df = df_all.sort_values(['month', 'category'])
df['category'] = df['category'].str.title()

bin_labels = ['Winter', 'Spring', 'Summer', 'Fall', 'Winter']
bin_boundaries = [ 0.9, 2, 5, 8, 11, 12.1]
df['season'] = pd.cut(df['month'], bins=bin_boundaries, labels=bin_labels, ordered=False)

df.reset_index(inplace=True)
df.drop('index', axis='columns', inplace=True)


df_winter = df[df['season']=='Winter']
df_spring = df[df['season']=='Spring']
df_summer = df[df['season']=='Summer']
df_fall = df[df['season']=='Fall']
df_total = df.groupby('month')[['clicks']].agg('sum')
df_alltime_greats = df.groupby('category').agg('sum').sort_values('clicks', ascending=False).head(10)
df_alltime_greats = df_alltime_greats.reset_index()

df_monthly_top_cat = pd.DataFrame()
for month in range(1,13):
    df_temp = df[df['month']==month]
    df_temp = df_temp.sort_values('clicks', ascending=False).head(1)
    df_monthly_top_cat = pd.concat([df_monthly_top_cat, df_temp])

df_seasonal_cat = pd.DataFrame()
categories = df['category'].unique().tolist()

for category in categories:
    df_temp = df[df['category']==f'{category}']
    df_temp = df_temp.groupby(['category', 'season']).agg('mean').sort_values('clicks', ascending=False).head(1)
    df_seasonal_cat = pd.concat([df_seasonal_cat, df_temp])
df_seasonal_cat.reset_index(inplace=True)
df_seasonal_cat= df_seasonal_cat.rename(columns={'season':'top_selling_season', 'clicks':'average_clicks'})
df_seasonal_cat = df_seasonal_cat.sort_values(['category'])

#flops
df_flops = df.groupby('category').agg('sum').sort_values('clicks', ascending=True).head(10)
df_flops = df_flops.reset_index()
#volatile categories
df_volatile_categories = df.groupby(['category'])[['month', 'clicks']].std().sort_values('clicks', ascending=False).head(10)
vol_cat_list = df_volatile_categories.index.tolist()
df_volatile_new = df[df['category'].isin(vol_cat_list)]
df_volatile_new = df_volatile_new.dropna()
#stable categories
df_stable_categories = df.groupby(['category'])[['month', 'clicks']].std().sort_values('clicks', ascending=True).head(10)
stable_cat_list = df_stable_categories.index.tolist()
df_stable_new = df[df['category'].isin(stable_cat_list)]
df_stable_new = df_stable_new.dropna()
#spring sellers
df_spring_sellers = df_spring.groupby(['category']).agg('mean').sort_values('clicks', ascending=False).head(10)
x = df_spring_sellers.index.tolist()
df_top_spring = df[df['category'].isin(x)]
#summer sellers
df_summer_sellers = df_summer.groupby(['category']).agg('mean').sort_values('clicks', ascending=False).head(10)
su = df_summer_sellers.index.tolist()
df_top_summer = df[df['category'].isin(su)]
#fall sellers
df_fall_sellers = df_fall.groupby(['category']).agg('mean').sort_values('clicks', ascending=False).head(10)
fa = df_fall_sellers.index.tolist()
df_top_fall = df[df['category'].isin(fa)]
#winter sellers
df_winter_sellers = df_winter.groupby(['category']).agg('mean').sort_values('clicks', ascending=False).head(10)
wi = df_winter_sellers.index.tolist()
df_top_winter = df[df['category'].isin(wi)]

#logo
image_path = './eCommerce_business_case_logo.png'



#plots:
#overall clicks per year:
fig_1 = px.line(df_total, title='Total Clicks 2021',
              height=850, width=1700,
              labels={'value': 'Total Clicks',
                    'month': 'Months of the Year'}
               )
              
fig_1.update_layout(
    font_family='Helvetica',
    font_color='black',
    title_font_family='Helvetica',
    title_font_color="rgb(102,17,0)",
    title_font_size=40
    #legend_title_font_color="green"
    )

fig_1.update_layout(showlegend=False)
fig_1.update_xaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_1.update_yaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_1.update_traces(line_color='rgb(217,95,2)', line_width=5)


fig_2 = px.bar(df_total, title='Total Clicks 2021',
              height=850, width=1700,
              labels={'value': 'Total Clicks',
                    'month': 'Months of the Year'}     
              )
fig_2.update_layout(
    font_family='Helvetica',
    font_color='black',
    title_font_family='Helvetica',
    title_font_color="rgb(102,17,0)",
    title_font_size=40
    )
fig_2.update_layout(showlegend=False)
fig_2.update_xaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_2.update_yaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_2.update_traces(marker_color='rgb(217,95,2)')

fig_3 = fig = px.bar(df_alltime_greats, x='clicks', y='category',
            height=850, width=1700, title='Alltime Favorites',
            labels={'category': 'Category',
                    'clicks': 'Total clicks 2021'}
            )
fig_3.update_layout(
    font_family='Helvetica',
    font_color='black',
    title_font_family='Helvetica',
    title_font_color="rgb(102,17,0)",
    title_font_size=40
)
fig_3.update_xaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_3.update_yaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_3.update_traces(marker_color='rgb(217,95,2)')

### 4. Most clicked category / month
fig_4 = px.bar(df_monthly_top_cat, x='month', y='clicks',
               color = 'category', title = 'Most clicked category per month',
               height=850, width=1700,
               labels={'clicks': 'Total clicks per month', 'month': 'Month of the Year'}              
              )

fig_4.update_layout(
    font_family='Helvetica',
    font_color='black',
    title_font_family='Helvetica',
    title_font_color="rgb(102,17,0)",
    title_font_size=40,
    legend_title_font_size=30,
    legend_title='Categories'
    )

fig_4.update_layout(showlegend=True)
fig_4.update_xaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_4.update_yaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_4.update_layout(legend=dict(title_font_family="Helvetica",
                              font=dict(size= 30)))


### 5. All categories and their best-selling season:
fig_5 = px.scatter(df_seasonal_cat, y="top_selling_season", x="average_clicks", color="category",
                  height=850, width=1700,
                  title='Highest average clicks per season',
                  labels={'top_selling_season': 'Seasonal High of Category',
                   'average_clicks': 'Avergage Clicks in Season'})
                  

fig_5.update_traces(marker_size=25)
fig_5.update_layout(
    font_family='Helvetica',
    font_color='black',
    title_font_family='Helvetica',
    title_font_color="rgb(102,17,0)",
    title_font_size=40,
    legend_title_font_size=30,
    legend_title='Categories'
)

fig_5.update_layout(showlegend=True)
fig_5.update_xaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_5.update_yaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_5.update_layout(legend=dict(title_font_family="Helvetica",
                              font=dict(size= 30)))

### 6. Flops
fig_6 = px.bar(df_flops, x='clicks', y='category',
            height=850, width=1700, title='Flop Category',
            labels={'category': 'Category',
                    'clicks': 'Total clicks 2021'}
            )
fig_6.update_layout(
    font_family='Helvetica',
    font_color='black',
    title_font_family='Helvetica',
    title_font_color="rgb(102,17,0)",
    title_font_size=40
    #legend_title_font_color="green"
)
fig_6.update_xaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_6.update_yaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_6.update_traces(marker_color='rgb(217,95,2)')

# 7. Volatile Categories
fig_7 = px.line(df_volatile_new, x='month', y='clicks', 
               color='category', height=850, width=1900, title='Volatile Categories',
               labels={'clicks': 'Total Clicks per Month', 'month': 'Month of the Year'})
fig_7.update_traces(line_width=5)
fig_7.update_layout(
    font_family='Helvetica',
    font_color='black',
    title_font_family='Helvetica',
    title_font_color="rgb(102,17,0)",
    title_font_size=40,
    legend_title_font_size=30,
    legend_title='Categories')
fig_7.update_layout(showlegend=True)
fig_7.update_xaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_7.update_yaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_7.update_layout(legend=dict(title_font_family="Helvetica",
                              font=dict(size= 30)))

# 8. Stable Categories
fig_8 = px.line(df_stable_new, x='month', y='clicks',
               color='category', height=850, width=1800, title='Stable Categories',
               labels={'clicks': 'Total Clicks per Month', 'month': 'Month of the Year'})
fig_8.update_traces(line_width=5)
fig_8.update_layout(
    font_family='Helvetica',
    font_color='black',
    title_font_family='Helvetica',
    title_font_color="rgb(102,17,0)",
    title_font_size=40,
    legend_title_font_size=30,
    legend_title='Categories'
)
fig_8.update_layout(showlegend=True)
fig_8.update_xaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_8.update_yaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_8.update_layout(legend=dict(title_font_family="Helvetica",
                              font=dict(size= 30)))


# 9. Top: Spring Sellers
fig_9 = px.line(df_top_spring, x='month', y='clicks',
             color='category', height=850, width=1700, title='Spring Top Categories',
             labels={'clicks': 'Total Clicks per Month', 'month': 'Month of the Year'})
fig_9.update_traces(line_width=5)
fig_9.update_layout(
    font_family='Helvetica',
    font_color='black',
    title_font_family='Helvetica',
    title_font_color="rgb(102,17,0)",
    title_font_size=40,
    legend_title_font_size=30,
    legend_title='Categories'
)
fig_9.update_layout(showlegend=True)
fig_9.update_xaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_9.update_yaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_9.update_layout(legend=dict(title_font_family="Helvetica",
                              font=dict(size= 30)))


# 10. Top: Summer Sellers
fig_10 = px.line(df_top_summer, x='month', y='clicks',
             color='category', height=850, width=1700, title='Summer Top Categories',
             labels={'clicks': 'Total Clicks per Month', 'month': 'Month of the Year'})
fig_10.update_traces(line_width=5)
fig_10.update_layout(
    font_family='Helvetica',
    font_color='black',
    title_font_family='Helvetica',
    title_font_color="rgb(102,17,0)",
    title_font_size=40,
    legend_title_font_size=30,
    legend_title='Categories'
)
fig_10.update_layout(showlegend=True)
fig_10.update_xaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_10.update_yaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_10.update_layout(legend=dict(title_font_family="Helvetica",
                              font=dict(size= 30)))


# 11. Top: Fall Sellers
fig_11 = px.line(df_top_fall, x='month', y='clicks',
             color='category', height=850, width=1700, title='Fall Top Categories',
             labels={'clicks': 'Total Clicks per Month', 'month': 'Month of the Year'})
fig_11.update_traces(line_width=5)
fig_11.update_layout(
    font_family='Helvetica',
    font_color='black',
    title_font_family='Helvetica',
    title_font_color="rgb(102,17,0)",
    title_font_size=40,
    legend_title_font_size=30,
    legend_title='Categories'
)
fig_11.update_layout(showlegend=True)
fig_11.update_xaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_11.update_yaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_11.update_layout(legend=dict(title_font_family="Helvetica",
                              font=dict(size= 30)))


#12. Top: Winter Sellers
fig_12 = px.line(df_top_winter, x='month', y='clicks',
             color='category', height=850, width=1900, title='Winter Top Categories',
             labels={'clicks': 'Total Clicks per Month', 'month': 'Month of the Year'})
fig_12.update_traces(line_width=5)
fig_12.update_layout(
    font_family='Helvetica',
    font_color='black',
    title_font_family='Helvetica',
    title_font_color="rgb(102,17,0)",
    title_font_size=40,
    legend_title_font_size=30,
    legend_title='Categories')
fig_12.update_layout(showlegend=True)
fig_12.update_xaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_12.update_yaxes(tickfont_size=30, title_font_family='Helvetica', titlefont=dict(size=30), title_font_color='rgb(102,17,0)')
fig_12.update_layout(legend=dict(title_font_family="Helvetica",
                              font=dict(size= 30)))

###LAYOUT
from dash import Dash, html, dcc # import the needed dash tools

app = Dash('smartbuy') # instantiate a Dash object called app

app.layout = html.Div(children=[
    
    html.Br(),
    
    html.H1(children='Inside SmartBuy',
            style={
            'textAlign': 'center',
            'font-family': 'Helvetica',
            'font-size': '60px'}),

    html.Div(children=
        "A visual analysis of our shopping categories' seasonality.",
        style={'textAlign': 'center',
               'font-family': 'Helvetica',
               'font-size': '40px'}
               ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    html.Img(src=app.get_asset_url('eCommerce_business_case_logo.png'), style={'display': 'block',
        'margin-left': 'auto',
        'margin-right': 'auto',
        'width': '40%',
        'height':'40%'}),
    
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),


    html.H1(children='Overall Numbers',
            style={
            'textAlign': 'left',
            'font-family': 'Helvetica',
            'font-size': '40px'}),        

    dcc.Graph(
        id='Total clicks line',
        figure=fig_1),
    
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dcc.Graph(
        id='Total clicks bar',
        figure=fig_2),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dcc.Graph(
        id='Alltime favorites',
        figure=fig_3),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dcc.Graph(
        id='Flop Categories',
        figure=fig_6),

    html.Br(),
    html.Br(),
    html.H1(children='Seasonality of Categories',
            style={
            'textAlign': 'left',
            'font-family': 'Helvetica',
            'font-size': '40px'}),

    dcc.Graph(
        id='Popular Categories per month',
        figure=fig_4),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dcc.Graph(
        id='Highest average clicks per season',
        figure=fig_5),
    
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dcc.Graph(
        id='Spring Favorites',
        figure=fig_9),
    
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dcc.Graph(
        id='Summer Favorites',
        figure=fig_10),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dcc.Graph(
        id='Fall Favorites',
        figure=fig_11),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dcc.Graph(
        id='Winter Favorites',
        figure=fig_12),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

     dcc.Graph(
        id='Volatile Categories',
        figure=fig_7),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dcc.Graph(
        id='Stable Categories',
        figure=fig_8),
    
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    html.H1(children='Recommendations:',
            style={
            'textAlign': 'left',
            'font-family': 'Helvetica',
            'font-size': '60px'}), 

    html.Br(),
    html.Br(),
    html.Br(),

    html.H1(children='- smoothen out the lows in total clicks over the year',
            style={
            'textAlign': 'left',
            'font-family': 'Helvetica',
            'font-size': '40px'}), 

     html.Br(),

    html.H1(children='- boost our overall not so popular categories',
            style={
            'textAlign': 'left',
            'font-family': 'Helvetica',
            'font-size': '40px'}), 

    html.Br(),

    html.H1(children='- ensure stock of the most popular categories each season',
            style={
            'textAlign': 'left',
            'font-family': 'Helvetica',
            'font-size': '40px'}), 

    html.Br(),

    html.H1(children='- smoothen out the seasonality of the volatile categories with special offers',
            style={
            'textAlign': 'left',
            'font-family': 'Helvetica',
            'font-size': '40px'}),
    
    html.Br(),
    html.Br(),
    html.Br()

    ])

if __name__ == '__main__':
    app.run_server(debug=True) # runs a local server for the dashboard app to run on

