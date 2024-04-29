import speedtest_cli

print("calculating your network speed please wait...\n")

s = speedtest_cli.Speedtest()

# Byte for conversation

bytes_num = 1048576

# Get download speed
dws = round(s.download() / bytes_num, 2)

# Get upload speed
ups = round(s.upload() / bytes_num, 2)

print(f'My download speed is: {dws} Mbps')
print(f'My upload speed is: {ups} Mbps')
