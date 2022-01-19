import os 
import shutil
import time

from email import message
from configs import pastaBackupFonte, pastaBackupDestino, TEMPO_ENTRE_CHECKAGENS


def PastasOk():
    pastaOk = True
    if not os.path.exists(pastaBackupFonte):
        print(f"Pasta Fonte {pastaBackupFonte} não existe!")
        pastaOk = False
    elif not os.path.exists(pastaBackupDestino):
        print(f"Pasta Destino {pastaBackupFonte} não existe. Criando pasta Destino")
        os.mkdir(pastaBackupDestino)
        
    return pastaOk

def TentarBackup(arquivoFonte, arquivoDestino):
    if not os.path.exists(arquivoDestino):
        print(f"Arquivo fonte não encontrado ${arquivoFonte} - Abortando Backup")
        return
        
    
    if not os.path.exists(arquivoDestino):
        shutil.copy(arquivoFonte, arquivoDestino)
        print(f"Copiando... ${arquivoFonte} -> ${arquivoDestino}")
    else:
        print(f"Ja existe um backup para o arquivo: ${arquivoDestino}")
    return


def LoopBackup():
    done = False
    while not done:
        try:
            #listando os arquivos da pasta
            nomesArquivos = os.listdir(pastaBackupFonte)
            for nomeArquivo in nomesArquivos:
                #Path dos arquivos
                arquivoFonte = f"{pastaBackupFonte}\{nomeArquivo}"
                arquivoDestino= f"{pastaBackupDestino}\{nomeArquivo}"

                TentarBackup(arquivoFonte, arquivoDestino)
                

        except Exception as e:
            print(e)

        time.sleep(MINUTOS_ENTRE_CHECKAGENS*60) # TODO: No futuro, avaliar se teria uma melhor forma de esperar esse tempo entre as checkagens

def Main():
    if PastasOk():
        LoopBackup()
    else:
        print("Abortando backup, pasta fonte não encontrada")


if __name__ == "__main__":
    Main()