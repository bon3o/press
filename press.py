#!/usr/bin/python3
#coding=utf8
import time
import RPi.GPIO as GPIO
from EmulatorGUI import GPIO


zasipka_pause = 0.7


#Настраиваем Входы-Выходы
GPIO.setmode(GPIO.BCM)
                                                    #НАЗНАЧЕНИЕ                         № ПИНА НА МАЛИНКЕ
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)           #ЭМ1                                07
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)          #ЭМ2                                11
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)          #ЭМ3                                12
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)          #ЭМ4                                13
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)          #ЭМ5                                15
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)          #ЭМ8                                16
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)          #ЗАСЫПКА ИЗ БУН                     18
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)          #ЗАСЫПКА В БУН                      22
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)          #СИГНАЛ СВЕТ                        33
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)          #СИГНАЛ ЗВУК                        36

GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #ДАТЧИК ПОЛЗУН ВЕРХ                 03
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #ДАТЧИК ТОЛК НИЗ                    05
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #КНОПКА СТАРТ                       08
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #ДАТЧИК ТОЛК ВЕРХ                   10
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #ДАТЧИК ТОЛК ЗАСЫП                  19
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #ДАТЧИК ПОЛЗУН ПЛАВ                 21
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #ДАТЧИК ПОЛЗУН НИЗ                  24
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #ДАТЧИК ЗАС В БУНК                  26
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #ДАТЧИК ЗАС СНАРУЖ                  31
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #РЕЗЕРВ                             29
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #КНОПКА СТОП                        32

pinOut = GPIO.output
pinIn = GPIO.input

### ВЫХОДЫ
# ГИДРАВЛИКА
em1 = 4
em2 = 17
em3 = 18
em4 = 27
em5 = 22
em8 = 23
# ПНЕВМАТИКА
z_out = 24
z_in = 25
# ИНДИКАЦИЯ
lamp = 13
buzz = 16

### ВХОДЫ
polUp = 2
polSlow = 9
polDn = 8
tolUp = 15
tolDn = 3
tolFill = 10
zasOut = 6
zasIn = 7
startBtn = 14
stopBtn = 12

def initial_signal():
    for i in range (1, 10):
        pinOut(buzz, 1)
        time.sleep(0.1)
        pinOut(buzz, 0)
        time.sleep(0.5)
    time.sleep(5)
    print("lets start!")
    return 0

def polzun_up():
    pinOut(em2, 1)
    pinOut(em5, 1)
    return 0

def polzun_slow_down():
    pinOut(em1, 1)
    return 0

def polzun_fast_down():
    pinOut(em1, 1)
    pinOut(em5, 1)
    pinOut(em8, 1)
    return 0

def tolkatel_up():
    pinOut(em4, 1)
    return 0

def tolkatel_down():
    pinOut(em3, 1)

def gidra_stop():
    pinOut(em1, 0)
    pinOut(em2, 0)
    pinOut(em3, 0)
    pinOut(em4, 0)
    pinOut(em5, 0)
    pinOut(em8, 0)
    return 0

def zasipka_out():
    pinOut(z_out, 1)
    return 0

def zasipka_in():
    pinOut(z_in, 1)
    return 0

def pnevmo_stop():
    pinOut(z_in, 0)
    pinOut(z_out, 0)
    return 0

def halt():
    gidra_stop()
    pnevmo_stop()
    for i in range (1, 2):
        pinOut(buzz, 1)
        time.sleep(0.3)
        pinOut(buzz, 0)
        time.sleep(0.3)
    time.sleep(1)
    for i in range (1, 2):
        pinOut(buzz, 1)
        time.sleep(0.3)
        pinOut(buzz, 0)
        time.sleep(0.3)
    return 0


def tolkatel_fill():
    while pinIn(tolDn) == True:
        tolkatel_down()
    else: 
        gidra_stop()
    while pinIn(tolFill) == True:
        tolkatel_up()
    else:
        gidra_stop()
    return 0

def fill():
    while pinIn(zasOut) == True:
        zasipka_out()
    else:
        pnevmo_stop()
        time.sleep(zasipka_pause)
    for i in range(1, 3):
            zasipka_in()
            time.sleep(zasipka_pause)
            pnevmo_stop()
            zasipka_out()
            time.sleep(zasipka_pause) 
            pnevmo_stop()   
    while pinIn(zasIn) == True:
        zasipka_in()
    else:
        pnevmo_stop()
    return 0

def suspend():
    while pinIn(startBtn) == True:
        pinOut(lamp, 1)
        time.sleep(0.5)
        pinOut(lamp, 0)
        time.sleep(0.5)
    else:
        return 0

def initial():
    while pinIn(polUp) == True: #While the main cylinder upper sensor is not covered move up
        polzun_up()
    else:
        gidra_stop()
    if pinIn(polUp) == False: #If we are sure that main cylinder us up close the tray
        while pinIn(zasIn) == True:
            zasipka_in()
        else:
            pnevmo_stop() 
    else:
        return 1                                                               
    if pinIn(zasIn) == False:#If we are sure that the tray is closed move the pusher
        while pinIn(tolUp) == True:
            tolkatel_up
        else:
            gidra_stop()
        while pinIn(polSlow) == True:#While the main cylinder middle proximity senser is uncovered move the down
            polzun_slow_down()
        else:
            gidra_stop()
        while pinIn(polUp) == True:#After triggering the middle sensor move up to the first upper sensor
            polzun_up()
        else:
            gidra_stop()
    return 0

def main_cycle():
    if pinIn(tolUp) == False and pinIn(polUp) == False and pinIn(zasIn) == False:
        tolkatel_fill()
        if pinIn(tolUp) == False:
            fill()
        else:
            return 1
        while pinIn(tolDn) == True:
            tolkatel_down()
        else:
            gidra_stop()
        while pinIn(polSlow) == True:
            polzun_fast_down()
        else:
            gidra_stop()
        while pinIn(polDn) == True:
            polzun_slow_down()
        else:
            gidra_stop()
        while pinIn(polUp) == True:
            polzun_up()
        else:
            gidra_stop()
        while pinIn(tolUp) == True:
            tolkatel_up()
        else:
            gidra_stop()
    else:
        return 1
    return 0
    
def main():
    count = 0
    while True:
        if count == 0:
            initialResult = initial()
            if initialResult == 1:
                count = 0
                continue
        else:
            suspend()
            if pinIn(polUp) == False and pinIn(tolUp) == False:
                result = main_cycle()
                if result == 0:
                    count += 1
                else:
                    count = 0

if __name__ == "__main__":
    main()