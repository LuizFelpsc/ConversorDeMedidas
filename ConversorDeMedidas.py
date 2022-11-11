#Conversor De Medidas

m = float(input("Digite Uma Distancia em Metros : "))
print("A Medida de {}m Corresponde a \n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm".format(m,m/1000,m/100,m/10,m*10,m*100,m*1000))
