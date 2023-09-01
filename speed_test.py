import speedtest

def run_speed_test():
    # Initialize speedtest
    st = speedtest.Speedtest()

    # Get best server to run the test
    st.get_best_server()
    
    # Perform download and upload speed tests
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    
    # Get ping (latency)
    ping = st.results.ping
    
    # Print the results
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")

# Run the speed test
if __name__ == '__main__':
    run_speed_test()
