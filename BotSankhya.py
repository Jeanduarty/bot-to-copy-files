import os 
import shutil
import time
from email import message

#Pegando o Path das pastas 
backupFonte = r'C:\Users\jeand\Documents\ProjetoPython\BackupFonteSankhya'
backupDestino = r'G:\Meu Drive\BackupExternoSankhya'

def VerificarPath():
    done = False
    if not os.path.exists(backupFonte):
        print(f"Pasta {backupFonte} não existe!")
        done = True
    if not os.path.exists(backupDestino) and done == False:
        os.mkdir(backupDestino)
    return done

def Backup():
    done = False
    while not done:
        try:
            #listando os arquivos da pasta
            listaArquivos = os.listdir(backupFonte)
            for arquivo in listaArquivos:
                #Path dos arquivos
                arquivoInterno = f"{backupFonte}\{arquivo}"
                arquivoExterno = f"{backupDestino}\{arquivo}"
                #Condição para copiar arquivos
                if os.path.isfile(arquivoInterno):
                    if not os.path.exists(arquivoExterno):
                        shutil.copy(arquivoInterno,backupDestino)
                        print("Copiando...")
                    else:
                        print("Ja existe")
                else:
                    print("Arquivo não reconhecido")
        except Exception as e:
            print(e)

        time.sleep(3600)#Intervalo para executar o programa - 1hora

def Main():
    if VerificarPath() == False:
        Backup()

if __name__ == "__main__":
    Main()