import RPi.GPIO as GPIO
import pygame.mixer
import time

MACHINE_ID = 1

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 

delay_time = 0.1 # second

pygame.init()
pygame.mixer.set_num_channels(100)

if MACHINE_ID == 1:
  s1 = pygame.mixer.Sound("sounds/lowlowC.wav")
  s2 = pygame.mixer.Sound("sounds/lowlowD.wav")
  s3 = pygame.mixer.Sound("sounds/lowlowE.wav")
  s4 = pygame.mixer.Sound("sounds/lowlowF.wav")
  s5 = pygame.mixer.Sound("sounds/lowlowG.wav")
  s6 = pygame.mixer.Sound("sounds/lowA.wav")
  s7 = pygame.mixer.Sound("sounds/lowB.wav")
  s8 = pygame.mixer.Sound("sounds/lowC.wav")
  s9 = pygame.mixer.Sound("sounds/lowD.wav")
  s10 = pygame.mixer.Sound("sounds/lowE.wav")
  s11 = pygame.mixer.Sound("sounds/lowF.wav")
  s12 = pygame.mixer.Sound("sounds/lowG.wav")
  s13 = pygame.mixer.Sound("sounds/midA.wav")
  s14 = pygame.mixer.Sound("sounds/midB.wav")
  s15 = pygame.mixer.Sound("sounds/midC.wav")

else :
  s1 = pygame.mixer.Sound("sounds/midD.wav")
  s2 = pygame.mixer.Sound("sounds/midE.wav")
  s3 = pygame.mixer.Sound("sounds/midF.wav")
  s4 = pygame.mixer.Sound("sounds/midG.wav")
  s5 = pygame.mixer.Sound("sounds/hiA.wav")
  s6 = pygame.mixer.Sound("sounds/hiB.wav")
  s7 = pygame.mixer.Sound("sounds/hiC.wav")
  s8 = pygame.mixer.Sound("sounds/hiD.wav")
  s9 = pygame.mixer.Sound("sounds/hiE.wav")
  s10 = pygame.mixer.Sound("sounds/hiF.wav")
  s11 = pygame.mixer.Sound("sounds/hiG.wav")
  s12 = pygame.mixer.Sound("sounds/hihiA.wav")
  s13 = pygame.mixer.Sound("sounds/hihiB.wav")
  s14 = pygame.mixer.Sound("sounds/hihiC.wav")
  s15 = pygame.mixer.Sound("sounds/hihiD.wav")

s1_lock_time = 0
s1_free = True
s2_lock_time = 0
s2_free = True
s3_lock_time = 0
s3_free = True
s4_lock_time = 0
s4_free = True
s5_lock_time = 0
s5_free = True
s6_lock_time = 0
s6_free = True
s7_lock_time = 0
s7_free = True
s8_lock_time = 0
s8_free = True
s9_lock_time = 0
s9_free = True
s10_lock_time = 0
s10_free = True
s11_lock_time = 0
s11_free = True
s12_lock_time = 0
s12_free = True
s13_lock_time = 0
s13_free = True
s14_lock_time = 0
s14_free = True
s15_lock_time = 0
s15_free = True
s16_lock_time = 0
s16_free = True

start_time = time.time()
end_time = time.time()

def delta_time():
  global start_time
  global end_time
  end_time = time.time()
  delta = end_time - start_time
  start_time = end_time
  return delta

try:
  while True:
    delta = delta_time()

    if s1_lock_time > 0:
      s1_lock_time -= delta
      if s1_lock_time < 0:
        s1_lock_time = 0

    if GPIO.input(17) == 0 and s1_lock_time <= 0:
      s1_free = True

    if (GPIO.input(17) == 1 and s1_free):
      s1_free = False
      s1_lock_time = delay_time
      s1.play()

    if s2_lock_time > 0:
      s2_lock_time -= delta
      if s2_lock_time < 0:
        s2_lock_time = 0

    if GPIO.input(27) == 0 and s2_lock_time <= 0:
      s2_free = True

    if (GPIO.input(27) == 1 and s2_free):
      s2_free = False
      s2_lock_time = delay_time
      s2.play()

    if s3_lock_time > 0:
      s3_lock_time -= delta
      if s3_lock_time < 0:
        s3_lock_time = 0

    if GPIO.input(22) == 0 and s3_lock_time <= 0:
      s3_free = True

    if (GPIO.input(22) == 1 and s3_free):
      s3_free = False
      s3_lock_time = delay_time
      s3.play()

    if s4_lock_time > 0:
      s4_lock_time -= delta
      if s4_lock_time < 0:
        s4_lock_time = 0

    if GPIO.input(5) == 0 and s4_lock_time <= 0:
      s4_free = True

    if (GPIO.input(5) == 1 and s4_free):
      s4_free = False
      s4_lock_time = delay_time
      s4.play()

    if s5_lock_time > 0:
      s5_lock_time -= delta
      if s5_lock_time < 0:
        s5_lock_time = 0

    if GPIO.input(6) == 0 and s5_lock_time <= 0:
      s5_free = True

    if (GPIO.input(6) == 1 and s5_free):
      s5_free = False
      s5_lock_time = delay_time
      s5.play()

    if s6_lock_time > 0:
      s6_lock_time -= delta
      if s6_lock_time < 0:
        s6_lock_time = 0

    if GPIO.input(13) == 0 and s6_lock_time <= 0:
      s6_free = True

    if (GPIO.input(13) == 1 and s6_free):
      s6_free = False
      s6_lock_time = delay_time
      s6.play()

    if s7_lock_time > 0:
      s7_lock_time -= delta
      if s7_lock_time < 0:
        s7_lock_time = 0

    if GPIO.input(19) == 0 and s7_lock_time <= 0:
      s7_free = True

    if (GPIO.input(19) == 1 and s7_free):
      s7_free = False
      s7_lock_time = delay_time
      s7.play()

    if s8_lock_time > 0:
      s8_lock_time -= delta
      if s8_lock_time < 0:
        s8_lock_time = 0

    if GPIO.input(26) == 0 and s8_lock_time <= 0:
      s8_free = True

    if (GPIO.input(26) == 1 and s8_free):
      s8_free = False
      s8_lock_time = delay_time
      s8.play()

    if s9_lock_time > 0:
      s9_lock_time -= delta
      if s9_lock_time < 0:
        s9_lock_time = 0

    if GPIO.input(18) == 0 and s9_lock_time <= 0:
      s9_free = True

    if (GPIO.input(18) == 1 and s9_free):
      s9_free = False
      s9_lock_time = delay_time
      s9.play()

    if s10_lock_time > 0:
      s10_lock_time -= delta
      if s10_lock_time < 0:
        s10_lock_time = 0

    if GPIO.input(23) == 0 and s10_lock_time <= 0:
      s10_free = True

    if (GPIO.input(23) == 1 and s10_free):
      s10_free = False
      s10_lock_time = delay_time
      s10.play()

    if s11_lock_time > 0:
      s11_lock_time -= delta
      if s11_lock_time < 0:
        s11_lock_time = 0

    if GPIO.input(24) == 0 and s11_lock_time <= 0:
      s11_free = True

    if (GPIO.input(24) == 1 and s11_free):
      s11_free = False
      s11_lock_time = delay_time
      s11.play()

    if s12_lock_time > 0:
      s12_lock_time -= delta
      if s12_lock_time < 0:
        s12_lock_time = 0

    if GPIO.input(25) == 0 and s12_lock_time <= 0:
      s12_free = True

    if (GPIO.input(25) == 1 and s12_free):
      s12_free = False
      s12_lock_time = delay_time
      s12.play()

    if s13_lock_time > 0:
      s13_lock_time -= delta
      if s13_lock_time < 0:
        s13_lock_time = 0

    if GPIO.input(12) == 0 and s13_lock_time <= 0:
      s13_free = True

    if (GPIO.input(12) == 1 and s13_free):
      s13_free = False
      s13_lock_time = delay_time
      s13.play()

    if s14_lock_time > 0:
      s14_lock_time -= delta
      if s14_lock_time < 0:
        s14_lock_time = 0

    if GPIO.input(16) == 0 and s14_lock_time <= 0:
      s14_free = True

    if (GPIO.input(16) == 1 and s14_free):
      s14_free = False
      s14_lock_time = delay_time
      s14.play()

    if s15_lock_time > 0:
      s15_lock_time -= delta
      if s15_lock_time < 0:
        s15_lock_time = 0

    if GPIO.input(20) == 0 and s15_lock_time <= 0:
      s15_free = True

    if (GPIO.input(20) == 1 and s15_free):
      s15_free = False
      s15_lock_time = delay_time
      s15.play()

except KeyboardInterrupt:
  GPIO.cleanup()
  pass

