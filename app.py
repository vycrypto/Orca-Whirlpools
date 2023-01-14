import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import time
import plotly.express as px
import plotly.graph_objects as go
import figures as f
import icons as icons

st.set_page_config(page_title='ORCA Pools',  layout='wide', page_icon='images/logo.png')

proj_title = '<p style="font-family:sans-serif; color:white; font-size: 50px;"><b>Rise of ORCA Whirlpools</b></p>'
gap = '<span>&nbsp;&nbsp;</span>'

t1, t2 = st.columns((1,5))
t1.image('images/logo.png', width = 120)
t2.markdown(proj_title, unsafe_allow_html=True)
t2.markdown(f'[{icons.link_icon}](https://www.orca.so/){gap}'
            f'{gap}[{icons.twitter_icon}](https://twitter.com/orca_so){gap}'
            f'{gap}[{icons.discord_icon}](https://discord.com/invite/rdrW577act){gap}'
            f'{gap}[{icons.medium_icon}](https://medium.com/orca-so){gap}'
            f'{gap}[{icons.github_icon}](https://github.com/orca-so)', unsafe_allow_html=True)

#=========================== OVERVIEW ==============================
st.markdown(
    """
        # Overview 
        
        This dashboard offers a holistic view of the Optimism ecosystem including 
        transactions, user activities, staking, and developments. Introduced in 
        June 2019, Optimism is a Layer 2 Optimistic Rollup network designed to utilize 
        the strong security guarantees of Ethereum while reducing 
        its cost and latency.
        https://medium.com/orca-so/introducing-whirlpools-concentrated-liquidity-on-orca-3987c131a44d
        - concentrated liquidity 
        
        1. Key finding 1
        2. Key finding 2
        3. Key finding 3
        
""")
st.markdown(
    f'####  ORCA Token Price[{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True
)
st.write("""*The price of the $ORCA token. Currency in USD.*""")
st.plotly_chart(f.fig_hist_prc, use_container_width=True)


st.markdown(
    """
    ---
    # Growth Over Time
    A holistic view of the growth of Orca Whirlpools over time. 
    
    """
)

#n1, n2 = st.columns((1, 1))

st.markdown(f'#### Daily Number of Transactions per Whirlpool [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True)
st.write(
    '')
st.plotly_chart(f.fig_trx_pool, use_container_width=True)

st.markdown(f'#### Active Liquidity Providers per Whirlpool [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/d8efa2d6-ba9c-4610-ae0b-bf2bcbe80b7c)', unsafe_allow_html=True)
st.write(
    """ """)
st.plotly_chart(f.fig_lp_num_pool, use_container_width=True)


st.markdown(f'#### Total Trading Volume (USD) [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True)
st.write(
    """ """)
st.plotly_chart(f.fig_swap_vol_pool, use_container_width=True)


st.markdown(f'#### Daily Fee Earned by Liquidity Providers (USD) [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True)
st.write(
    """ """)
st.plotly_chart(f.fig_swap_fee_pool, use_container_width=True)





st.markdown(
    """
    As of January 11th, 2023, ... 

    """
)

st.markdown(
    """
    ---
    # Impact of $BONK on Orca Whirlpools
    On January 3rd 2023, a token 
    
    

    """
)

st.markdown(f'#### Total Volume (USD) [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True)
st.write(
    """ """)
st.plotly_chart(f.fig_swap_vol_pool_bonk, use_container_width=True)

st.markdown(f'#### Total Volume (USD) [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True)
st.write(
    """ """)
st.plotly_chart(f.fig_lp_pool_bonk, use_container_width=True)

st.markdown(f'#### Total Volume (USD) [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True)
st.write(
    """ """)
st.plotly_chart(f.fig_swap_fee_pool_bonk, use_container_width=True)




st.markdown(
    """
    ---
    # Capital Efficiency: Orca vs. Uniswap
    
    On January 3rd 2023, a token 



    """
)


st.markdown(
    f'####  [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/d8efa2d6-ba9c-4610-ae0b-bf2bcbe80b7c)', unsafe_allow_html=True
)
st.write("""*The monthly inflow volume of assets bridged from Ehereum to Optimism.*""")
st.plotly_chart(f.fig_lp_num_pool, use_container_width=True)

st.markdown(
    f'#### Daily LP Position Adjustment on Orca [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/2ec0ad61-7b05-4a13-82a0-423d39dc0e6f)', unsafe_allow_html=True
)
st.write("""*The monthly inflow volume of assets bridged from Ehereum to Optimism.*""")
st.plotly_chart(f.fig_lp_adj_orca, use_container_width=True)

st.markdown(
    f'####  Daily LP Position Adjustment on Uniswap [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/65d08749-498e-4406-aa54-62ab91b210b5)', unsafe_allow_html=True
)
st.write("""*The monthly inflow volume of assets bridged from Ehereum to Optimism.*""")
st.plotly_chart(f.fig_lp_adj_uni, use_container_width=True)



st.markdown(
    f'#### Title [{icons.setting_icon}](https://twitter.com/phi_deltalytics)', unsafe_allow_html=True
)

st.markdown(
    """
    ---
    # Methodology 
    
    Data is drawn from [Flipside Crypto](https://flipsidecrypto.xyz/)'s Solana tables. 
    
    """
    f'For Flipside data, links to the underlying queries are provided in the wrench icon ({icons.setting_icon})'
   
    """
    next to chart and table tiles.
    
    For page source, see [Github](https://github.com/pd123459/OptimismDashboard).
    
    ---
    # About

    This dashboard is designed by [@Phi_Deltalytics](https://twitter.com/phi_deltalytics)
     for MetricsDao's 
    Optimism Mega Dashboard bounty. I hope it serves as a valuable tool for 
    both newcomers and experienced users to gain insights into the Optimism ecosystem. 
    
    
    Any comments and suggestions are welcomed. 
    """
    , unsafe_allow_html=True

    )










