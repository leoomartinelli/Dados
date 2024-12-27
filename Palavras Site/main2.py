from collections import Counter
import string
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = "https://www.cnnbrasil.com.br/internacional/pensei-que-o-aviao-fosse-despedacar-diz-sobrevivente-de-queda-no-cazaquistao/"

response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')


textos = [titulo.get_text() for titulo in soup.find_all('p')]


texto = " ".join(textos).lower()

# Remove pontuação
texto = texto.translate(str.maketrans("", "", string.punctuation))


palavras = texto.split()

# Tira palavras não impactantes
stopwords = {"e", "o", "de", "a", "em", "um", "uma", "os", "as", "do", "para", "que", "da", "no", "na", "se"}
palavras_filtradas = [palavra for palavra in palavras if palavra not in stopwords]


contagem = Counter(palavras_filtradas)
print(contagem.most_common(10))






# Pegue as 10 palavras mais comuns
palavras, frequencias = zip(*contagem.most_common(10))

# Crie o gráfico de barras
plt.bar(palavras, frequencias)
plt.xlabel("Palavras")
plt.ylabel("Frequência")
plt.title("Palavras mais comentadas")
plt.xticks(rotation=45)
plt.show()