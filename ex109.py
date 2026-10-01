def notas (*n, sit=True):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos
    :param sit: valor opcional
    :return: dicionário com várias informações sobre a situação dos alunos
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r ['Média'] >= 7:
            r['situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

resp = notas(5.5, 8, 7)
print(resp)
help(notas)