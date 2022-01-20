import os 
import shutil
import time
from configs import BACKUPFONTE,BACKUPDESTINO,MINUTOS_ENTRE_CHECKAGENS

def VerificarPath():
    done = True
    if not os.path.exists(BACKUPFONTE):
        print(f"Pasta {BACKUPFONTE} não existe!\nAbortando backup!")
        done = False
    if not os.path.exists(BACKUPDESTINO) and done == True:
        os.mkdir(BACKUPDESTINO)
    return done

def Backup(arquivoFonte,arquivoDestino):
    if not os.path.exists(arquivoDestino):
        shutil.copy(arquivoFonte, arquivoDestino)
        print(f"Copiando... ${arquivoFonte} -> ${arquivoDestino}")
    else:
        print(f"Ja existe um backup para o arquivo: ${arquivoDestino}")

def LoopBackup():
    done = False
    while not done:
        try:
            #listando os arquivos da pasta
            nomesArquivos = os.listdir(BACKUPFONTE)
            for arquivo in nomesArquivos:
                arquivoFonte = f"{BACKUPFONTE}\{arquivo}"
                arquivoDestino = f"{BACKUPDESTINO}\{arquivo}"
                #Condição para copiar arquivos
                if os.path.isfile(arquivoFonte):
                    Backup(arquivoFonte,arquivoDestino)
                else:
                    print(f"Não foi possível copiar o {arquivoFonte}")

        except Exception as e:
            print(e)

        time.sleep(MINUTOS_ENTRE_CHECKAGENS * 60)#Intervalo para executar o programa - 30 minutos

def Main():
    if VerificarPath():
        LoopBackup()

if __name__ == "__main__":
    Main()