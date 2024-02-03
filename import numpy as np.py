import numpy as np
import matplotlib.pyplot as plt

# Parameters
mu = 1
lambda_ = 0.95
T = 10000

# Initialize variables
max_thresholds = range(1, 10)
average_throughputs = []
packet_loss_rates = []
average_queuing_delays = []
average_system_times = []

for b in max_thresholds:
    queue = []
    packet_loss = 0
    total_packets = 0
    total_time_in_system = 0
    total_time_in_queue = 0

    # Start simulation
    for t in range(T):
        # Packet arrival
        if np.random.exponential() < lambda_:
            total_packets += 1
            if len(queue) < b:
                queue.append(t)
            else:
                packet_loss += 1

        # Packet departure
        if queue and np.random.exponential() < mu:
            arrival_time = queue.pop(0)
            total_time_in_system += t - arrival_time
            total_time_in_queue += max(0, t - arrival_time - 1/mu)

    # Calculate metrics
    average_throughputs.append((total_packets - packet_loss) / T)
    packet_loss_rates.append(packet_loss / total_packets)
    average_queuing_delays.append(total_time_in_queue / total_packets)
    average_system_times.append(total_time_in_system / total_packets)

# Plot metrics
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(max_thresholds, average_throughputs)
plt.title('Average Throughput')
plt.xlabel('Max Threshold')
plt.ylabel('Throughput (packets/sec)')

plt.subplot(2, 2, 2)
plt.plot(max_thresholds, packet_loss_rates)
plt.title('Packet Loss Rate')
plt.xlabel('Max Threshold')
plt.ylabel('Loss Rate')

plt.subplot(2, 2, 3)
plt.plot(max_thresholds, average_queuing_delays)
plt.title('Average Queuing Delay')
plt.xlabel('Max Threshold')
plt.ylabel('Delay (sec)')

plt.subplot(2, 2, 4)
plt.plot(max_thresholds, average_system_times)
plt.title('Average System Time')
plt.xlabel('Max Threshold')
plt.ylabel('System Time (sec)')

plt.tight_layout()
plt.show()
