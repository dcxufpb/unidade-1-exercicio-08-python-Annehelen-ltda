# coding: utf-8

def isEmpty(value:str) -> bool:
        return (value == None) or (len(value) == value.count(" "))

class Loja:
  def __init__(self, nome_loja, logradouro, numero, complemento, bairro, 
               municipio, estado, cep, telefone, observacao, cnpj,
               inscricao_estadual):
    self.nome_loja = nome_loja
    self.logradouro = logradouro
    self.numero = numero
    self.complemento = complemento
    self.bairro = bairro
    self.municipio = municipio
    self.estado = estado
    self.cep = cep
    self.telefone = telefone
    self.observacao = observacao
    self.cnpj = cnpj
    self.inscricao_estadual = inscricao_estadual


def dados_loja_objeto(loja):
    # Implemente aqui
    if (isEmpty(loja.nome_loja)):
        raise Exception("O campo nome da loja é obrigatório")
    if (isEmpty(loja.logradouro)):
        raise Exception("O campo logradouro do endereço é obrigatório")

    numero = int()
    try:
      numero = int(loja.numero)
    except Exception:
      numero = 0
    if(numero<=0):
      numero = "s/n"
  
    if(isEmpty(loja.cnpj)):
        raise Exception("O campo CNPJ da loja é obrigatório")
    if (isEmpty(loja.municipio)):
        raise Exception("O campo município do endereço é obrigatório")
    if (isEmpty(loja.estado)):
        raise Exception("O campo estado do endereço é obrigatório")
    if (isEmpty(loja.inscricao_estadual)):
        raise Exception("O campo inscrição estadual da loja é obrigatório")

    part2 = f"{loja.logradouro}, {numero}"
    if not isEmpty (loja.complemento):
        part2 += f" {loja.complemento}"
    part3 = str()
    if not isEmpty (loja.bairro):
        part3 += f"{loja.bairro} - "
    part3 += f"{loja.municipio} - {loja.estado}"
    part4 = str()
    if not isEmpty (loja.cep):
        part4 = f"CEP:{loja.cep}"
    if not isEmpty(loja.telefone):
        if not isEmpty(part4):
            part4 += " "
        part4 += f"Tel {loja.telefone}"     
    if not isEmpty(part4):
        part4 += "\n"
    part5 = str()
    if not isEmpty(loja.observacao):
        part5 += f"{loja.observacao}"
    
    output = f"{loja.nome_loja}\n"
    output += f"{part2}\n"
    output += f"{part3}\n"
    output += f"{part4}"
    output += f"{part5}\n"
    output += f"CNPJ: {loja.cnpj}\n"
    output += f"IE: {loja.inscricao_estadual}"

    return output 
