from os import listdir, mkdir, remove
from os.path import exists, splitext
from shutil import copy
from time import localtime
from configs import BACKUP_FONTE, BACKUP_DESTINO, EXTENSAO


def VerificarPath():
    done = True
    if not exists(BACKUP_FONTE):
        print(f"Pasta {BACKUP_FONTE} não existe!\nAbortando backup!")
        done = False
    if not exists(BACKUP_DESTINO) and done:
        try:
            mkdir(BACKUP_DESTINO)
        except:
            print("Disco não encontrado!")
            done = False
    return done


def LimiteBackup():
    # listando os arquivos da pasta
    listaArquivosDestino = listdir(BACKUP_DESTINO)
    while len(listaArquivosDestino) > 5:
        try:
            arquivoAntigo = listaArquivosDestino[0]
            arquivoAntigoPath = F"{BACKUP_DESTINO}\{arquivoAntigo}"
            print(f"Excluindo arquivo antigo -> {arquivoAntigo}")
            remove(arquivoAntigoPath)
            # Removendo o primeiro item da lista que pela lógica é o mais antigo
            listaArquivosDestino.pop(0)
        except Exception as e:
            print(e)


def Backup(arquivoFonte, arquivoDestino, arquivo):
    # Listando os arquivos da pasta
    listaArquivosDestino = listdir(BACKUP_DESTINO)
    if not arquivo in listaArquivosDestino:
        try:
            copy(arquivoFonte, arquivoDestino)  # Copiando arquivos
            print(f"Copiando... ${arquivoFonte} -> ${arquivoDestino}")
        except Exception as e:
            print(e)
    else:
        print(f"Já existe uma copia para o arquivo => {arquivo}")

def LoopBackup():
    done = False
    wasVerified = False
    while not done:
        relogio = localtime()
        horas = relogio[3]  # Indice 3 são as horas.
        if horas == 8 or horas == 20:  # Flag para controlar quando será executado o backup
            wasVerified = True
        if (horas == 9 or horas == 21) and wasVerified:
            try:
                # listando os arquivos da pasta
                nomesArquivos = listdir(BACKUP_FONTE)
                # Ordenando os arquivos
                nomesArquivos = sorted(nomesArquivos, key=len)
                while len(nomesArquivos) > 5:
                    nomesArquivos.pop(0)

                for arquivo in nomesArquivos:
                    # Dando split para pegar o formato do arquivo
                    nome, extensao = splitext(arquivo)
                    # Setando o path completo dos arquivos
                    arquivoFonte = f"{BACKUP_FONTE}\{arquivo}"
                    arquivoDestino = f"{BACKUP_DESTINO}\{arquivo}"

                    # Condição para copiar arquivos
                    if extensao == EXTENSAO:
                        Backup(arquivoFonte, arquivoDestino, arquivo)
                    else:
                        print(
                            f"{arquivo} // Não será copiado pois não possui formato {EXTENSAO}")
            except Exception as e:
                print(e)

            LimiteBackup()
            wasVerified = False  # Deixando a flag False para não executar mais de uma vez


def Main():
    if VerificarPath():
        LoopBackup()


if __name__ == "__main__":
    Main()
