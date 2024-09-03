import psutil
import time

def get_network_usage():
    # Get the network statistics
    net_io = psutil.net_io_counters()

    # Return the bytes sent and receivbed
    return net_io.bytes_sent, net_io.bytes_recv

def convert_to_mbps(bytes_amount):
    # Convert bytes to megabits
    return(bytes_amount * 8) /(1024*1024)

def monitor_bandwidth(interval = 1):
    # Intial values for bytes sent and received
    last_sent, last_recv = get_network_usage()

    while True:
        # Wait for the interval period
        time.sleep(interval)

        # Get new values for bytes sent and received
        current_sent, current_recv = get_network_usage()

        # Calculate the bandwidth usage
        sent_rate = convert_to_mbps(current_sent - last_sent)/ interval
        recv_rate = convert_to_mbps(current_recv - last_recv)/ interval

        # UPdate the last sent and received values
        last_sent, last_recv = current_sent, current_recv

        # Print the bandwidth usage
        print(f"Upload: {sent_rate:.2f} Mbps, Download: {recv_rate:.2f} Mbps")

if __name__ == "__main__":
    monitor_bandwidth()