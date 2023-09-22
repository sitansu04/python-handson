import time
import redis
from redis.sentinel import Sentinel

# Define Sentinel Configuration
sentinel = Sentinel([
    ('localhost', 26379),  # Sentinel instance 1
    ('localhost', 26380),  # Sentinel instance 2
    ('localhost', 26381)   # Sentinel instance 3
], socket_timeout=0.1)

# Get the Master Connection
master = sentinel.master_for('mymaster', socket_timeout=0.1)

# Get the Slave Connection
slave = sentinel.slave_for('mymaster', socket_timeout=0.1)

# Perform Redis Operations on the Master
print("Setting 'my_key' on the master...")
master.set('my_key', 'Hello, Redis Master!')

# Retrieve Data from the Slave
value = slave.get('my_key')
print(f"Value from the slave: {value.decode('utf-8')}")

# Simulate a Master Failure for Testing Failover
print("Simulating a master failure...")
time.sleep(10)  # Simulate a 10-second delay for failover to occur

# After failover, the slave should be promoted to master
new_master = sentinel.master_for('mymaster', socket_timeout=0.1)
print("Setting 'new_key' on the new master...")
new_master.set('new_key', 'This is the new master.')

# Retrieve Data from the New Master
new_value = new_master.get('new_key')
print(f"Value from the new master: {new_value.decode('utf-8')}")

# Clean up connections
master.connection_pool.disconnect()
slave.connection_pool.disconnect()
new_master.connection_pool.disconnect()
