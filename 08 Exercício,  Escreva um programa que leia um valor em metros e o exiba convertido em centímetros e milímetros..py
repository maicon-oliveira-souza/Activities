media = float(input('Uma distância em metros: '))
cm = media * 100
mm = media * 1000
dm = media * 10
dam = media / 10
hm = media / 100
km = media / 1000
print(f'A media de {media}m corresponde a: \n{cm:.3f} cm\n{mm:.3f} mm\n{dm:.3f} dm\n{dam:.3f} dam\n{hm:.3f} hm\n{km:.3f} km')
