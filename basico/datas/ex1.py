from datetime import datetime, timedelta

data_agora = datetime.now() #Pega a data do momento atual
data_futura = data_agora + timedelta(2) #Adicionei 2 dias no futuro
print(data_agora)
print(data_futura)

