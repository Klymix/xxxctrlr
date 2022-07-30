"""
Example of non-blocking reception from input port.
"""

from __future__ import print_function
import sys
import time
import mido
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal, Qt
from PyQt5.QtGui import QColor, QPalette

import sys
"""
port = mido.open_input('USB Uno MIDI Interface:USB Uno MIDI Interface MIDI 1 40:0')
"""
midiports = mido.get_input_names()

inport1 = mido.open_input(midiports[1])
inport2 = mido.open_input(midiports[2])
#inport = mido.open_input()

class DrumCtrl(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        drumLayout = QGridLayout()
        self.setLayout(drumLayout)
         
### DRUMZ ### 
         ###### LFO FILTER      
        self.A1Fader = QSlider()
        self.A1Fader.setMinimum(0)
        self.A1Fader.setMaximum(127)
        self.A1Fader.setValue(40)
        drumLayout.addWidget(self.A1Fader, 0, 0)
       
                
        self.A2Fader = QSlider()
        self.A2Fader.setMinimum(0)
        self.A2Fader.setMaximum(127)
        self.A2Fader.setValue(40)        
        drumLayout.addWidget(self.A2Fader, 0, 1)
        
        self.A3Fader = QSlider()
        self.A3Fader.setMinimum(0)
        self.A3Fader.setMaximum(127)
        self.A3Fader.setValue(40)
        drumLayout.addWidget(self.A3Fader, 0, 2)
        
###### LOOPER
        self.drumLooper = QHBoxLayout()
        self.A01Butt = QPushButton('4/1')
        self.A01Butt.setMaximumWidth(25)
        self.A02Butt = QPushButton('2/1')
        self.A02Butt.setMaximumWidth(25)
        self.A03Butt = QPushButton('1/1')
        self.A03Butt.setMaximumWidth(25)
        self.A04Butt = QPushButton('1/2')
        self.A04Butt.setMaximumWidth(25)
        self.A05Butt = QPushButton('1/4')
        self.A05Butt.setMaximumWidth(25)
        self.A06Butt = QPushButton('1/8')
        self.A06Butt.setMaximumWidth(25)
        self.drumLooper.addWidget(self.A01Butt, 0)
        self.drumLooper.addWidget(self.A02Butt, 1)
        self.drumLooper.addWidget(self.A03Butt, 2)
        self.drumLooper.addWidget(self.A04Butt, 3)
        self.drumLooper.addWidget(self.A05Butt, 4)
        self.drumLooper.addWidget(self.A06Butt, 5)              
                
        drumLayout.addLayout(self.drumLooper, 1,0, 1, 3)

class BassCtrl(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        bassLayout = QGridLayout()
        self.setLayout(bassLayout)
                
###### LFO FILTER      
        self.A4Fader = QSlider()
        self.A4Fader.setMinimum(0)
        self.A4Fader.setMaximum(127)
        self.A4Fader.setValue(40)
        bassLayout.addWidget(self.A4Fader, 0, 0)
                
        self.A5Fader = QSlider()
        self.A5Fader.setMinimum(0)
        self.A5Fader.setMaximum(127)
        self.A5Fader.setValue(40)        
        bassLayout.addWidget(self.A5Fader, 0, 1)
        
        self.A6Fader = QSlider()
        self.A6Fader.setMinimum(0)
        self.A6Fader.setMaximum(127)
        self.A6Fader.setValue(40)
        bassLayout.addWidget(self.A6Fader, 0, 2)
      
###### LOOPER
        self.bassLooper = QHBoxLayout()
        self.MPK01Butt = QPushButton('4/1')
        self.MPK01Butt.setCheckable(True)
        self.MPK01Butt.setMaximumWidth(32)
        self.MPK02Butt = QPushButton('2/1')
        self.MPK02Butt.setCheckable(True)
        self.MPK02Butt.setMaximumWidth(32)
        self.MPK03Butt = QPushButton('1/1')
        self.MPK03Butt.setCheckable(True)
        self.MPK03Butt.setMaximumWidth(32)
        self.MPK04Butt = QPushButton('1/2')
        self.MPK04Butt.setCheckable(True)
        self.MPK04Butt.setMaximumWidth(32)
        self.bassLooper.addWidget(self.MPK01Butt, 0)
        self.bassLooper.addWidget(self.MPK02Butt, 1)
        self.bassLooper.addWidget(self.MPK03Butt, 2)
        self.bassLooper.addWidget(self.MPK04Butt, 3)
                
        bassLayout.addLayout(self.bassLooper, 1,0,  1, 3)
        
  ###### JOYSTICK
        self.FoxJogAY = QSlider()
        bassLayout.addWidget(self.FoxJogAY, 0, 4)
        
        self.FoxJogAX = QSlider(Qt.Horizontal)
        bassLayout.addWidget(self.FoxJogAX, 1, 4)
        
class AcydCtrl(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        acydLayout = QGridLayout()
        self.setLayout(acydLayout)
        
         
###### LFO FILTER      
        self.B1Fader = QSlider()
        self.B1Fader.setMinimum(0)
        self.B1Fader.setMaximum(127)
        self.B1Fader.setValue(40)
        acydLayout.addWidget(self.B1Fader, 0, 0)
        #self.B1Fader.setStyleSheet("background-color: yellow")
                 
        self.B2Fader = QSlider()
        self.B2Fader.setMinimum(0)
        self.B2Fader.setMaximum(127)
        self.B2Fader.setValue(40)        
        acydLayout.addWidget(self.B2Fader, 0, 1)
         
        self.B3Fader = QSlider()
        self.B3Fader.setMinimum(0)
        self.B3Fader.setMaximum(127)
        self.B3Fader.setValue(40)
        acydLayout.addWidget(self.B3Fader, 0, 2)
        
###### JOYSTICK
        self.FoxJogBY = QSlider()
        acydLayout.addWidget(self.FoxJogBY, 0, 4)
      
        self.FoxJogBX = QSlider(Qt.Horizontal)
        acydLayout.addWidget(self.FoxJogBX, 1, 4)
         
###### LOOPER
        self.acydLooper = QHBoxLayout()
        self.A07Butt = QPushButton('4/1')
        self.A07Butt.setMaximumWidth(25)
        self.A08Butt = QPushButton('2/1')
        self.A08Butt.setMaximumWidth(25)
        self.A09Butt = QPushButton('1/1')
        self.A09Butt.setMaximumWidth(25)
        self.A10Butt = QPushButton('1/2')
        self.A10Butt.setMaximumWidth(25)
        self.A11Butt = QPushButton('1/4')
        self.A11Butt.setMaximumWidth(25)
        self.A12Butt = QPushButton('1/8')
        self.A12Butt.setMaximumWidth(25)
        self.acydLooper.addWidget(self.A07Butt, 0)
        self.acydLooper.addWidget(self.A08Butt, 1)
        self.acydLooper.addWidget(self.A09Butt, 2)
        self.acydLooper.addWidget(self.A10Butt, 3)
        self.acydLooper.addWidget(self.A11Butt, 4)
        self.acydLooper.addWidget(self.A12Butt, 5)
                
 ###### DIALz
        self.acydDialz = QHBoxLayout()
        self.MPKDial01 = QDial()
        self.MPKDial02 = QDial()
        self.MPKDial03 = QDial()
        self.MPKDial04 = QDial()
        self.acydDialz.addWidget(self.MPKDial01, 0)
        self.acydDialz.addWidget(self.MPKDial02, 0)
        self.acydDialz.addWidget(self.MPKDial03, 0)
        self.acydDialz.addWidget(self.MPKDial04, 0)
       
        
        acydLayout.addLayout(self.acydLooper, 1,0, 1, 3)
        acydLayout.addLayout(self.acydDialz, 2,0, 1, 3)
        
class NppCtrl(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        nppLayout = QGridLayout()
        self.setLayout(nppLayout)
######  FADERz   
        self.B4Fader = QSlider()
        self.B4Fader.setMinimum(0)
        self.B4Fader.setMaximum(127)
        self.B4Fader.setValue(40)
        nppLayout.addWidget(self.B4Fader, 0, 0)
        #self.B4Fader.setStyleSheet("background-color: yellow")
                 
        self.B5Fader = QSlider()
        self.B5Fader.setMinimum(0)
        self.B5Fader.setMaximum(127)
        self.B5Fader.setValue(40)        
        nppLayout.addWidget(self.B5Fader, 0, 1)
         
        self.B6Fader = QSlider()
        self.B6Fader.setMinimum(0)
        self.B6Fader.setMaximum(127)
        self.B6Fader.setValue(40)
        nppLayout.addWidget(self.B6Fader, 0, 2)
        
###### JOYSTICK
        self.FoxJogCY = QSlider()
        nppLayout.addWidget(self.FoxJogCY, 0, 4)
      
        self.FoxJogCX = QSlider(Qt.Horizontal)
        nppLayout.addWidget(self.FoxJogCX, 1, 4)
         
###### LOOPER
        self.nppLooper = QHBoxLayout()
        self.MPK05Butt = QPushButton('4/1')
        self.MPK05Butt.setCheckable(True)
        self.MPK05Butt.setMaximumWidth(25)
        self.MPK06Butt = QPushButton('2/1')
        self.MPK06Butt.setCheckable(True)
        self.MPK06Butt.setMaximumWidth(25)
        self.MPK07Butt = QPushButton('1/1')
        self.MPK07Butt.setCheckable(True)
        self.MPK07Butt.setMaximumWidth(25)
        self.MPK08Butt = QPushButton('1/2')
        self.MPK08Butt.setMaximumWidth(25)
        self.MPK08Butt.setCheckable(True)
        self.nppLooper.addWidget(self.MPK05Butt, 0)
        self.nppLooper.addWidget(self.MPK06Butt, 1)
        self.nppLooper.addWidget(self.MPK07Butt, 2)
        self.nppLooper.addWidget(self.MPK08Butt, 3)
                        
 ###### DIALz
        self.nppDialz = QHBoxLayout()
        self.MPKDial05 = QDial()
        self.MPKDial06 = QDial()
        self.MPKDial07 = QDial()
        self.MPKDial08 = QDial()
        self.nppDialz.addWidget(self.MPKDial05, 0)
        self.nppDialz.addWidget(self.MPKDial06, 0)
        self.nppDialz.addWidget(self.MPKDial07, 0)
        self.nppDialz.addWidget(self.MPKDial08, 0)
       
        
        nppLayout.addLayout(self.nppLooper, 1,0, 1, 3)
        nppLayout.addLayout(self.nppDialz, 2,0, 1, 3)
        

class Worker(QObject):
    finished = pyqtSignal()
    msgIn = pyqtSignal()
    
    _channel = 127
    _control = 127
    _value = 127
    _note = 127
    _velocity = 66
    _type = 'control_change'
    
    def run(self):
        while True:
            for msg in inport1.iter_pending() :
                print(msg)
                self._channel = msg.channel
                if msg.type == 'control_change' :
                    self._type = 'control_change'
                    self._control = msg.control
                    self._value  = msg.value
                if msg.type == 'note_on' :
                    self._type = 'note_on'
                    self._note = msg.note
                    self._velocity = msg.velocity
                if msg.type == 'note_off' :
                    self._type = 'note_off'
                    self._note = msg.note
                    self._velocity = msg.velocity
                self.msgIn.emit()
                
            for msg in inport2.iter_pending() :
                print(msg)
                self._channel = msg.channel
                if msg.type == 'control_change' :
                    self._type = 'control_change'
                    self._control = msg.control
                    self._value  = msg.value
                if msg.type == 'note_on' :
                    self._type = 'note_on'
                    self._note = msg.note
                    self._velocity = msg.velocity
                if msg.type == 'note_off' :
                    self._type = 'note_off'
                    self._note = msg.note
                    self._velocity = msg.velocity
                self.msgIn.emit()
            time.sleep(0.01)
        
  
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        self.thread =  QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        
        mainLayout = QGridLayout()
        self.setLayout(mainLayout)
################
### DRUMZ ###         
        self.drumCtrl = DrumCtrl()
        
        self.drumFrame = QFrame()
        self.drumFrame.setFrameStyle(QFrame.Panel)        
        self.drumFrame.setStyleSheet("color: orange")
        self.drumFrame.setLineWidth(2)
        #self.drumFrame.setAutoFillBackground(0)
        
        mainLayout.addWidget(self.drumFrame, 0, 0, 1, 1)

        mainLayout.addWidget(self.drumCtrl,0,0)
        self.drumCtrl.setStyleSheet("color: orange")
        self.drumCtrl.setStyleSheet("text-color : black")
################     
### BASSz ### 
        self.bassCtrl = BassCtrl()
        self.bassFrame = QFrame()
        self.bassFrame.setFrameStyle(QFrame.Panel)        
        self.bassFrame.setStyleSheet("color: yellow")
        self.bassFrame.setLineWidth(2)
        #self.bassFrame.setAutoFillBackground(0)
        
        mainLayout.addWidget(self.bassFrame, 0, 1, 1, 1)

        mainLayout.addWidget(self.bassCtrl,0,1)
        self.bassCtrl.setStyleSheet("color: yellow")
        self.bassCtrl.setStyleSheet("text-color : black")
        
 
### ACYDz ### 
        self.acydCtrl = AcydCtrl()
        self.acydFrame = QFrame()
        self.acydFrame.setFrameStyle(QFrame.Panel)        
        self.acydFrame.setStyleSheet("color: green")
        self.acydFrame.setLineWidth(2)
        #self.acydFrame.setAutoFillBackground(0)
        
        mainLayout.addWidget(self.acydFrame, 1, 0, 1, 1)

        mainLayout.addWidget(self.acydCtrl,1,0)
        self.acydCtrl.setStyleSheet("color: green")
        self.acydCtrl.setStyleSheet("text-color : black")
         
       
### NPPz ### 
        self.nppCtrl = NppCtrl()
        self.nppFrame = QFrame()
        self.nppFrame.setFrameStyle(QFrame.Panel)        
        self.nppFrame.setStyleSheet("color: blue")
        self.nppFrame.setLineWidth(2)
        #self.nppFrame.setAutoFillBackground(0)
        
        mainLayout.addWidget(self.nppFrame, 1, 1, 1, 1)

        mainLayout.addWidget(self.nppCtrl,1,1)
        self.nppCtrl.setStyleSheet("color: blue")
        self.nppCtrl.setStyleSheet("text-color : black")
        
        self.thread.started.connect(self.worker.run)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
       
        self.thread.start()
        
        self.worker.msgIn.connect(self.motor)

        
    def resetAcydButts(self):
        self.acydCtrl.A07Butt.setDown(False)
        self.acydCtrl.A08Butt.setDown(False)
        self.acydCtrl.A09Butt.setDown(False)
        self.acydCtrl.A10Butt.setDown(False)
        self.acydCtrl.A11Butt.setDown(False)
        self.acydCtrl.A12Butt.setDown(False)
        
        
    def motor(self):
###### DRUMz Controler
        ### Drum Fox Faders
        if self.worker._channel == 11 and self.worker._control == 0:
            self.drumCtrl.A1Fader.setValue(self.worker._value)
        if self.worker._channel == 11 and self.worker._control == 1:
            self.drumCtrl.A2Fader.setValue(self.worker._value)
        if self.worker._channel == 11 and self.worker._control == 2:
            self.drumCtrl.A3Fader.setValue(self.worker._value)
        ### Drum Fox Loop Butts
        if self.worker._channel == 11 and self.worker._note == 8 and self.worker._velocity == 127:
            self.drumCtrl.A01Butt.setDown(True)
        if self.worker._channel == 11 and self.worker._note == 8 and self.worker._velocity == 0:
            self.drumCtrl.A01Butt.setDown(False)
        if self.worker._channel == 11 and self.worker._note == 9 and self.worker._velocity == 127:
            self.drumCtrl.A02Butt.setDown(True)
        if self.worker._channel == 11 and self.worker._note == 9 and self.worker._velocity == 0:
            self.drumCtrl.A02Butt.setDown(False)
        if self.worker._channel == 11 and self.worker._note == 10 and self.worker._velocity == 127:
            self.drumCtrl.A03Butt.setDown(True)
        if self.worker._channel == 11 and self.worker._note == 10 and self.worker._velocity == 0:
            self.drumCtrl.A03Butt.setDown(False)
        if self.worker._channel == 11 and self.worker._note == 11 and self.worker._velocity == 127:
            self.drumCtrl.A04Butt.setDown(True)
        if self.worker._channel == 11 and self.worker._note == 11 and self.worker._velocity == 0:
            self.drumCtrl.A04Butt.setDown(False)
        if self.worker._channel == 11 and self.worker._note == 12 and self.worker._velocity == 127:
            self.drumCtrl.A05Butt.setDown(True)
        if self.worker._channel == 11 and self.worker._note == 12 and self.worker._velocity == 0:
            self.drumCtrl.A05Butt.setDown(False)
        if self.worker._channel == 11 and self.worker._note == 13 and self.worker._velocity == 127:
            self.drumCtrl.A06Butt.setDown(True)
        if self.worker._channel == 11 and self.worker._note == 13 and self.worker._velocity == 0:
            self.drumCtrl.A06Butt.setDown(False)
            
  ###### BASS Controler      
        ### Bass Fox Faders
        if self.worker._channel ==11 and self.worker._control == 3:
            self.bassCtrl.A4Fader.setValue(self.worker._value)
        if self.worker._channel == 11 and self.worker._control == 4:
            self.bassCtrl.A5Fader.setValue(self.worker._value)
        if self.worker._channel == 11 and self.worker._control == 5:
            self.bassCtrl.A6Fader.setValue(self.worker._value)
        ### Bass MPK Loop Butts
        if self.worker._type == 'note_on' and self.worker._channel == 9 and self.worker._note == 40  :
            self.bassCtrl.MPK02Butt.setChecked(False)
            self.bassCtrl.MPK03Butt.setChecked(False)
            self.bassCtrl.MPK04Butt.setChecked(False)
            self.bassCtrl.MPK01Butt.toggle()
        if self.worker._type == 'note_on' and self.worker._channel == 9 and self.worker._note == 41  :
            self.bassCtrl.MPK01Butt.setChecked(False)
            self.bassCtrl.MPK03Butt.setChecked(False)
            self.bassCtrl.MPK04Butt.setChecked(False)
            self.bassCtrl.MPK02Butt.toggle()
        if self.worker._type == 'note_on' and self.worker._channel == 9 and self.worker._note == 42  :
            self.bassCtrl.MPK01Butt.setChecked(False)
            self.bassCtrl.MPK02Butt.setChecked(False)
            self.bassCtrl.MPK04Butt.setChecked(False)
            self.bassCtrl.MPK03Butt.toggle()
        if self.worker._type == 'note_on' and self.worker._channel == 9 and self.worker._note == 43  :
            self.bassCtrl.MPK01Butt.setChecked(False)
            self.bassCtrl.MPK02Butt.setChecked(False)
            self.bassCtrl.MPK03Butt.setChecked(False)
            self.bassCtrl.MPK04Butt.toggle()
       #### JOYSTICK
        if self.worker._channel ==9 and self.worker._control == 16:
            self.bassCtrl.FoxJogAY.setValue(self.worker._value)
        if self.worker._channel == 9 and self.worker._control == 36:
            self.bassCtrl.FoxJogAX.setValue(self.worker._value)

###### ACYD Controler            
        ### Acyd Fox Faders
        if self.worker._channel == 11 and self.worker._control == 6:
            self.acydCtrl.B1Fader.setValue(self.worker._value)
        if self.worker._channel == 11 and self.worker._control == 7:
            self.acydCtrl.B2Fader.setValue(self.worker._value)
        if self.worker._channel == 11 and self.worker._control == 8:
            self.acydCtrl.B3Fader.setValue(self.worker._value)
        ### Acyd Fox Loop Butts
        if self.worker._channel == 11 and self.worker._note == 14 and self.worker._velocity == 127:
            self.resetAcydButts()
            self.acydCtrl.A07Butt.setDown(True)
        if self.worker._channel == 11 and self.worker._note == 15 and self.worker._velocity == 127:
            self.resetAcydButts()
            self.acydCtrl.A08Butt.setDown(True)       
        if self.worker._channel == 11 and self.worker._note == 39 and self.worker._velocity == 127:
            self.resetAcydButts()
            self.acydCtrl.A09Butt.setDown(True)
        if self.worker._channel == 11 and self.worker._note == 40 and self.worker._velocity == 127:
            self.resetAcydButts()
            self.acydCtrl.A10Butt.setDown(True)
        if self.worker._channel == 11 and self.worker._note == 41 and self.worker._velocity == 127:
            self.resetAcydButts()
            self.acydCtrl.A11Butt.setDown(True)
        if self.worker._channel == 11 and self.worker._note == 42 and self.worker._velocity == 127:
            self.resetAcydButts()
            self.acydCtrl.A12Butt.setDown(True)
        #### JOYSTICK
        if self.worker._channel == 11 and self.worker._control == 36:
            self.acydCtrl.FoxJogBY.setValue(self.worker._value)
        if self.worker._channel == 11 and self.worker._control == 38:
            self.acydCtrl.FoxJogBX.setValue(self.worker._value)
        ### Acyd Dialz
        if self.worker._channel == 0 and self.worker._control == 70:
            self.acydCtrl.MPKDial01.setValue(self.worker._value)
        if self.worker._channel == 0 and self.worker._control == 71:
            self.acydCtrl.MPKDial02.setValue(self.worker._value)
        if self.worker._channel == 0 and self.worker._control == 72:
            self.acydCtrl.MPKDial03.setValue(self.worker._value)
        if self.worker._channel == 0 and self.worker._control == 73:
            self.acydCtrl.MPKDial04.setValue(self.worker._value)
            
###### NPP Controler            
        ### NPP Fox Faders
        if self.worker._channel == 11 and self.worker._control == 9:
            self.nppCtrl.B4Fader.setValue(self.worker._value)
        if self.worker._channel == 11 and self.worker._control == 10:
            self.nppCtrl.B5Fader.setValue(self.worker._value)
        if self.worker._channel == 11 and self.worker._control == 11:
            self.nppCtrl.B6Fader.setValue(self.worker._value)
        ### Npp MPK Loop Butts
        if self.worker._type == 'note_on' and self.worker._channel == 9 and self.worker._note == 36  :
            self.nppCtrl.MPK06Butt.setChecked(False)
            self.nppCtrl.MPK07Butt.setChecked(False)
            self.nppCtrl.MPK08Butt.setChecked(False)
            self.nppCtrl.MPK05Butt.toggle()
        if self.worker._type == 'note_on' and self.worker._channel == 9 and self.worker._note == 37  :
            self.nppCtrl.MPK05Butt.setChecked(False)
            self.nppCtrl.MPK07Butt.setChecked(False)
            self.nppCtrl.MPK08Butt.setChecked(False)
            self.nppCtrl.MPK06Butt.toggle()
        if self.worker._type == 'note_on' and self.worker._channel == 9 and self.worker._note == 38  :
            self.nppCtrl.MPK05Butt.setChecked(False)
            self.nppCtrl.MPK06Butt.setChecked(False)
            self.nppCtrl.MPK08Butt.setChecked(False)
            self.nppCtrl.MPK07Butt.toggle()
        if self.worker._type == 'note_on' and self.worker._channel == 9 and self.worker._note == 39  :
            self.nppCtrl.MPK05Butt.setChecked(False)
            self.nppCtrl.MPK06Butt.setChecked(False)
            self.nppCtrl.MPK07Butt.setChecked(False)
            self.nppCtrl.MPK08Butt.toggle()
        
        #### JOYSTICK
        if self.worker._channel == 11 and self.worker._control == 37:
            self.nppCtrl.FoxJogCY.setValue(self.worker._value)
        if self.worker._channel == 11 and self.worker._control == 39:
            self.nppCtrl.FoxJogCX.setValue(self.worker._value)
        ### Npp Dialz
        if self.worker._channel == 0 and self.worker._control == 74:
            self.nppCtrl.MPKDial05.setValue(self.worker._value)
        if self.worker._channel == 0 and self.worker._control == 75:
            self.nppCtrl.MPKDial06.setValue(self.worker._value)
        if self.worker._channel == 0 and self.worker._control == 76:
            self.nppCtrl.MPKDial07.setValue(self.worker._value)
        if self.worker._channel == 0 and self.worker._control == 77:
            self.nppCtrl.MPKDial08.setValue(self.worker._value)
        
            
            
        
        # if self.worker._type == 'note_on' and self.worker._channel == 9 and self.worker._note == 40 and self.MPK01Butt.isDown() :
        #     self.MPK01Butt.setChecked(False)
        
            # if self.MPK01Butt.isDown():
            #     self.MPK01Butt.setDown(False)
            # if not (self.MPK01Butt.isDown()):
            #     self.MPK01Butt.setDown(True)
        # if self.worker._channel == 11 and self.worker._note == 8 and self.worker._velocity == 0:
        #     self.MPK01Butt.setDown(False)
            
        # if self.worker._channel == 11 and self.worker._note == 9 and self.worker._velocity == 127:
        #     self.MPK02Butt.setDown(True)
        # if self.worker._channel == 11 and self.worker._note == 9 and self.worker._velocity == 0:
        #     self.A02Butt.setDown(False)
            
        # if self.worker._channel == 11 and self.worker._note == 10 and self.worker._velocity == 127:
        #     self.A03Butt.setDown(True)
        # if self.worker._channel == 11 and self.worker._note == 10 and self.worker._velocity == 0:
        #     self.A03Butt.setDown(False)
            
        # if self.worker._channel == 11 and self.worker._note == 11 and self.worker._velocity == 127:
        #     self.A04Butt.setDown(True)
        # if self.worker._channel == 11 and self.worker._note == 11 and self.worker._velocity == 0:
        #     self.A04Butt.setDown(False)
            
        # if self.worker._channel == 11 and self.worker._note == 12 and self.worker._velocity == 127:
        #     self.A05Butt.setDown(True)
        # if self.worker._channel == 11 and self.worker._note == 12 and self.worker._velocity == 0:
        #     self.A05Butt.setDown(False)
            
        # if self.worker._channel == 11 and self.worker._note == 13 and self.worker._velocity == 127:
        #     self.A06Butt.setDown(True)
        # if self.worker._channel == 11 and self.worker._note == 13 and self.worker._velocity == 0:
        #     self.A06Butt.setDown(False)
        
    
'''       
try:
    with mido.open_input() as port:
        print('Using {}'.format(port))        
        while True:
            for msg in port.iter_pending():
                print(msg.control, msg.value)  
            time.sleep(0.01)
           
except KeyboardInterrupt:
    pass

'''
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())

