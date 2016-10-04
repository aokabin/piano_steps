import RPi.GPIO as GPIO
import pygame.mixer
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # mid_c
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # mid_d
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # mid_e
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # mid_f
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # mid_g
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # hi_a
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # hi_b

delay_time = 0.5 # second

pygame.init()
pygame.mixer.set_num_channels(8)

mid_c = pygame.mixer.Sound("mid_c.wav")
mid_c_lock_time = 0
mid_c_free = True
# mid_d = pygame.mixer.Sound("mid_d.wav")
# mid_d_lock_time = 0
# mid_e = pygame.mixer.Sound("mid_e.wav")
# mid_e_lock_time = 0
# mid_f = pygame.mixer.Sound("mid_f.wav")
# mid_f_lock_time = 0
# mid_g = pygame.mixer.Sound("mid_g.wav")
# mid_g_lock_time = 0
# hi_a = pygame.mixer.Sound("hi_a.wav")
# hi_a_lock_time = 0
# hi_b = pygame.mixer.Sound("hi_b.wav")
# hi_b_lock_time = 0

start_time = time.time()
end_time = time.time()

# def timer_decrement():
#   if mid_c_lock_time > 0:
#     mid_c_lock_time -= delta_time()
#   else
#     mid_c_lock_time = 0

def delta_time():
  end_time = time.time()
  delta = end_time - start_time
  start_time = end_time
  return delta

try:
  while True:
    delta = delta_time() # 前回のループからの経過時間

    if mid_c_lock_time > 0:
      mid_c_lock_time -= delta
      if mid_c_lock_time < 0:
        mid_c_lock_time = 0

    if GPIO.input(2) == 0 and mid_c_lock_time <= 0:
      mid_c_free = True

    if (GPIO.input(2) == 1 && mid_c_free):
      mid_c_free = False
      mid_c_lock_time = delay_time
      mid_c.play()

    # if (GPIO.input(3) == 1 && mid_d_lock_time <= 0):
    #   mid_d()
    # if (GPIO.input(4) == 1 && mid_e_lock_time <= 0):
    #   mid_e()
    # if (GPIO.input(14) == 1 && mid_f_lock_time <= 0):
    #   mid_f()
    # if (GPIO.input(15) == 1 && mid_g_lock_time <= 0):
    #   mid_g()
    # if (GPIO.input(17) == 1 && hi_a_lock_time <= 0):
    #   hi_a()
    # if (GPIO.input(18) == 1 && hi_b_lock_time <= 0):
    #   hi_b()

