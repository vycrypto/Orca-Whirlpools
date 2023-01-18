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
        
        #### **Key takeaways:**
        
        1. The SOL-USDC pool has generated the most fees for liquidity providers in 2022
        
        2. $BONK pools generated the most trading volume and fees in 2023 
        
        3. Liquidity providers adjust their positions much more frequently on Orca compared to Uniswap, contributing to better capital efficiency in Orca whirlpools
        
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
    """
)


st.markdown(f'#### Daily Active Whirlpools [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True)
st.write(
    """*The number of Orca Whirlpools that have active transactions per day.* """)
st.plotly_chart(f.fig_pool_count, use_container_width=True)

st.markdown(
    """
    
    From March 2022 to January 2023, the number of daily active Orca whirlpools has increased from 
    single digit to over 100 with more than 400 whirlpools in total. Furthermore, the daily trading 
    volume in January surged to the 5-10 million USD range with the maximum daily trading volume 
    surpassing 15 million USD. The rise in 2023 usage and adoption was impacted by a newly launched token $BONK
    which we will dive into in the section below. This section focuses on the growth of Orca 
    whirlpools in 2022.
    
    The most popular whirlpool in 2022 is the SOL-USDC pool, often contributing more than 50% of the total 
    whirlpool trading volume and fees earned by liquidity providers on a daily basis. As a result, it 
    also has the highest number of active liquidity providers on most days throughout 2022. While most 
    volume concentrates in the SOL-USDC pool, the distribution of active liquidity providers is more 
    decentralized. For example, while the SOL-USDC pool contributed to 73.2% of total whirlpool trading volume
    on April 12th, 2022, only 44.4% of active liquidity providers were interacting with the SOL-USDC pool. 
    Such difference in distribution potentially indicates the liquidity providers for Orca whirlpools have 
    motivations beyond earning trading fees. 
    
    mSOL(*a liquid staking token that you receive when you stake SOL on the Marinade protocol*) and 
    stSOL(*a token that represents staking positions with a diverse set of professional validators on Solana*) 
    whirlpools have also been popular in 2022. 
    
    *Note: pie charts below are zoomed in views of the data on the following four selected dates - 4/12/22
    , 7/18/22, 11/18/22, 1/5/23.*
    """
)

st.markdown(f'#### Total Trading Volume (USD) [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True)
st.write(
    """*Total trading volume for each pool per day.* """)
st.plotly_chart(f.fig_swap_vol_pool, use_container_width=True)
n1, n2= st.columns((1,1))
n1.plotly_chart(f.fig_pie_apr, use_container_width=True)
n2.plotly_chart(f.fig_pie_jul, use_container_width=True)
n1.plotly_chart(f.fig_pie_nov, use_container_width=True)
n2.plotly_chart(f.fig_pie_jan, use_container_width=True)


st.markdown(f'#### Daily Fee Earned by Liquidity Providers (USD) [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True)
st.write(
    """*Total fees earned by liquidity providers for each pool per day. Only 97% of the fees counted as 
    3% goes to the Foundation.* """)
st.plotly_chart(f.fig_swap_fee_pool, use_container_width=True)

g1, g2= st.columns((1,1))
g1.plotly_chart(f.fig_pie_fee_apr, use_container_width=True)
g2.plotly_chart(f.fig_pie_fee_jul, use_container_width=True)
g1.plotly_chart(f.fig_pie_fee_nov, use_container_width=True)
g2.plotly_chart(f.fig_pie_fee_jan, use_container_width=True)


st.markdown(f'#### Active Liquidity Providers per Whirlpool [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/d8efa2d6-ba9c-4610-ae0b-bf2bcbe80b7c)', unsafe_allow_html=True)
st.write(
    """*Number of unique liquidity providers who increased or decreased liquidity from each Orca Whirlpool each day.*""")
st.plotly_chart(f.fig_lp_num_pool, use_container_width=True)

m1, m2= st.columns((1,1))
m1.plotly_chart(f.fig_pie_lp_apr, use_container_width=True)
m2.plotly_chart(f.fig_pie_lp_jul, use_container_width=True)
m1.plotly_chart(f.fig_pie_lp_nov, use_container_width=True)
m2.plotly_chart(f.fig_pie_lp_jan, use_container_width=True)





st.markdown(
    """
    ---
    # Impact of $BONK on Orca Whirlpools
    
    While the SOL-USDC pool dominated trading volume in most of 2022, the launch of BONK token changed
    the Orca whirlpools landscape. As the first dog-themed meme coin on Solana, $BONK was up more than 30,000%
    in the first week of January. The launch not only drove the price of SOL from 8 to 22 USD, but also 
    changed the popularity of Orca whirlpools. 
    
    """
)

st.markdown(f'#### Total Trading Volume (USD) [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True)
st.write(
    """*Total volume for swaps for each pool per day.*  """)
st.plotly_chart(f.fig_swap_vol_pool_bonk, use_container_width=True)

st.markdown(f'#### Total Fees Earned by Liquidity Providers (USD) [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True)
st.write(
    """ *Total fees earned by liquidity providers for each pool per day. Only 97% of the fees counted as 
    3% goes to the Foundation.*""")
st.plotly_chart(f.fig_swap_fee_pool_bonk, use_container_width=True)

st.markdown(f'#### Daily Active Liquidity Providers [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/860f8493-6bad-45a6-98b0-d76d587dc1c3)', unsafe_allow_html=True)
st.write("""*Number of unique liquidity providers who increased or decreased liquidity from each Orca Whirlpool each day.*""")
st.plotly_chart(f.fig_lp_pool_bonk, use_container_width=True)

st.markdown(
    """
    ---
    # Capital Efficiency: Orca vs. Uniswap
    With concentrated liquidity, liquidity providers on Orca Whirlpools rebalance their positions much more frequently 
    compared to liquidity providers on Uniswap. While an average Uniswap liquidity provider adjusts his/her 
    positions 3-4 times a week, an average Orca liquidity provider adjusts his/her positions everyday. 
    """
)


st.markdown(
    f'#### Daily LP Position Adjustment on Orca [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/2ec0ad61-7b05-4a13-82a0-423d39dc0e6f)', unsafe_allow_html=True
)
st.write("""*The average daily number of price range adjustments a liquidity provider performs. Estimated by 
counting the pairs of decreasing liquidity transaction with increasing liquidity transaction in the same whirlpool by each liquidity provider per day.*""")
st.plotly_chart(f.fig_lp_adj_orca, use_container_width=True)

st.markdown(
    f'####  Daily LP Position Adjustment on Uniswap [{icons.setting_icon}](https://app.flipsidecrypto.com/velocity/queries/65d08749-498e-4406-aa54-62ab91b210b5)', unsafe_allow_html=True
)
st.write("""*The average daily number of price range adjustments a liquidity provider performs. Estimated by 
counting the pairs of decreasing liquidity transaction with increasing liquidity transaction in the same whirlpool by each liquidity provider per day.*""")
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










