# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
def f_to_c(f):
  c = (f - 32) * 5/9
  return c

f100_in_celsius = 100
print(f_to_c(f100_in_celsius))

def c_to_f(c):
  f = c*(9/5) +32
  return f


c0_to_fahrenheit = 0
print(c_to_f(c0_to_fahrenheit))

def get_force(mass, acceleration):
  return mass*acceleration

train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

c = 3*10**8
def get_energy(mass, c):
  return mass*c^2

bomb_energy = get_energy(bomb_mass, c)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration)*distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

