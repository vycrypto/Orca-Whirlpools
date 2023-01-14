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
        
        This dashboard analyses the growth of Orca Whirlpools on Solana. 
        Launched in March 2022, Orca whirlpools utilizes concentrated liquidity, allowing LPs to concentrate their liquidity 
        in specific price ranges. Such innovation not only encourages a more efficient use of capital, 
        but also reduces slippage costs for traders.
        
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
    Since launch in March 2022, the SOL-USDC whirlpool has ranked high 
    regardless by trading volume, fees generated for liquidity providers, or daily number of 
    transactions. As a result, the SOL-USDC pool had always been a favorite among liquidity 
    providers in 2022. 
    """
)

#n1, n2 = st.columns((1, 1))

st.markdown(f'#### Daily Number of Transactions per Whirlpool [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True)
st.write(
    '*Number of unique transactions interacting with each Orca Whirlpool each day.*')
st.plotly_chart(f.fig_trx_pool, use_container_width=True)

st.markdown(f'#### Active Liquidity Providers per Whirlpool [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/d8efa2d6-ba9c-4610-ae0b-bf2bcbe80b7c)', unsafe_allow_html=True)
st.write(
    """*Number of unique liquidity providers who increased or decreased liquidity from each Orca Whirlpool each day.*""")
st.plotly_chart(f.fig_lp_num_pool, use_container_width=True)


st.markdown(f'#### Total Trading Volume (USD) [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True)
st.write(
    """*Total volume for swaps for each pool per day.* """)
st.plotly_chart(f.fig_swap_vol_pool, use_container_width=True)


st.markdown(f'#### Daily Fee Earned by Liquidity Providers (USD) [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True)
st.write(
    """*Total fees earned by liquidity providers for each pool per day. Only 97% of the fees counted as 
    3% goes to the Foundation.* """)
st.plotly_chart(f.fig_swap_fee_pool, use_container_width=True)


st.markdown(
    """
    ---
    # Impact of $BONK on Orca Whirlpools
    On January 3rd 2023, $BONK was launched, which changed the landscapes on Orca whirlpools.
    """
)

st.markdown(f'#### Total Trading Volume (USD) [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True)
st.write(
    """*Total volume for swaps for each pool per day.*  """)
st.plotly_chart(f.fig_swap_vol_pool_bonk, use_container_width=True)

st.markdown(f'#### Daily Active Liquidity Providers (USD) [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True)
st.write(
    """*Number of unique liquidity providers who increased or decreased liquidity from each Orca Whirlpool each day.*""")
st.plotly_chart(f.fig_lp_pool_bonk, use_container_width=True)

st.markdown(f'#### Total Fees Earned by Liquidity Providers (USD) [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True)
st.write(
    """ *Total fees earned by liquidity providers for each pool per day. Only 97% of the fees counted as 
    3% goes to the Foundation.*""")
st.plotly_chart(f.fig_swap_fee_pool_bonk, use_container_width=True)




st.markdown(
    """
    ---
    # Capital Efficiency: Orca vs. Uniswap
    
    With concentrated liquidity, liquidity providers on Orca Whirlpools rebalance their positions much more frequently 
    compared to liquidity providers on Uniswap. 



    """
)


st.markdown(
    f'#### Daily LP Position Adjustment on Orca [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/2ec0ad61-7b05-4a13-82a0-423d39dc0e6f)', unsafe_allow_html=True
)
st.write("""*The average daily number of price range adjustments a liquidity provider performs. Estimated by 
counting the pairs of decreasing liquidity transaction with increasing liquidity transaction in the same whirlpool each day.*""")
st.plotly_chart(f.fig_lp_adj_orca, use_container_width=True)

st.markdown(
    f'####  Daily LP Position Adjustment on Uniswap [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/65d08749-498e-4406-aa54-62ab91b210b5)', unsafe_allow_html=True
)
st.write("""*The average daily number of price range adjustments a liquidity provider performs. Estimated by 
counting the pairs of decreasing liquidity transaction with increasing liquidity transaction in the same whirlpool each day.*""")
st.plotly_chart(f.fig_lp_adj_uni, use_container_width=True)


st.markdown(
    """
    ---
    # Methodology 
    
    Data is drawn from [Flipside Crypto](https://flipsidecrypto.xyz/)'s Solana tables. 
    
    """
    f'For Flipside data, links to the underlying queries are provided in the wrench icon ({icons.setting_icon})'
   
    """
    next to chart and table tiles.
    
    For page source, see [Github](https://github.com/pd123459/Orca-Whirlpools).
    
    ---
    # About

    This dashboard is designed by [@Phi_Deltalytics](https://twitter.com/phi_deltalytics). 
    I hope it serves as a valuable tool for both newcomers and experienced users 
    to gain insights into the Orca Whirlpools. 
    
    
    Any comments and suggestions are welcomed. 
    """
    , unsafe_allow_html=True

    )










