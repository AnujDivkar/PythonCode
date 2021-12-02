#python cs1.py a.txt x.txt
import sys
import threading
def processFile(filename):
    try: 
        file = open(filename, "r")
        number_of_lines = 0
        number_of_words = 0
        for line in file:
            line = line.strip("\n")
            words = line.split()
            number_of_lines += 1
            number_of_words += len(words)
        file.close()
        print(filename, "\t", number_of_lines, "\t", number_of_words)
    except: 
        print('File not found')
def main(argv):
   thread_list = []
   for arg in argv:
        thread = threading.Thread(target=processFile, args=(arg,))
        thread_list.append(thread)
   for thread in thread_list:
        thread.start()
main(sys.argv[1:])