P1 = 1e5 # Pa
T1 = 170 + 273.15 # K
P2 = 3e5 # Pa
T2 = 330 + 273.15 # K

h1 = cp.PropsSI('H','P',P1,'T',T1,'Water')
s1 = cp.PropsSI('S','P',P1,'T',T1,'Water')
h2 = cp.PropsSI('H','P',P2,'T',T2,'Water')
s2 = cp.PropsSI('S','P',P2,'T',T2,'Water')

print('h1 = %s kJ/kg'%round(h1/1000,2))
print('s1 = %s kJ/kg*K'%round(s1/1000,5))
print('---------------')
print('h2 = %s kJ/kg'%round(h2/1000,2))
print('s2 = %s kJ/kg*K'%round(s2/1000,5))
