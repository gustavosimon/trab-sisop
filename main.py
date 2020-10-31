import psutil

# Varre as pids do SO
# Criar um programa em python para imprimir as seguintes informacoes sobre as pids do sistema operacinal
# - PID ok
# - TGID ok
# - PPID ok
# - Nome ok
# - Estado ok
# - Quantidade de Memoria Residente ok
# - Quantidade de Threads ok

def showPidsInfo():

# Pega a lista de pids do SO
    pids = psutil.pids()
    for pid in pids:
# Pega o processo da pid        
        proc = psutil.Process(pid)
        num_pid = proc.pid
        num_ppid = psutil.Process.ppid(proc)
        name = psutil.Process.name(proc)
        status = psutil.Process.status(proc)
        num_threads = psutil.Process.num_threads(proc)
        pmem = psutil.Process.memory_info(proc)
        rss_memory = pmem[0]
        tgid = getProcessTGID(num_pid)
        print(num_pid, num_ppid, name, status, num_threads, rss_memory, tgid)

def getProcessTGID(pid):
    path ="/proc/{}/status".format(pid)
    f = open(path, "r")
    linhas = f.read().splitlines()
    for linha in linhas:
        if linha.startswith("Tgid"):
            return linha.split("\t")[-1]
    return None

def main():
    showPidsInfo()

if __name__ == '__main__':
    main()
