# Web Scraping com Python

#1: como fazer o python acessar o site da ALESP ?
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

pl = {}
lista_url = []

url = "https://www.al.sp.gov.br/propositura/?id=100025293&tipo=1&ano=2018"

##contexto
with uReq(url) as pagina:
    conteudo = pagina.read()

#2: feito o acesso, como extrair os dados de forma que seja possível a manipulação
#Beautifulsoup

pagina_estruturada = soup(conteudo, "html.parser")

div_alvo = pagina_estruturada.findAll("div",{"class":"ativo","id":"referencias"})

tabela = div_alvo[0].table.tbody.find_all("td")

pl['num_legislativo'] = tabela[3].text.strip()
pl['ementa'] = tabela[5].text.strip()
pl['data'] = tabela[7].text.strip()
pl['regime'] = tabela[9].text.strip()
pl['autores'] = tabela[11].text.strip()
pl['apoiadores'] = tabela[13].text.strip()
pl['indexadores'] = tabela[15].text.strip()
pl['etapa_atual'] = tabela[17].text.strip()

#3: como manipular esses dados ?

#4: como transformar em informação ?

