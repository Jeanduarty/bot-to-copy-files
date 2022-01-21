from os import listdir, mkdir
from os.path import exists, isfile
from shutil import copy
from time import localtime, sleep
from configs import BACKUPFONTE,BACKUPDESTINO, HORAS_ENTRE_CHECKAGENS

def VerificarPath():
    done = True
    if not exists(BACKUPFONTE):
        print(f"Pasta {BACKUPFONTE} não existe!\nAbortando backup!")
        done = False
    if not exists(BACKUPDESTINO) and done == True:
        try:
            mkdir(BACKUPDESTINO)
        except:
            print("Disco não encontrado!")
            done = False
    return done

def Backup(arquivoFonte,arquivoDestino):
    if not exists(arquivoDestino):
        copy(arquivoFonte, arquivoDestino)
        print(f"Copiando... ${arquivoFonte} -> ${arquivoDestino}")
    else:
        print(f"Ja existe um backup para o arquivo: ${arquivoDestino}")

def LoopBackup():
    done = False
    while not done:
        relogio = localtime()
        horas = relogio[3] #Indice 3 são as horas.
        if horas == 21 or horas == 9:
            try:
                #listando os arquivos da pasta
                nomesArquivos = listdir(BACKUPFONTE)
                for arquivo in nomesArquivos:
                    arquivoFonte = f"{BACKUPFONTE}\{arquivo}"
                    arquivoDestino = f"{BACKUPDESTINO}\{arquivo}"
                    #Condição para copiar arquivos
                    if isfile(arquivoFonte):
                        Backup(arquivoFonte,arquivoDestino)
                    else:
                        print(f"Não foi possível copiar o {arquivoFonte}")             
            except Exception as e:
                print(e)
        sleep(HORAS_ENTRE_CHECKAGENS * 60) #Programei para executar depois de 11 horas

def Main():
    if VerificarPath():
        LoopBackup()

if __name__ == "__main__":
    Main()