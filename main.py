# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
from os.path import expanduser

def rename_files():


    desktop_path = expanduser("~/Desktop/images-dev/motor-grosseiro")  # Caminho para o diretório Desktop

    # Percorre todos os arquivos no diretório Desktop
    for file_name in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, file_name)

        # Verifica se o arquivo é uma foto com uma das extensões de imagem comuns
        if os.path.isfile(file_path) and file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            new_file_name = file_name.lower().replace(" ", "-")  # Substitui espaços por hifens
            new_file_path = os.path.join(desktop_path, new_file_name)

            # Renomeia o arquivo
            os.rename(file_path, new_file_path)

            print(f"Arquivo renomeado: {file_name} -> {new_file_name}")


# Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rename_files()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
