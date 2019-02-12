#!/usr/bin/python3
#coding=utf8
import time
import RPi.GPIO as GPIO

#Настраиваем Входы-Выходы
GPIO.setmode(GPIO.BCM)
																	#НАЗНАЧЕНИЕ						№ ПИНА НА МАЛИНКЕ	
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)				#ЭМ1								07  
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)			#ЭМ2								11
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)			#ЭМ3								12
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)			#ЭМ4								13
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)			#ЭМ5								15
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)			#ЭМ8								16
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)			#ЗАСЫПКА ИЗ БУН				18
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)			#ЗАСЫПКА В БУН					22
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)			#СИГНАЛ СВЕТ					33
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)			#СИГНАЛ ЗВУК					36

GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#ДАТЧИК ПОЛЗУН ВЕРХ 			03
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#ДАТЧИК ТОЛК НИЗ				05
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#КНОПКА СТАРТ					08
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#ДАТЧИК ТОЛК ВЕРХ				10
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#ДАТЧИК ТОЛК ЗАСЫП 			19
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#ДАТЧИК ПОЛЗУН ПЛАВ			21
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#ДАТЧИК ПОЛЗУН НИЗ			24
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#ДАТЧИК ЗАС В БУНК			26
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#ДАТЧИК ЗАС СНАРУЖ			31
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#РЕЗЕРВ							29
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#КНОПКА СТОП					32

po = GPIO.output
pi = GPIO.input

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
pol_up = 2
pol_slow = 9
pol_dn = 8
tol_up = 15
tol_dn = 3
zas_out = 6
zas_in = 7
start_btn = 14
stop_btn = 12

def initial_signal():
    for i in range (1, 10):
        po(16, 1)
	     time.sleep(0.1)
        po(16, 0)
	     time.sleep(0.5)
	 time.sleep(5)
	 print ("lets start!")
    return

def polzun_up():
    po(em2, 1)
	 po(em5, 1)
    return

def polzun_slow_down():
    po(em1, 1)
	 return

def polzun_fast_down():
	 po(em1, 1)
    po(em5, 1)
	 po(em8, 1)
	 return

def tolkatel_up():
	 po(em4, 1)
	 return

def tolkatel_down():
	 po(em3, 1)

def gidra_stop():
	 po(em1, 0)
    po(em2, 0)
	 po(em3, 0)
	 po(em4, 0)
	 po(em5, 0)
	 po(em8, 0)
    return

def zasipka_out():
	 po(z_out, 1)
	 return
	
def zasipka_in():
	 po(z_in, 1)
	 return

def pnevmo_stop():
	 po(z_in, 0)
	 po(z_out, 0)
	 return

def halt():
	gidra_stop()
	pnevmo_stop()

def initial():
    while pi(pol_up) == True:
		 polzun_up()
	 else:
		 gidra_stop()
	 if pi(pol_up) == False:
		 while pi(zas_in) == True:
           zasipka_in()
	    else:
		     pnevmo_stop() 
	 else:
	     halt()
    if pi(zas_in) == False:
	     while pi(tol_up) == True:
		      tolkatel_up
	     else:
		      gidra_stop()
        while pi(pol_slow) == True:
			   polzun_slow_down())
		  else:
			   gidra_stop()
		  while pi(pol_up) == True:
			   polzun_up()
		  else:
			   gidra_stop()
	 return





