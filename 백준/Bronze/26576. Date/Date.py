m={'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06','July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}
ans=[]
for d in open(0).readlines()[1:]:
    mm,dd,yy=d.strip().split()
    dd=int(dd[:-1])
    if mm in m and 1<=dd<=31:ans.append(f"{m[mm]}/{dd:02d}/{yy[-2:].zfill(2)}")
    else:ans.append('Invalid')
print('\n'.join(ans))
    