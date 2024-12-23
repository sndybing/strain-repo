#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 03:25:48 2020

@author: sydneydybing
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

RC_path_to_files = '/Users/sydneydybing/StrainProject/Ridgecrest/StrainData/Processed/RMS/Trimmed/PST/'
RC_quake_folders = ['1', '2', '3', '4', '5', '6']
RC_stas = ['B916', 'B917', 'B921']
RC_dist = pd.read_csv('/Users/sydneydybing/StrainProject/Ridgecrest/evt-sta_dist.csv')

RC_dist = RC_dist.to_numpy()

# file = path_to_files + '1/MCMC_xinter/B916_xinter2.npz'
# xinter_1_916 = np.load(file) 

# print(xinter_1_916['xinter'])

RC_tau_list = []
RC_mag_list = []

for RC_quake in RC_quake_folders:
    
    for RC_sta in RC_stas:
        
        RC_file = RC_path_to_files + RC_quake + '/MCMC_xinter/' + RC_sta + '_xinter.npz'
        RC_xinter = np.load(RC_file)
        RC_xinter_array = RC_xinter['xinter']
        
        print('Quake: ' + RC_quake)
        print('Station: ' + RC_sta)
        print(RC_xinter_array)
        
        if (RC_quake == '1') or (RC_quake == '2') or (RC_quake == '5') or (RC_quake == '6'):
            start = 10
        elif RC_quake == '3':
            start = 10.2
        else:
            start = 10.1
        
        RC_mean_xinter = np.mean(RC_xinter_array)
        
        print('xinter mean: ' + str(RC_mean_xinter))
        
        RC_tau = RC_mean_xinter - start
        
        print('tau: ' + str(RC_tau))
        
        RC_tau_list.append(RC_tau)
        
        print(RC_tau_list)
        
        if (RC_quake == '1'):
            mag = 6.4
        elif (RC_quake == '2'):
            mag = 5.36
        elif (RC_quake == '3'):
            mag = 7.1
        elif (RC_quake == '4'):
            mag = 5.5
        elif RC_quake == '5':
            mag = 5.44
        else:
            mag = 5.53
        
        print('mag: ' + str(mag))
        RC_mag_list.append(mag)
        
        print('-------')

RC_tau_plot = pd.read_csv('/Users/sydneydybing/StrainProject/Ridgecrest/tau_plot.csv', encoding="utf-8-sig")

RC_tau_array = np.asarray(RC_tau_list)
RC_mag_array = np.asarray(RC_mag_list)
RC_dist = RC_tau_plot.dist.values

print(RC_tau_array.shape)
print(RC_dist.shape)

Tai_path_to_files = '/Users/sydneydybing/StrainProject/Taiwan/Trimmed/Aligned/PST/MCMC_xinter/'
Tai_dist = pd.read_csv('/Users/sydneydybing/StrainProject/Taiwan/evt-sta_dist.csv')

Tai_dist = Tai_dist.to_numpy()

# file = path_to_files + '1/MCMC_xinter/B916_xinter2.npz'
# xinter_1_916 = np.load(file) 

# print(xinter_1_916['xinter'])

Tai_tau_list = []
Tai_mag_list = []

Tai_stas_chans = ['CHMB.EV', 'DONB.EV', 'FBRB.EV', 'HGSB.EV', 'SJNB.EV', 'SSTB.EV', 'ZANB.EV', 'SSNB.EV', 'SSNB.G1', 'SSNB.G2', 'TRKB.EV', 'TRKB.G1', 'TRKB.G2']
    
for Tai_sta_chan in Tai_stas_chans:
    
    Tai_file = Tai_path_to_files + Tai_sta_chan+ '_xinter.npz'
    Tai_xinter = np.load(Tai_file)
    Tai_xinter_array = Tai_xinter['xinter']
    
    print('Station: ' + Tai_sta_chan)
    print(Tai_xinter_array)
    
    start = 9.9
    
    Tai_mean_xinter = np.mean(Tai_xinter_array)
    
    print('xinter mean: ' + str(Tai_mean_xinter))
    
    Tai_tau = Tai_mean_xinter - start
    
    print('tau: ' + str(Tai_tau))
    
    Tai_tau_list.append(Tai_tau)
    
    print(Tai_tau_list)
    
    Tai_mag = 6.2
    
    Tai_mag_list.append(Tai_mag)
      
    print('-------')

Tai_distances = pd.read_csv('/Users/sydneydybing/StrainProject/Taiwan/evt-sta_dist.csv')

Tai_tau_array = np.asarray(Tai_tau_list)
Tai_mag_array = np.asarray(Tai_mag_list)
Tai_dist = Tai_distances.dist_km.values

print(Tai_tau_array.shape)
print(Tai_dist.shape)

B_path_to_files = '/Users/sydneydybing/StrainProject/M6_500km_sel/StrainData_sel/Trimmed/PeakStrains/'
B_quake_folders = np.genfromtxt('/Users/sydneydybing/StrainProject/M6_500km_sel/quake_folders_sel.txt', dtype=str)
B_stas = np.genfromtxt('/Users/sydneydybing/StrainProject/stations.txt', dtype=str)
B_dist = pd.read_csv('/Users/sydneydybing/StrainProject/Barbour_sel_dists.csv')

B_dist = B_dist.to_numpy()

# file = path_to_files + '1/MCMC_xinter/B916_xinter2.npz'
# xinter_1_916 = np.load(file) 

# print(xinter_1_916['xinter'])

B_tau_list = []
B_mag_list = []

for B_quake in B_quake_folders:
    
    for B_sta in B_stas:
        
        try:
        
            B_file = B_path_to_files + B_quake + '/MCMC_xinter/' + B_sta + '_xinter.npz'
            B_xinter = np.load(B_file)
            B_xinter_array = B_xinter['xinter']
            
            print('-------')
            print('Quake: ' + B_quake)
            print('Station: ' + B_sta)
            # print(B_xinter_array)
            
            if (B_quake == '59_2008_6.3'):
                start = 0
                
            elif (B_quake == '109_2010_6.5'):
                if (B_sta == 'B933') or (B_sta == 'B934') or (B_sta == 'B935') or (B_sta == 'B035') or (B_sta == 'B036'):
                    start = 10.1
                else:
                    start = 10
                
            elif (B_quake == '112_2010_7.2'):
                if (B_sta == 'B916') or (B_sta == 'B917') or (B_sta == 'B918') or (B_sta == 'B921'):
                    start = 9.8
                else:
                    start = 10.1
                    
            else:
                start = 10
            
            B_mean_xinter = np.mean(B_xinter_array)
            
            # print('xinter mean: ' + str(B_mean_xinter))
            
            B_tau = B_mean_xinter - start
            
            print('tau: ' + str(B_tau))
            
            B_tau_list.append(B_tau)
            
            # print(B_tau_list)
            
            if (B_quake == '59_2008_6.3'):
                mag = 6.3
                
            elif (B_quake == '109_2010_6.5'):
                mag = 6.5
                
            elif (B_quake == '112_2010_7.2'):
                mag = 7.2
                
            elif (B_quake == '152_2012_6.0'):
                mag = 6.0
                
            elif (B_quake == '172_2012_6.1'):
                mag = 6.1
                
            elif (B_quake == '185_2014_6.8'):
                mag = 6.8
            
            # print('mag: ' + str(mag))
            B_mag_list.append(mag)
            
            print('-------')

        except:
            pass

B_dist = pd.read_csv('/Users/sydneydybing/StrainProject/Barbour_sel_dists.csv')

B_tau_array = np.asarray(B_tau_list)
B_mag_array = np.asarray(B_mag_list)
B_dist = B_dist.dist_km.values

print(B_tau_array.shape)
print(B_dist.shape)

############### SOURCE DURATION PARTS ##################

apref = -6.407
bpref = 0.385

##### Ridgecrest #####

Rcrest = pd.read_csv('/Users/sydneydybing/StrainProject/Ridgecrest/rcrest_quakes_Mo.csv')

Rcrest_Mo = Rcrest.Mo.values
print(Rcrest_Mo)

Rcrest_S_list = []
Rcrest_S_mags_list = [6.4, 5.36, 7.1, 5.5, 5.44, 5.53]

for Mo in Rcrest_Mo:
    
    logS = apref + bpref * np.log10(Mo)
    #print(logS)
    
    S = 10**logS
    Rcrest_S = S
    
    print(Rcrest_S)
    
    Rcrest_S_list.append(Rcrest_S)

print(Rcrest_S_list)
print('-------------')

##### Barbour #####

Barbour = pd.read_csv('/Users/sydneydybing/StrainProject/Barbour_quakes_Mo.csv')

Barbour_Mo = Barbour.Mo.values
print(Barbour_Mo)

Barbour_S_list = []
Barbour_S_mags_list = [6.3, 6.5, 7.2, 6.4, 6.0, 6.1, 6.8]

for Mo in Barbour_Mo:
    
    logS = apref + bpref * np.log10(Mo)
    #print(logS)
    
    S = 10**logS
    Barbour_S = S
    
    print(Barbour_S)
    
    Barbour_S_list.append(Barbour_S)

print(Barbour_S_list)
    
print('-------------')

##### Taiwan #####

Taiwan_Mo = 2.195*10**18
Taiwan_S_list = []
Taiwan_S_mags_list = [6.2]

Taiwan_logS = apref + bpref * np.log10(Taiwan_Mo)
#print(logS)

Taiwan_S = 10**Taiwan_logS

print(Taiwan_S)
Taiwan_S_list.append(Taiwan_S)

print(Taiwan_S_list)

print('-------------')

Rcrest_S_array = np.asarray(Rcrest_S_list)
Rcrest_S_mags_array = np.asarray(Rcrest_S_mags_list)

Barbour_S_array = np.asarray(Barbour_S_list)
Barbour_S_mags_array = np.asarray(Barbour_S_mags_list)

Taiwan_S_array = np.asarray(Taiwan_S_list)
Taiwan_S_mags_array = np.asarray(Taiwan_S_mags_list)

################# PLOTTING ###################

fig = plt.figure(1, figsize=(8,5),dpi=300)

plt.scatter(B_dist[18:28],B_tau_array[18:28],label='M7.2',color='maroon')
plt.scatter(RC_dist[6:8],RC_tau_array[6:8],label='M7.1',color='brown')
plt.scatter(B_dist[68:83],B_tau_array[68:83],label='M6.8',color='firebrick')
plt.scatter(B_dist[5:17],B_tau_array[5:17],label='M6.5',color='red')
plt.scatter(RC_dist[0:2],RC_tau_array[0:2],label='M6.4',color='tomato')
plt.scatter(B_dist[0:4],B_tau_array[0:4],label='M6.3',color='coral')
plt.scatter(Tai_dist,Tai_tau_array,label='M6.2',color='lightcoral')
plt.scatter(B_dist[48:67],B_tau_array[48:67],label='M6.1',color='darksalmon')
plt.scatter(B_dist[29:47],B_tau_array[29:47],label='M6.0',color='salmon')
plt.scatter(RC_dist[15:17],RC_tau_array[15:17],label='M5.5',color='lightsalmon')
plt.scatter(RC_dist[9:11],RC_tau_array[9:11],label='M5.5',color='sandybrown')
plt.scatter(RC_dist[12:14],RC_tau_array[12:14],label='M5.4',color='peachpuff')
plt.scatter(RC_dist[3:5],RC_tau_array[3:5],label='M5.4',color='mistyrose')
plt.xlabel('Hypocentral Distance (km)', fontsize = 13)
plt.ylabel('Tau (s)', fontsize = 13)
plt.legend(loc='upper left', ncol=2, fontsize = 12)
plt.title('Tau-Distance Plot (All Earthquakes)', fontsize = 15)

# plt.show()
plt.savefig('/Users/sydneydybing/Documents/Comps/Figures/fulltauplot.jpg', format='JPEG')

plt.close()

# fig = plt.figure(1, figsize=(8,5),dpi=300)

# plt.scatter(B_mag_array[18:28],B_tau_array[18:28],label='M7.2',color='maroon')
# plt.scatter(RC_mag_array[6:8],RC_tau_array[6:8],label='M7.1',color='brown')
# plt.scatter(B_mag_array[68:83],B_tau_array[68:83],label='M6.8',color='firebrick')
# plt.scatter(B_mag_array[5:17],B_tau_array[5:17],label='M6.5',color='red')
# plt.scatter(RC_mag_array[0:2],RC_tau_array[0:2],label='M6.4',color='tomato')
# # plt.scatter(B_mag_array[0:4],B_tau_array[0:4],label='M6.3',color='coral')
# plt.scatter(Tai_mag_array,Tai_tau_array,label='M6.2',color='lightcoral')
# plt.scatter(B_mag_array[48:67],B_tau_array[48:67],label='M6.1',color='darksalmon')
# plt.scatter(B_mag_array[29:47],B_tau_array[29:47],label='M6.0',color='salmon')
# plt.scatter(RC_mag_array[15:17],RC_tau_array[15:17],label='M5.5',color='lightsalmon')
# plt.scatter(RC_mag_array[9:11],RC_tau_array[9:11],label='M5.5',color='sandybrown')
# plt.scatter(RC_mag_array[12:14],RC_tau_array[12:14],label='M5.4',color='peachpuff')
# plt.scatter(RC_mag_array[3:5],RC_tau_array[3:5],label='M5.4',color='mistyrose')
# # plt.scatter(Rcrest_S_mags_array,Rcrest_S_array,color='black',marker='x',label='Estimated\nsource\nduration')
# # plt.scatter(Barbour_S_mags_array,Barbour_S_array,color='black',marker='x')
# # plt.scatter(Taiwan_S_mags_array,Taiwan_S_array,color='black',marker='x')

# plt.xlabel('Earthquake Magnitude', fontsize = 13)
# plt.ylabel('Tau (s)', fontsize = 13)
# plt.legend(loc=2, ncol=1, fontsize=12)
# plt.title('Tau-Magnitude Plot (All Earthquakes)', fontsize = 15)

# # plt.show()
# plt.savefig('/Users/sydneydybing/Documents/Comps/Figures/fulltau_vs_mag_plot_nooutlier.jpg', format='JPEG')

# plt.close()




