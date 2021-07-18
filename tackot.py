from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
from time import sleep
import sys
import argparse        

def bot(delay):
    urlList = ['http://shrink-service.it/s/DdoWjF', 'http://shrink-service.it/s/5smif4', 'http://shrink-service.it/s/JO2ZqP', 'http://shrink-service.it/s/m02btO', 'http://shrink-service.it/s/0KhJLM', 'http://shrink-service.it/s/hdIF6d'] 
    
    for urls in urlList:
        response = urlopen(urls)
        print ("URL visitada: " + urls)
        sleep(delay)
        print ("Tiempo de espera terminado !!!")

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--delay", help="Tiempo de espera por pagina visitada", type=int)
args = parser.parse_args()

bot(args.delay)    