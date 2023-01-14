import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import json
import requests
import time

# ============================ FUNCTIONS ===============================
# -------- Update chart layout -------------
def chart_update_layout(figure, x_axis, y_axis):
    figure.update_layout(
        font_size=12,
        #width=450,
        height=300,
        autosize=True,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(14,17,23,255)',
        margin=dict(l=20, r=20, t=20, b=20),
        hovermode='x unified',
        hoverlabel=dict(
            bgcolor="rgba(100,100,100,0.3)",
            font_size=14,
            #font_family="Rockwell"
        ),

        legend_title_text='',
        legend=dict(
            orientation='h',
            yanchor='top',
            y=1.2,
            xanchor='left',
            x=0.01,
            font=dict(
                size=12,
                color="white"
            ),
            bgcolor="rgba(0,0,0,0)",
            bordercolor="rgba(0,0,0,0)",
            borderwidth=2
        ),
        legend_font=dict(size=12),  # legend location


        xaxis=dict(
            title=x_axis,
            title_font=dict(size=14, color='rgba(170,170,170,0.7)'), #, family='Arial Black'
            gridcolor='rgba(100,100,100,0.3)',
            linecolor='rgba(100,100,100,0.7)',
            tickfont=dict(color='rgba(100,100,100,1)')
            # rangeslider=dict(bgcolor='rgba(0,0,0,0)',yaxis_rangemode='auto')
        ),

        yaxis=dict(
            title=y_axis,
            title_font=dict(size=14, color='rgba(171,171,171,0.7)'), #, family='Arial Black'
            title_standoff=3,
            gridcolor='rgba(100,100,100,0.3)',
            linecolor='rgba(100,100,100,0.7)',
            tickfont=dict(color='rgba(100,100,100,1)')
        )
    )


# ============================ HISTORICAL DAILY TIME SERIES ===============================
## ------ DATA ----------
UniLP = 'https://node-api.flipsidecrypto.com/api/v2/queries/65d08749-498e-4406-aa54-62ab91b210b5/data/latest'
df_unilp_ttl = pd.read_json(UniLP)

OrcaLPSplit = 'https://node-api.flipsidecrypto.com/api/v2/queries/d8efa2d6-ba9c-4610-ae0b-bf2bcbe80b7c/data/latest'
df_orcalp_splitpool = pd.read_json(OrcaLPSplit)
df_orcalp_bonk = df_orcalp_splitpool.loc[:'2023-01-01 00:00:00.000']
df_orcalp_bonk['POOL BONK?'] = df_orcalp_bonk['POOL_ADDRESS_NAME'].str.contains("BONK")

OrcaLPTtl = 'https://node-api.flipsidecrypto.com/api/v2/queries/2ec0ad61-7b05-4a13-82a0-423d39dc0e6f/data/latest'
df_orcalp_ttl = pd.read_json(OrcaLPTtl)

OrcaDailyHist = 'https://node-api.flipsidecrypto.com/api/v2/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3/data/latest'
df_orca_daily = pd.read_json(OrcaDailyHist)
df_orca_daily.loc[df_orca_daily['NUM_TRX'] <= 50, 'POOL NAME'] = 'OTHER'
df_orca_daily.loc[df_orca_daily['NUM_TRX'] > 50, 'POOL NAME'] = df_orca_daily['POOL_ADDRESS_NAME']


#df_orca_daily['2023'] = df_orca_daily['DT'].str.contains("2023", regex=False)
df_orca_bonk = df_orca_daily.loc[:'2023-01-01 00:00:00.000']
df_orca_bonk['POOL BONK?'] = df_orca_bonk['POOL_ADDRESS_NAME'].str.contains("BONK", regex=False)


df_unilp_ttl['AVG_LP_ADJ_MA'] = df_unilp_ttl['AVG_LP_ADJ'][::-1].rolling(7).mean()[::-1].replace(np.nan, 'None')

df_orcalp_ttl['AVG_LP_ADJ_MA'] = df_orcalp_ttl['AVG_PRICERANGE_ADJ'][::-1].rolling(7).mean()[::-1].replace(np.nan, 'None')

#df_orca_daily[''] = df_unilp_ttl['AVG_LP_ADJ'][::-1].rolling(7).mean()[::-1].replace(np.nan, 'None')


## ------ PLOTS ----------
# --> LP avg adj (UNI)
fig_lp_adj_uni = px.line(df_unilp_ttl, x='DT', y='AVG_LP_ADJ_MA', labels ={'DT':'Date', 'AVG_LP_ADJ_MA':'7-Day MA'}
                ,color_discrete_sequence=['white']
                ,hover_data={'DT':False,'AVG_LP_ADJ_MA':True} )
fig_lp_adj_uni.add_bar(x=df_unilp_ttl['DT'],y=df_unilp_ttl['AVG_LP_ADJ'], name="# LP Position Adjustment / day"
                     ,marker_color='rgba(255,171,171,255)')
chart_update_layout(fig_lp_adj_uni, "", "Daily LP Position Adjustment on Uniswap")

#--> LP avg adj (ORCA)
fig_lp_adj_orca = px.line(df_orcalp_ttl, x='DT', y='AVG_LP_ADJ_MA', labels ={'DT':'Date', 'AVG_LP_ADJ_MA':'7-Day MA'}
                ,color_discrete_sequence=['white']
                ,hover_data={'DT':False,'AVG_LP_ADJ_MA':True} )
fig_lp_adj_orca.add_bar(x=df_orcalp_ttl['DT'],y=df_orcalp_ttl['AVG_PRICERANGE_ADJ'], name="# LP Position Adjustment / day"
                     ,marker_color='rgba(131,201,255,255)')
chart_update_layout(fig_lp_adj_orca, "", "Daily LP Position Adjustment on Orca")


#--> Active LP (Orca)
fig_lp_num_pool = px.bar(df_orcalp_splitpool,x='DT',y='NUM_USERS',color='POOL_ADDRESS_NAME'
                           , hover_data={'DT': False, 'NUM_USERS': True}
                           ).update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20), yaxis=dict(title='Number of Active LPs'))
fig_lp_pool_bonk = px.bar(df_orcalp_bonk,x='DT',y='NUM_USERS',color='POOL BONK?'
                           , hover_data={'DT': False, 'NUM_USERS': True}
                           ).update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20), yaxis=dict(title='Number of Active LPs'))


# --> $ORCA Price
fig_hist_prc = px.line(df_orca_daily, x='DT', y='ORCA_CLOSE', labels ={'DT':'Date', 'ORCA_CLOSE':'$OP Price'}
                ,color_discrete_sequence=['yellow']
                ,hover_data={'DT':False,'ORCA_CLOSE':True})
chart_update_layout(fig_hist_prc, "", "ORCA Token Price (USD)")


#--> daily transaction by pool
fig_trx_pool = px.bar(df_orca_daily,x='DT',y='NUM_TRX',color='POOL NAME'
                           , hover_data={'DT': False, 'NUM_TRX': True}
                           ).update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20), yaxis=dict(title='Number of Transactions'))

# Total Swap volume by pool
fig_swap_vol_pool = px.bar(df_orca_daily,x='DT',y='TTL_SWAP_VOLUME',color='POOL NAME'
                           , hover_data={'DT': False, 'TTL_SWAP_VOLUME': True}
                           ).update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20), yaxis=dict(title='Total Trading Volume (USD)'))
# --> (bonk)
fig_swap_vol_pool_bonk = px.bar(df_orca_bonk,x='DT',y='TTL_SWAP_VOLUME',color='POOL BONK?'
                           , hover_data={'DT': False, 'TTL_SWAP_VOLUME': True}
                           ).update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20), yaxis=dict(title='Total Trading Volume (USD)'))




# Total Fee by pool
fig_swap_fee_pool = px.bar(df_orca_daily,x='DT',y='TTL_LP_FEE',color='POOL NAME'
                           , hover_data={'DT': False, 'TTL_LP_FEE': True}
                           ).update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20), yaxis=dict(title='Total Fee Earned by LP (USD)'))

fig_swap_fee_pool_bonk = px.bar(df_orca_bonk,x='DT',y='TTL_LP_FEE',color='POOL BONK?'
                           , hover_data={'DT': False, 'TTL_LP_FEE': True}
                           ).update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20), yaxis=dict(title='Total Fee Earned by LP (USD)'))