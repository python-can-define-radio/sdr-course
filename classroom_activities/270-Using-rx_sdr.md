Write to a file:  
`rx_sdr -f 101e6 -s 2e6 myrecording.iqdata`

Write to stdout, with a hexdump so it doesn't spew weird symbols (can mess up terminal since some are non-printable)  
Remember, Ctrl+C to quit.  
`rx_sdr -f 101e6 -s 2e6 - | hexdump`

Same as previous, but with head so you just see the first 5 lines:  
`rx_sdr -f 101e6 -s 2e6 - | hexdump | head -n 5`

Write the hexdump to a file (Easier to look at than raw data, but not useful for analysis and such):  
`rx_sdr -f 101e6 -s 2e6 - | hexdump > myrecording.iqdata`
