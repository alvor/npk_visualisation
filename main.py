micro_names = ['Cl', 'Fe', 'Mn', 'B', 'Zn', 'Cu', 'Mo', 'Co', 'Si']
micro_values = [0, 2.449, 0.98, 0.694, 0.531, 0.102, 0.102, 0.102, 0]
micro_colors = ['b', 'saddlebrown', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 9})

plt.title('NPK')

xs = range(len(macro_names))

plt.pie(micro_values, autopct='%.1f', counterclock=False, startangle=180, pctdistance=1.2 , radius = 1.2,
    explode = [0.2] + [0.2 for _ in range(len(micro_names) - 1)], labels=micro_names, labeldistance = 1.3, colors=micro_colors)
plt.pie(macro_values, autopct='%.2f', counterclock=False, startangle=180, pctdistance= 0.7 , radius = 1,
    explode = [0]+[0 for _ in range(len(macro_names) - 1)], labels=macro_names, labeldistance = 0.9,  colors=macro_colors)
#plt.legend(
#    bbox_to_anchor = (-0.16, 0.45, 0.25, 0.25),
#    loc = 'lower left', labels = macro_names )

fig.savefig('pie.png')
