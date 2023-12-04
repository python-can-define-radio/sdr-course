"""                                                                           
Added Commandline functionality for displaying signal data in the terminal usi
the dashing module built on blessed.                                          
See URL for more information on dashing: https://github.com/FedericoCeratto/da
"""                                                                           
                                                                              
from __future__ import annotations                                            
from gnuradio import gr                                                       
from gnuradio import blocks                                                   
from pcdr import configure_graceful_exit                                      
import time                                                                   
import numpy as np                                                            
from dashing import *                                                         
                                                                              
                                                                              
class dashing_display(gr.sync_block):                                         
                                                                              
    def __init__(self, sleep_seconds=1.0/90):                                 
        gr.sync_block.__init__(                                               
            self,                                                             
            name="Print block",                                               
            in_sig=[np.complex64],                                            
            out_sig=[]                                                        
        )                                                                     
        self.ui = HChart(title="Some Horizontal Chart", color=7, border_color=
        self.sleep_seconds = sleep_seconds                                    
                                                                              
    def work(self, input_items, output_items):                                
        singleDataPoint = input_items[0][0]                                   
        self.ui.append(singleDataPoint)                                       
        self.ui.display()                                                     
        time.sleep(self.sleep_seconds)                                        
        return 1                                                              
                                                                              
class Random_Signal_Generator(gr.top_block):                                  
    def __init__(self):                                                       
        gr.top_block.__init__(self, "Top block")                              
        d = np.array([2, 10, 50], dtype=np.complex64)                         
        self.myFirstBlock = blocks.vector_source_c(d, repeat=True)            
        self.dashing_display = dashing_display()                              
        self.connect(self.myFirstBlock, self.dashing_display)                 
                                                                              
tb = Random_Signal_Generator()                                                
configure_graceful_exit(tb)                                                   
tb.start()                                                                    
while True:                                                                   
    time.sleep(0.25)                                                          
                                                                              
