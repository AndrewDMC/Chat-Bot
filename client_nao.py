import sys
import socket #nao is a client
import time

HOST = "169.254.87.125"
PORT = 9000

class MyClass(GeneratedClass):
    command = ""

    def __init__(self):
        GeneratedClass.__init__(self, False)
        self.tts = ALProxy('ALTextToSpeech')
        self.ttsStop = ALProxy('ALTextToSpeech', True)

    def onLoad(self):
        self.tts = self.session().service('ALAnimatedSpeech')
        self.ttsStop = self.session().service('ALAnimatedSpeech')

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.send("Hello".encode("utf-8"))
        id = self.tts.pCall("say", str("Sono pronto"))
        movement= "contextual"

        while True:
            data = s.recv(1024)
            received = data.decode("utf-8")
            print("Received: " + received)
            if(received == "arrivederci" or received == "arrivederci."):
                sys.exit(0)
            id = self.tts.pCall("say", str(received), {"speakingMovementMode": movement})
            self.ids.append(id)
            #id = self.tts.pCall("say", str(received))
            self.tts.wait(id, 0)
            #comunica con host
            s.send("listen now".encode("utf-8"))

        sock.close()
        # put initialization code here
        pass

    def onUnload(self):
        for id in self.ids:
            try:
                self.ttsStop.stop(id)
            except:
                pass
        while( self.bIsRunning ):
            time.sleep( 0.2 )
        #put clean-up code here
        pass

    def onInput_onStart(self):
        #self.onStopped() #activate the output of the box
        #self.processing()
        pass

    def onInput_onStop(self):
        self.log("Closing the Socket!!")
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box

    def processing(self):
        pass