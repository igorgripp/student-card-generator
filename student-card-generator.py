from PIL import Image, ImageFont, ImageDraw
import pandas as pd
import os

# Coordenadas dos campos que serão colocadas no background guia
coord_nome = (135, 126)
coord_curso = (140, 197)
coord_data = (307, 234)
coord_matricula = (180, 273)
coord_foto = (597, 170)


# Definindo a fonte e o tamanho que será usado no carteirinha
caminho_fonte = r'C:\\Windows\\Fonts\\ARIALBD.TTF'
font = ImageFont.truetype(caminho_fonte, 26)

# Variaveis de cores para fonte
rgb_preto = (0, 0, 0)
rgb_branco = (255, 255, 255)

# Tamanho da foto na carteirinha
foto_size = 366, 400

#Carregando arquivo com os dados dos alunos
file = pd.read_csv('CSV\\lista_alunos.csv', encoding='UTF-8')

# Carregando somente os alunos que matrícula
listaAluno = (file[file['Matrícula do Aluno'].notna()]).values.tolist()

# Loop de geração das carteirinhas
for aluno in listaAluno:
    path_foto_aluno = 'JPG\\'+aluno[2]+'\\' + aluno[1] + '.jpg'
    path_pasta_aluno = 'student-cards\\' + str(aluno[2])[0:11]

    
    if os.path.exists(path_foto_aluno):

        if not os.path.exists(path_pasta_aluno):
            os.mkdir(path_pasta_aluno)

        image = Image.open(r'JPG\\student-card-canva.jpg')
        foto_aluno = Image.open(path_foto_aluno)

        foto_aluno.thumbnail(foto_size, Image.ANTIALIAS)

        nome_aluno = aluno[1]
        curso_aluno = str(aluno[2])[:6]
        data_aluno = aluno[3]
        matricula_aluno = str(aluno[0])

        # Ajuste da matriculo para fica no padrão: 9999
        lenMatricula = 4 - int(len(matricula_aluno))
        if(lenMatricula > 0):
            for i in range(lenMatricula):
                matricula_aluno = "0" + matricula_aluno
        
        desenho = ImageDraw.Draw(image)

        desenho.text(coord_nome, nome_aluno, font=font, fill=rgb_branco)
        desenho.text(coord_curso, curso_aluno, font=font, fill=rgb_preto)
        desenho.text(coord_data, data_aluno, font=font, fill=rgb_preto)
        desenho.text(coord_matricula, matricula_aluno, font=font, fill=rgb_preto)
        
        image.paste(foto_aluno, coord_foto)

        image.save(path_pasta_aluno + '\\' + nome_aluno + '.jpg')
        image.close()
    else:
        # LOg de alunos que não tem foto para a carteirinha
        print(aluno[2] + ': ' + aluno[1])