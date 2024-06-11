import audioRecognition as ar
import matchAlgo as ma
import time

def programRun():
    ar.main()
    time.sleep(5)
    ma.main()

if __name__ == "__main__":
    programRun()