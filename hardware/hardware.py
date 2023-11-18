import time
import psutil

def display_usage(cpu_usage,memory_usage,bars=50):
    cpu_percent = (cpu_usage/100)
    cpu_bar = '█' * int(cpu_percent*bars) +'-'*(bars -int(cpu_percent*bars))
    
    memory_percent = (memory_usage/100)
    memory_bar = '█' * int(memory_percent*bars) +'-'*(bars -int(memory_percent*bars))
    
    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:0.2f}% ",end="" )
    print(f"\rMEMORY Usage: |{memory_bar}| {memory_usage:0.2f}% ",end="\r" )
    
    
while True:
    display_usage(psutil.cpu_percent(),psutil.virtual_memory().percent,30)
    time.sleep(0.5)
    