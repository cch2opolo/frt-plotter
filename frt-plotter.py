import matplotlib.pyplot as plt
import numpy as np
min_psi = 500
max_psi = 600

# 5-1/8" FRT-HF
constant5 = 0.064885
flow_power5 = 1.5181
avg_area_power5 = -1.5421
ratio_power5 = 0.2774

# 1.15
avg_area_1_15 = 0.805963837
avg_ratio_1_15 = 1.348147737
# 1.2
avg_area_1_2 = 0.85
avg_ratio_1_2 = 1.339821637
# 1.3
avg_area_1_3 = 0.93
avg_ratio_1_3 = 1.310775046
# 1.4
avg_area_1_4 = 0.995928802
avg_ratio_1_4 = 1.263153376
# 1.5
avg_area_1_5 = 1.050176259
avg_ratio_1_5 = 1.181142461
# 1.6
avg_area_1_6 = 1.088890865
avg_ratio_1_6 = 1.107696826

x = np.arange(8.0, 16.0, 0.5)
y1_min5 = ((min_psi * 8.3)/(constant5 * avg_area_1_15**avg_area_power5
           * avg_ratio_1_15**ratio_power5 * x))**(1 / flow_power5)
y1_max5 = ((max_psi * 8.3)/(constant5 * avg_area_1_15**avg_area_power5 *
           avg_ratio_1_15**ratio_power5 * x))**(1 / flow_power5)
y2_min5 = ((min_psi * 8.3)/(constant5 * avg_area_1_2**avg_area_power5 *
           avg_ratio_1_2**ratio_power5 * x))**(1 / flow_power5)
y2_max5 = ((max_psi * 8.3)/(constant5 * avg_area_1_2**avg_area_power5 *
           avg_ratio_1_2**ratio_power5 * x))**(1 / flow_power5)
y3_min5 = ((min_psi * 8.3)/(constant5 * avg_area_1_3**avg_area_power5 *
           avg_ratio_1_3**ratio_power5 * x))**(1 / flow_power5)
y3_max5 = ((max_psi * 8.3)/(constant5 * avg_area_1_3**avg_area_power5 *
           avg_ratio_1_3**ratio_power5 * x))**(1 / flow_power5)
y4_min5 = ((min_psi * 8.3)/(constant5 * avg_area_1_4**avg_area_power5 *
           avg_ratio_1_4**ratio_power5 * x))**(1 / flow_power5)
y4_max5 = ((max_psi * 8.3)/(constant5 * avg_area_1_4**avg_area_power5 *
           avg_ratio_1_4**ratio_power5 * x))**(1 / flow_power5)
y5_min5 = ((min_psi * 8.3)/(constant5 * avg_area_1_5**avg_area_power5 *
           avg_ratio_1_5**ratio_power5 * x))**(1 / flow_power5)
y5_max5 = ((max_psi * 8.3)/(constant5 * avg_area_1_5**avg_area_power5 *
           avg_ratio_1_5**ratio_power5 * x))**(1 / flow_power5)
y6_min5 = ((min_psi * 8.3)/(constant5 * avg_area_1_6**avg_area_power5 *
           avg_ratio_1_6**ratio_power5 * x))**(1 / flow_power5)
y6_max5 = ((max_psi * 8.3)/(constant5 * avg_area_1_6**avg_area_power5 *
           avg_ratio_1_6**ratio_power5 * x))**(1 / flow_power5)

# 7-1/8" FRT
constant7 = 0.088186
flow_power7 = 1.46363280992427
avg_area_power7 = -2.08597187930271
ratio_power7 = 1.86403044591205

# 1.85
avg_area_1_85 = 1.924749851
avg_ratio_1_85 = 1.65
# 1.9
avg_area_1_9 = 1.979229122
avg_ratio_1_9 = 1.59
# 1.95
avg_area_1_95 = 2.030403397
avg_ratio_1_95 = 1.54
# 2.0
avg_area_2_0 = 2.078668423
avg_ratio_2_0 = 1.49
# 2.05
avg_area_2_05 = 2.124257189
avg_ratio_2_05 = 1.45
# 2.1
avg_area_2_1 = 2.167294954
avg_ratio_2_1 = 1.40
# 2.2
avg_area_2_2 = 2.246086745
avg_ratio_2_2 = 1.324659713


x = np.arange(8.0, 16.0, 0.5)
y1_min7 = ((min_psi * 8.3)/(constant7 * avg_area_1_85**avg_area_power7
           * avg_ratio_1_85**ratio_power7 * x))**(1 / flow_power7)
y1_max7 = ((max_psi * 8.3)/(constant7 * avg_area_1_85**avg_area_power7
           * avg_ratio_1_85**ratio_power7 * x))**(1 / flow_power7)
y2_min7 = ((min_psi * 8.3)/(constant7 * avg_area_1_9**avg_area_power7
           * avg_ratio_1_9**ratio_power7 * x))**(1 / flow_power7)
y2_max7 = ((max_psi * 8.3)/(constant7 * avg_area_1_9**avg_area_power7
           * avg_ratio_1_9**ratio_power7 * x))**(1 / flow_power7)
y3_min7 = ((min_psi * 8.3)/(constant7 * avg_area_1_95**avg_area_power7
           * avg_ratio_1_95**ratio_power7 * x))**(1 / flow_power7)
y3_max7 = ((max_psi * 8.3)/(constant7 * avg_area_1_95**avg_area_power7
           * avg_ratio_1_95**ratio_power7 * x))**(1 / flow_power7)
y4_min7 = ((min_psi * 8.3)/(constant7 * avg_area_2_0**avg_area_power7
           * avg_ratio_2_0**ratio_power7 * x))**(1 / flow_power7)
y4_max7 = ((max_psi * 8.3)/(constant7 * avg_area_2_0**avg_area_power7
           * avg_ratio_2_0**ratio_power7 * x))**(1 / flow_power7)
y5_min7 = ((min_psi * 8.3)/(constant7 * avg_area_2_05**avg_area_power7
           * avg_ratio_2_05**ratio_power7 * x))**(1 / flow_power7)
y5_max7 = ((max_psi * 8.3)/(constant7 * avg_area_2_05**avg_area_power7
           * avg_ratio_2_05**ratio_power7 * x))**(1 / flow_power7)
y6_min7 = ((min_psi * 8.3)/(constant7 * avg_area_2_1**avg_area_power7
           * avg_ratio_2_1**ratio_power7 * x))**(1 / flow_power7)
y6_max7 = ((max_psi * 8.3)/(constant7 * avg_area_2_1**avg_area_power7
           * avg_ratio_2_1**ratio_power7 * x))**(1 / flow_power7)
y7_min7 = ((min_psi * 8.3)/(constant7 * avg_area_2_2**avg_area_power7
           * avg_ratio_2_2**ratio_power7 * x))**(1 / flow_power7)
y7_max7 = ((max_psi * 8.3)/(constant7 * avg_area_2_2**avg_area_power7
           * avg_ratio_2_2**ratio_power7 * x))**(1 / flow_power7)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 8.5))

ax1.fill_between(x, y1_min5, y1_max5, alpha=0.4)
ax1.fill_between(x, y2_min5, y2_max5, alpha=0.4)
ax1.fill_between(x, y3_min5, y3_max5, alpha=0.4)
ax1.fill_between(x, y4_min5, y4_max5, alpha=0.4)
ax1.set_title('5-1/8" FRT-HF Interal Plate Chart',
              fontsize='16', pad='50', ha='center')
plt.figtext(0.28, 0.915, '1.20" Rotating Valve',
            fontsize='14', ha='center')
plt.figtext(0.28, 0.885, '500 psi - 600 psi Pressure Drop',
            fontsize='14', ha='center')
ax1.legend(['1.15', '1.20', '1.30', '1.40'])
ax1.set_xlabel('Mud Weight', fontsize='14', labelpad=10)
ax1.set_ylabel('Flow Rate', fontsize='14', labelpad=10)
ax1.set_ylim(200, 400)
ax1.grid()


ax2.plot(x, y5_min5, '#900', label='1.85 Min')
fig.text(0.588, 0.31, '1.85\nMin', fontsize='8', color='white',
         backgroundcolor='#900', multialignment='center')
ax2.plot(x, y5_max5, '#900', label='1.85 Max')
fig.text(0.588, 0.422, '1.85\nMax', fontsize='8', color='white',
         backgroundcolor='#900', multialignment='center')
ax2.plot(x, y6_min5, '#990', label='1.90 Min')
fig.text(0.588, 0.38, '1.90\nMin', fontsize='8', color='white',
         backgroundcolor='#990', multialignment='center')
ax2.plot(x, y6_max5, '#990', label='1.90 Max')
fig.text(0.588, 0.51, '1.90\nMax', fontsize='8', color='white',
         backgroundcolor='#990', multialignment='center')
ax2.plot(x, y7_min5, '#090', label='1.95 Min')
fig.text(0.588, 0.465, '1.95\nMin', fontsize='8', color='white',
         backgroundcolor='#090', multialignment='center')
ax2.plot(x, y7_max5, '#090', label='1.95 Max')
fig.text(0.588, 0.605, '1.95\nMax', fontsize='8', color='white',
         backgroundcolor='#090', multialignment='center')
ax2.plot(x, y8_min5, '#099', label='2.00 Min')
fig.text(0.588, 0.555, '2.00\nMin', fontsize='8', color='white',
         backgroundcolor='#099', multialignment='center')
ax2.plot(x, y8_max5, '#099', label='2.00 Max')
fig.text(0.588, 0.70, '2.00\nMax', fontsize='8', color='white',
         backgroundcolor='#099', multialignment='center')
ax2.plot(x, y9_min5, '#009', label='2.05 Min')
fig.text(0.588, 0.65, '2.05\nMin', fontsize='8', color='white',
         backgroundcolor='#009', multialignment='center')
ax2.plot(x, y9_max5, '#009', label='2.05 Max')
fig.text(0.588, 0.79, '2.05\nMax', fontsize='8', color='white',
         backgroundcolor='#009', multialignment='center')
ax2.plot(x, y10_min5, '#909', label='2.1 Min')
fig.text(0.588, 0.745, '2.10\nMin', fontsize='8', color='white',
         backgroundcolor='#909', multialignment='center')
ax2.plot(x, y10_max5, '#909', label='2.1 Max')
fig.text(0.588, 0.84, '2.10\nMax', fontsize='8', color='white',
         backgroundcolor='#909', multialignment='center')

ax2.set_title('7-1/8" FRT-HF Interal Plate Chart',
              fontsize='16', pad='50', ha='center')
plt.figtext(0.78, 0.915, '1.80" Rotating Valve',
            fontsize='14', ha='center')
plt.figtext(0.78, 0.885, '500 psi - 600 psi Pressure Drop',
            fontsize='14', ha='center')
ax2.set_xlabel('Mud Weight', fontsize='14', labelpad=10)
ax2.set_ylabel('Flow Rate', fontsize='14', labelpad=10)
ax2.set_xlim(7, 15.5)
ax2.set_ylim(400, 800)
ax2.minorticks_on()
ax2.grid(which='major')
ax2.grid(which='minor', linestyle=':')

line = plt.Line2D([0.5, 0.5], [1, 0], transform=fig.transFigure, color="black")
fig.add_artist(line)

fig.tight_layout(pad=2.0)
fig.savefig('out.png')
