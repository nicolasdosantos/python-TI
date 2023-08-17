def obter_data_atual():
    from datetime import datetime, timedelta
    return datetime.now()

def formatar_data(data, formato="%d/%m/%Y"):
    from datetime import datetime, timedelta
    return data.strftime(formato)

def calcular_idade(data_nascimento):
    from datetime import datetime, timedelta
    hoje = datetime.now()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

def adicionar_dias(data, dias):
    from datetime import datetime, timedelta
    nova_data = data + timedelta(days=dias)
    return nova_data

def diferenca_entre_datas(data1, data2):
    from datetime import datetime, timedelta
    diferenca = data2 - data1
    return diferenca.days