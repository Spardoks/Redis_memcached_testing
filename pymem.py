from time import sleep

from pymemcache.client import base as memcache

mc = memcache.Client('127.0.0.1:11211')

should_expired_mem = {'key1': 'value1', 'key2': 'value2'}
should_saved_mem = {'key3': 'value3'}

for key, value in should_expired_mem.items():
  print("Add expired 5s " + key)
  mc.set(key, value, 5)
  value_got = mc.get(key)
  print("Value got after adding ", end='')
  print(value_got)
print()
for key, value in should_saved_mem.items():
  print("Add not_expired " + key)
  mc.set(key, value)
  value_got = mc.get(key)
  print("Value got after adding ", end='')
  print(value_got)
  
print("\nSleep 5s\n")
sleep(5)

for key in should_expired_mem:
  print("Get expired " + key)
  value_got = mc.get(key)
  print("Value got after 5s ", end='')
  print(value_got)
print()
for key in should_saved_mem:
  print("Get not_expired " + key)
  value_got = mc.get(key)
  print("Value got after 5s ", end='')
  print(value_got)
