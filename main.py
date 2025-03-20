# Para testar o código, adicione imagens a pasta "imgs", após rodar, as imagens devem sair formatadas em preto e branco e com efeito de nitidez na pasta "editedImgs".
from PIL import Image, ImageEnhance, ImageFilter # Importa módulos da biblioteca Pillow para manipular imagens
import os # Importa módulos da biblioteca para interagir com o sistema de arquivos
# Define os caminhos das imagens originais e editadas:
path = './imgs' # Originais
pathOut = '/editedImgs' # Editadas
for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}") # Abre a imagem
    edit = img.filter(ImageFilter.SHARPEN).convert('L') # Aplica nitidez, 'sharpen', e converte para tons de cinza, 'L'
    factor = 1.5 # Fator de aumento de contraste
    enhancer = ImageEnhance.Contrast(edit) # Objeto que irá manipular o contraste
    edit = enhancer.enhance(factor) # Aplica o aumento de contraste
    clean_name = os.path.splitext(filename) [0] # Remove a extensão do nome do arquivo para salvar com um novo nome
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg') # Salva a foto editada na pasta com saída de novo nome.



    