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
<<<<<<< HEAD
    if not exists(BACKUP_DESTINO) and done:
=======
    if not exists(BACKUPDESTINO) and done:
>>>>>>> 3842f468e8347a7ca2f86f1dee321978a545d851
        try:
            mkdir(BACKUP_DESTINO)
        except:
            print("Disco não encontrado!")
            done = False
    return done

<<<<<<< HEAD

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
=======
def Backup(arquivoFonte, arquivoDestino):
    if not exists(arquivoDestino):
        copy(arquivoFonte, arquivoDestino)
        print(f"Copiando... ${arquivoFonte} -> ${arquivoDestino}")
>>>>>>> 3842f468e8347a7ca2f86f1dee321978a545d851
    else:
        print(f"Ja existe um backup para o arquivo: ${arquivoDestino}")


def LoopBackup():
    done = False
    wasVerified = False
    while not done:
        relogio = localtime()
<<<<<<< HEAD
        horas = relogio[3]  # Indice 3 são as horas.
        if horas == 8 or horas == 20:  # Flag para controlar quando será executado o backup
            liberar = True
        if horas == 9 or horas == 21 and liberar:
=======
        horas = relogio[3] #Indice 3 são as horas.
        if horas == 22 or horas == 10:
            wasVerified = False
        if horas == 21 or horas == 9 and not wasVerified:
>>>>>>> 3842f468e8347a7ca2f86f1dee321978a545d851
            try:
                # listando os arquivos da pasta
                nomesArquivos = listdir(BACKUP_FONTE)
                # Ordenando os arquivos
                nomesArquivos = sorted(nomesArquivos, key=len)
                while len(nomesArquivos) > 5:
                    nomesArquivos.pop(0)

                for arquivo in nomesArquivos:
<<<<<<< HEAD
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
            liberar = False  # Deixando a flag False para não executar mais de uma vez


=======
                    arquivoFonte = f"{BACKUPFONTE}\{arquivo}"
                    arquivoDestino = f"{BACKUPDESTINO}\{arquivo}"
                    #Condição para copiar arquivos
                    if isfile(arquivoFonte):
                        Backup(arquivoFonte, arquivoDestino)
                    else:
                        print(f"Não foi possível copiar o {arquivoFonte}")
                wasVerified = True
            except Exception as e:
                print(e)
>>>>>>> 3842f468e8347a7ca2f86f1dee321978a545d851
def Main():
    if VerificarPath():
        LoopBackup()


if __name__ == "__main__":
    Main()
