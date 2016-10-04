import RPi.GPIO as GPIO
import pygame.mixer
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # mid_c
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # mid_d
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # mid_e
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # mid_f
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # mid_g
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # hi_a
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # hi_b

delay_time = 0.1 # second

pygame.init()
pygame.mixer.set_num_channels(100)

mid_c = pygame.mixer.Sound("mid_c.wav")
mid_c_lock_time = 0
mid_c_free = True
mid_d = pygame.mixer.Sound("mid_d.wav")
mid_d_lock_time = 0
mid_d_free = True
mid_e = pygame.mixer.Sound("mid_e.wav")
mid_e_lock_time = 0
mid_e_free = True
mid_f = pygame.mixer.Sound("mid_f.wav")
mid_f_lock_time = 0
mid_f_free = True
mid_g = pygame.mixer.Sound("mid_g.wav")
mid_g_lock_time = 0
mid_g_free = True
hi_a = pygame.mixer.Sound("hi_a.wav")
hi_a_lock_time = 0
hi_a_free = True
hi_b = pygame.mixer.Sound("hi_b.wav")
hi_b_lock_time = 0
hi_b_free = True

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

    # mid c
    if mid_c_lock_time > 0:
      mid_c_lock_time -= delta
      if mid_c_lock_time < 0:
        mid_c_lock_time = 0

    if GPIO.input(27) == 0 and mid_c_lock_time <= 0:
      mid_c_free = True

    if (GPIO.input(27) == 1 and mid_c_free):
      mid_c_free = False
      mid_c_lock_time = delay_time
      mid_c.play()

    # mid d
    if mid_d_lock_time > 0:
      mid_d_lock_time -= delta
      if mid_d_lock_time < 0:
        mid_d_lock_time = 0

    if GPIO.input(22) == 0 and mid_d_lock_time <= 0:
      mid_d_free = True

    if (GPIO.input(22) == 1 and mid_d_free):
      mid_d_free = False
      mid_d_lock_time = delay_time
      mid_d.play()

    # mid e
    if mid_e_lock_time > 0:
      mid_e_lock_time -= delta
      if mid_e_lock_time < 0:
        mid_e_lock_time = 0

    if GPIO.input(4) == 0 and mid_e_lock_time <= 0:
      mid_e_free = True

    if (GPIO.input(4) == 1 and mid_e_free):
      mid_e_free = False
      mid_e_lock_time = delay_time
      mid_e.play()

    #mid f
    if mid_f_lock_time > 0:
      mid_f_lock_time -= delta
      if mid_f_lock_time < 0:
        mid_f_lock_time = 0

    if GPIO.input(23) == 0 and mid_f_lock_time <= 0:
      mid_f_free = True

    if (GPIO.input(23) == 1 and mid_f_free):
      mid_f_free = False
      mid_f_lock_time = delay_time
      mid_f.play()

    # mid g
    if mid_g_lock_time > 0:
      mid_g_lock_time -= delta
      if mid_g_lock_time < 0:
        mid_g_lock_time = 0

    if GPIO.input(24) == 0 and mid_g_lock_time <= 0:
      mid_g_free = True

    if (GPIO.input(24) == 1 and mid_g_free):
      mid_g_free = False
      mid_g_lock_time = delay_time
      mid_g.play()

    # hi a
    if hi_a_lock_time > 0:
      hi_a_lock_time -= delta
      if hi_a_lock_time < 0:
        hi_a_lock_time = 0

    if GPIO.input(17) == 0 and hi_a_lock_time <= 0:
      hi_a_free = True

    if (GPIO.input(17) == 1 and hi_a_free):
      hi_a_free = False
      hi_a_lock_time = delay_time
      hi_a.play()

    # hi b
    if hi_b_lock_time > 0:
      hi_b_lock_time -= delta
      if hi_b_lock_time < 0:
        hi_b_lock_time = 0

    if GPIO.input(18) == 0 and hi_b_lock_time <= 0:
      hi_b_free = True

    if (GPIO.input(18) == 1 and hi_b_free):
      hi_b_free = False
      hi_b_lock_time = delay_time
      hi_b.play()

except KeyboardInterrupt:
  GPIO.cleanup()
  pass

