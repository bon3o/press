#coding=utf8
import time
import RPi.GPIO as GPIO

#Настраиваем Входы-Выходы

GPIO.setmode(GPIO.BCM)

								#НАЗНАЧЕНИЕ			№ ПИНА НА МАЛИНКЕ	
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)			#ЭМ1				07  
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)			#ЭМ2				11
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)			#ЭМ3				12
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)			#ЭМ4				13
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)			#ЭМ5				15
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)			#ЭМ8				16
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)			#ЗАСЫПКА ИЗ БУН			18
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)			#ЗАСЫПКА В БУН			22
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)			#СИГНАЛ СВЕТ			33
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)			#СИГНАЛ ЗВУК			36

GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)		#ДАТЧИК ПОЛЗУН ВЕРХ 		03
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)		#ДАТЧИК ТОЛК НИЗ		05
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)		#КНОПКА СТАРТ			08
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)		#ДАТЧИК ТОЛК ВЕРХ		10
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)		#ДАТЧИК ТОЛК ЗАСЫП 		19
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)		#ДАТЧИК ПОЛЗУН ПЛАВ		21
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)		#ДАТЧИК ПОЛЗУН НИЗ		24
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)		#ДАТЧИК ЗАС В БУНК		26
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)		#ДАТЧИК ЗАС НАРУЖЕ		31
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)		#РЕЗЕРВ				29
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)		#КНОПКА СТОП			32

while True:
	while GPIO.input(12) == False:
		try:
		   def overall():
			
			#Инициализация: Ползун вверх, Толкатель вверх.

			def initial():
			 GPIO.output(16, 1)
			 time.sleep(0.1)
			 GPIO.output(16, 0)
			 time.sleep(1)
			 GPIO.output(16, 1)
			 time.sleep(0.1)
			 GPIO.output(16, 0)
			 time.sleep(1)
			 GPIO.output(16, 1)
			 time.sleep(0.1)
			 GPIO.output(16, 0)
			 time.sleep(1)
			 GPIO.output(16, 1)
			 time.sleep(0.2)
			 GPIO.output(16, 0)
			 time.sleep(5)
			 print ("lets start!")
			 #GPIO.output(13, 1)

			#Ползун уходит вверх до одного из датчиков верхнего положения. Два датчика на случай, когда ползун оставили в положении выше, чем первый датчик. 

			 while GPIO.input(2) == True: 
			  GPIO.output(17, 1)
			  GPIO.output(22, 1)
			  time.sleep(0.01)
			 else:
			  GPIO.output(17, 0)
			  GPIO.output(22, 0)
			  time.sleep(0.01)
			  
			#Засыпка уезжает в бункер до датчика
			 
			 while GPIO.input(7) == True: 
			  GPIO.output(24, 1)
			  time.sleep(0.01) 
			 else:
			  GPIO.output(24, 0)
			  time.sleep(0.01)

			#Толкатель выезжает до верхнего датчика
			  
			 while GPIO.input(15) == True: 
			  GPIO.output(27, 1)
			  time.sleep(0.01)
			 else:
			  GPIO.output(27, 0)
			  time.sleep(0.01)

			#Далее делаем позиционирование ползуна на его рабочее место - опускаем на плавном ходу до датчика перехода на плавный ход, и поднимаем до первого верх датчика

			 while GPIO.input(9) == True:
			  GPIO.output(4, 1)
			  time.sleep(0.01) 
			 else:
			  GPIO.output(4, 0)
			  time.sleep(0.01)
			 
			 while GPIO.input(2) == True:
			  GPIO.output(17, 1)
			  GPIO.output(22, 1)
			  time.sleep(0.01)
			 else:
			  GPIO.output(17, 0)
			  GPIO.output(22, 0)
			  time.sleep(0.01) 


			initial()

			#Основной цикл программы

			def main():
			 while True:
			  def press():

			   print ("Waiting for start button to be pressed")

			   while GPIO.input(14) == True:
				GPIO.output(13, 0)
				time.sleep(0.01)
			   else: 
				print ("Starting!")
				print ("Fill")
				time.sleep(0.01)
				GPIO.output(13,1)
				time.sleep(0.01)


			   while GPIO.input(2) == True: #PROVERKA polzun vverh do metki
				GPIO.output(17, 1)
				GPIO.output(22, 1)
				time.sleep(0.01)
			   else:
				GPIO.output(17, 0)
				GPIO.output(22, 0)
				time.sleep(0.01)
				
			   print ("proverka tolkatel")
                           while GPIO.input(15) == True: #PROVERKA vitalkivatel vverh do metki
				GPIO.output(27, 1)
				time.sleep(0.01)
			   else:
				GPIO.output(27, 0)
				GPIO.output(13, 0)
				time.sleep(0.01)
				GPIO.output(13, 1)
			        time.sleep(0.01)
			   print ("tolk vniz")
			   while GPIO.input(3) == True: #vitalkivatel samiy niz
				GPIO.output(18, 1)
   			        time.sleep(0.01)
			   else:
				GPIO.output(18, 0)
                                time.sleep(0.01)
               
			   while GPIO.input(6) == True: #Выезжает засыпка
				GPIO.output(24, 0)
				GPIO.output(25, 1)
				time.sleep(0.01)
			   else: 
				print ("Засыпка вышла из бункера")
				time.sleep (0.6)
				GPIO.output(25, 0)
				GPIO.output(24, 1)
				time.sleep (0.8)
				GPIO.output(25, 1)
				GPIO.output(24, 0)
				time.sleep (0.8)
				
				
				
				#GPIO.output(25, 0)
				#GPIO.output(24, 1)
				#time.sleep (0.4)
				#GPIO.output(25, 1)
				#GPIO.output(24, 0)
				#time.sleep (0.4)
			   
			   
			   print ("Толкатель до метки засыпки")
			   while GPIO.input(10) == True: #vitalkivatel do zasipki
				GPIO.output(27, 1)
				time.sleep(0.01)
			   else:
				GPIO.output(27, 0)
				time.sleep(0.01)   
			   
			   
			   while GPIO.input(7) == True:
				GPIO.output(25, 0)
				GPIO.output(24, 1)
				time.sleep(0.01)
			   else:
				GPIO.output(24, 1)
				GPIO.output(16, 1)
				time.sleep(0.3)
				GPIO.output(16, 0)    

				print ("Pressing")

			   while GPIO.input(3) == True: #vitalkivatel do niza
				GPIO.output(18, 1)
				time.sleep(0.01)
			   else:
				GPIO.output(18, 0)
				time.sleep(0.01)

				print ("Fast Run")
			   while GPIO.input(9) == True: #Perehod na plavniy hod
				GPIO.output(4, 1)
				GPIO.output(22, 1)
				GPIO.output(23, 1)
				time.sleep(0.01)
			   else:
				GPIO.output(4, 0)
				GPIO.output(22, 0)
				GPIO.output(23, 0)
				time.sleep(0.01)

				print ("Slow Run")
			   while GPIO.input(8) == True: #plavniy hod
				GPIO.output(4, 1)
				time.sleep(0.01) 
			   else:
				GPIO.output(4, 0) #podpressovka
				print ("Ejecting")
			   while GPIO.input(2) == True: #polzun vverh do metki
				GPIO.output(17, 1)
				GPIO.output(22, 1)
				time.sleep(0.01)
			   else:
				GPIO.output(17, 0)
				GPIO.output(22, 0)
				time.sleep(0.01)

			   while GPIO.input(15) == True: #vitalkivatel vverh do metki
				GPIO.output(27, 1)
				time.sleep(0.01)
			   else:
				GPIO.output(27, 0)
				GPIO.output(13, 0) 
				time.sleep(0.01)
			  press()
		  
			
			main()
		  
		   overall()
			
		except KeyboardInterrupt:  
		  GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
		GPIO.cleanup()           # clean up GPIO on normal exit 
