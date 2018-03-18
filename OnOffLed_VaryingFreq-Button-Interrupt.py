import	machine
import	time

#	OUTPUT	PINS	-	LEDs
pin_D0	=	machine.Pin(16,	machine.Pin.OUT)
pin_D1	=	machine.Pin(5,machine.Pin.OUT)
pin_D2	=	machine.Pin(4,machine.Pin.OUT)
pin_D3	=	machine.Pin(0,machine.Pin.OUT)
pin_D4	=	machine.Pin(2,machine.Pin.OUT)
pin_D5	=	machine.Pin(14,machine.Pin.OUT)

#	INPUT	PIN	-	Button
button	=	machine.Pin(12,	machine.Pin.IN)

#	Interrupt	Callback	function
def	mycallback(p):
	global	IsButtonPressed	
	IsButtonPressed	=	not	IsButtonPressed

#	Interrupt
button.irq(trigger=machine.Pin.IRQ_FALLING,	handler=mycallback)	

IsButtonPressed		=	False
lightsOn	=	False






pin_D0.off()
pin_D1.off()
pin_D2.off()
pin_D3.off()
pin_D4.off()
pin_D5.off()

					

#	Toggle	function	which	toggles	LED	when	PIN	and	sleep	time	are	given	
def	ToggleGivenPin(pin,	toggleDelay):
				time.sleep(toggleDelay)
				pin.on()
				time.sleep(toggleDelay)
				pin.off()
				print(button.value())


sleepTime	=	0.5				


while	True:

	while	IsButtonPressed:
		if	IsButtonPressed:			
			ToggleGivenPin(pin_D0,	sleepTime)			
		else:
			sleepTime	=	0.5	
			break

		if	IsButtonPressed:
			ToggleGivenPin(pin_D1,	sleepTime)			
		else:
			sleepTime	=	0.5	
			break
		
		if	IsButtonPressed:
			ToggleGivenPin(pin_D2,	sleepTime)			
		else:
			sleepTime	=	0.5	
			break	
				
		if	IsButtonPressed:
			ToggleGivenPin(pin_D3,	sleepTime)			
		else:
			sleepTime	=	0.5	
			break
		
		if	IsButtonPressed:
			ToggleGivenPin(pin_D4,	sleepTime)			
		else:
			sleepTime	=	0.5	
			break
		
		if	IsButtonPressed:
			ToggleGivenPin(pin_D5,	sleepTime)			
		else:
			sleepTime	=	0.5	
			break	


		if	sleepTime	>	0.1	:
			sleepTime	=	sleepTime	-	0.1
		else:
			sleepTime	=	0.5

			
			
#	Pin	mappings
#	D0	->	GPIO16
#	D1	->	GPIO5
#	D2	->	GPIO4
#	D3	->	GPIO0
#	D4	->	GPIO2
#	D5	->	GPIO14
