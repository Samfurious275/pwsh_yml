import subprocess
import sys

# Function to check if user exists
def user_exists(username):
    try:
        subprocess.check_output(["getent", "passwd", username])
        return True
    except subprocess.CalledProcessError:
        return False

# Function to run commands with sudo
def run_command(command):
    full_command = ["sudo"] + command
    print(f"Running: {' '.join(full_command)}")
    result = subprocess.run(full_command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(1)
    return result.stdout

# Create user if not exists
username = "JohnDoe"
if not user_exists(username):
    print(f"Creating user {username}...")
    run_command(["useradd", "-m", "-s", "/bin/bash", username])
else:
    print(f"User {username} already exists.")

# Set password
print(f"Setting password for {username}...")
password_process = subprocess.Popen(
    ["sudo", "chpasswd"],
    stdin=subprocess.PIPE,
    text=True
)
password_process.communicate(f"{username}:P@ssw0rd")

# Add to sudo group
print(f"Adding {username} to sudo group...")
run_command(["usermod", "-aG", "sudo", username])

# Export users to CSV
print("Exporting users to CSV...")
with open("/home/samrider/users.csv", "w") as f:
    f.write("Name,Enabled\n")
    passwd_data = subprocess.check_output(["cut", "-d:", "-f1", "/etc/passwd"]).decode()
    for line in passwd_data.splitlines():
        f.write(f"{line},Enabled\n")

print("✅ User setup completed.")
