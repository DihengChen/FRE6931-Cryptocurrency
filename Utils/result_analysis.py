# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 19:36:18 2018

@author: njucd
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import seaborn as sns
import pandas as pd
import numpy as np
class result_daily():
    def __init__(self,re_turn):
        self.re=re_turn
        self.cum_re=(re_turn+1).cumprod()-1
        self.num_day=len(re_turn)
        self.drawdown=self.cum_re-np.maximum.accumulate(self.cum_re)
        
    def get_metrics(self):
        self.annual_re=self.cum_re[-1]/self.num_day*252
        self.annual_std=np.std(self.re)*np.sqrt(252)
        self.annual_sp=np.mean(self.re)/np.std(self.re)*np.sqrt(252)   
        self.max_drawdown=np.max(self.drawdown)
        
    def figure_plot(self):
        ax1=plt.subplot(311)
        cum_re_P=self.cum_re*100
        cum_re_P.plot(ax=ax1)
        ax1.set(xlabel='',ylabel='Cumulative Retuen',xticks=[])
        fmt='%.f%%'
        ax1.yaxis.set_major_formatter(FormatStrFormatter(fmt))
        
        ax2=plt.subplot(312)
        self.re.plot(ax=ax2)
        ax2.set(xlabel='',ylabel='Daily Return',xticks=[])
        
        ax3=plt.subplot(313)
        self.drawdown.plot(ax=ax3)
        ax3.set(xlabel='',ylabel='Drawdown')

        plt.show()