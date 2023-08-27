##############################################################################################
#                                                                                           #
# INSTRUCTIONS TO RUN THE SCRIPT:                                                           #
# STEP ZERO                                                                                 #
# MUTE YOUR SPEAKERS, SAVE ALL OF YOUR WORK                                                 #
# YOU CAN USE THIS ON A POOR LAPTOP IN THE CORNER                                           #
# IT JUST USE MANY RAMS SO START WITH LONGER DURATION AND IT WILL BE BETTER                 # 
#       FULL COMMENTS BELOW                                                                 #
#      BUT YOU CAN RUN THE SCRIPT RIGHT NOW IN CMD OR TERMINAL OR VSCODE (I RECOMMEND VSCODE)#
#                                 VSCODE IF YOU WANT  https://code.visualstudio.com/download #
# 1. Prerequisites:                                                                         #
#    - Ensure you have Python installed on your system. You can download it from            #
#      https://www.python.org/downloads/                                                    #
#                                                                                           #
# 2. Download the Script:                                                                   #
#    - Download the script file and save it with a '.py' extension, e.g.,                   #
#      'youtube_viewbot.py'.                                                                #
#                                                                                           #
# 3. Open a Terminal or Command Prompt:                                                     #
#    - On Windows, open the Command Prompt. On macOS or Linux, open the Terminal.           #
#                                                                                           #
# 4. Navigate to the Script's Directory:                                                    #
#    - Use 'cd' command to navigate to the script's directory, e.g.,                        #
#      'cd Downloads' (replace 'Downloads' with your directory).                            #
#                                                                                           #
# 5. Run the Script:                                                                        #
#    - Enter 'python youtube_viewbot.py' in the terminal. If you have                       #
#      multiple Python versions, use 'python3' instead.                                     #
#                                                                                           #
# 6. Follow the Prompts:                                                                    #
#    - The script will prompt you for inputs like YouTube video URL, views,                 #
#      view durations, etc. Follow the instructions.                                        #
#                                                                                           #
# 7. Read and Understand the Disclaimer:                                                    #
#    - Carefully read the disclaimer at the beginning of the script.                        #
#      Understand the ethical and legal implications of using the script.                   #
#                                                                                           #
# 8. Running the Script:                                                                    #
#    - If your inputs meet the conditions, the script will simulate viewing the             #
#      video using threads and loops, opening browser windows with autoplaying videos.      #
#      Note that this behavior may violate terms of service and guidelines.                 #
#                                                                                           #
# 9. Responsibility and Ethics:                                                             #
#    - Always use scripts responsibly and ethically. Unauthorized use                       #
#      of the script for automating interactions on platforms can have legal                #
#      and ethical consequences.                                                            #
#                                                                                           #
# 10. Exiting the Script:                                                                   #
#     - You can exit the script anytime by pressing 'Ctrl + C' in the terminal.             #
#       Close any browser windows opened by the script.                                     #
#                                                                                           #
# DISCLAIMER: This script is for educational purposes only. Use it responsibly              #
# and respect the terms of service of platforms you interact with. The creators             #
# of this script do not endorse any unauthorized or unethical activities.                   #
#                                                                                           #
##############################################################################################


# Import necessary modules
import webbrowser  # Module to open URLs in web browser
import time  # Module for time-related functions
import threading  # Module for creating threads
import random  # Module for generating random numbers

                            # ANSI colour codes for terminal output
class Color:
    GREEN = '\033[92m'      # Green text color
    RED = '\033[91m'        # Red text color
    YELLOW = '\033[93m'     # Yellow text color
    CYAN = '\033[96m'       # Cyan text color
    END = '\033[0m'         # Reset text color to default

                            # Function to open autoplaying window
def open_autoplaying_window(url, view_duration):
                            # Open the URL in a new web browser window
    webbrowser.open_new(url)
    print(f"{Color.CYAN}Autoplaying window opened.{Color.END}")
                            # Wait for the specified view duration
    time.sleep(view_duration)
    print(f"{Color.CYAN}View duration completed.{Color.END}")
                            # Open the video URL in a new tab
    webbrowser.open_new_tab(user_video_url)
    print(f"{Color.CYAN}User video window opened.{Color.END}")
                            # Wait again for the view duration
    time.sleep(view_duration)
    print(f"{Color.GREEN}View duration completed.{Color.END}")

                            # User input
                            # Prompt user for their YouTube video URL
user_url = input(f"{Color.YELLOW}Enter your YouTube video URL (format: https://www.youtube.com/watch?v=VIDEO_ID): {Color.END}")
                            # Prompt user for the number of views, ensuring a minimum of 5
view_count = max(int(input(f"{Color.YELLOW}How many tabs (min 5)? (High numbers use many RAMs) {Color.END}")), 5)
                            # Prompt user for the minimum view duration, ensuring a minimum of 30 seconds
min_duration = max(int(input(f"{Color.GREEN}Enter the MINIMUM duration of view in seconds (minimum 30 seconds): {Color.END}")), 30)
                            # Prompt user for the maximum view duration, ensuring it's greater than or equal to the minimum
max_duration = max(int(input(f"{Color.RED}Enter the maximum duration of view in seconds: {Color.END}")), min_duration)
                            # Prompt user for the number of loops before opening the URL, ensuring a minimum of 5
loop_count_before_url = random.randint(5, 25)
# URL SAMPLE Check - Only use full urls, not shortened or playlists
# A user URL for an autoplaying video (Do not change or remove this line)
user_video_url = "https://www.youtube.com/watch?v=FQX_kMLjG-g&autoplay=1"

# THE CODE ABOVE SETS UP ALL OF THE CHECKS AND PROMPTS
# THE CODE BELOW RUNS THE SCRIPT 
# WATCH THE TERMINAL FOR THE OUTPUT
# HAPPY LUCK AND MANY VIEWS TO YOU

##############################################################################################
#                                                                                            #
# DISCLAIMER: This script is provided for educational and illustrative purposes only.        #
# The script demonstrates various programming concepts and should not be used for any        #
# unauthorized or unethical activities, including but not limited to artificially            #
# inflating views on videos, violating terms of service, or engaging in any form of          #
# automated behavior that may violate platform guidelines or applicable laws.                 #
#                                                                                            #
# The authors and creators of this script do not condone or promote any unauthorized or      #
# unethical use of this code. The script is distributed in the hope that it will be useful,   #
# but WITHOUT ANY WARRANTY, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED     #
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT.      #
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR    #
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT   #
# OF OR IN CONNECTION WITH THE SCRIPT OR THE USE OR OTHER DEALINGS IN THE SCRIPT.            #
#                                                                                            #
# It is your responsibility to understand and comply with the terms of service of any         #
# platform or service you interact with. Be sure to respect the rights and guidelines of     #
# content creators and platform providers. Use this script responsibly and ethically.        #
#                                                                                            #
##############################################################################################
if (
    user_url.startswith("https://www.youtube.com/watch?v=") and
    view_count >= 5 and
    min_duration >= 30 and
    max_duration >= min_duration and
    loop_count_before_url >= 5
):                          # Check if user inputs meet the specified conditions
    print(f"{Color.GREEN}URL verified and ready to open in 1 to 30 seconds.{Color.END}")  # Indicate that the URL is ready to open
    time.sleep(random.randint(1, 30))  # Introduce randomness by sleeping for a random time between 1 to 30 seconds
    
    print(f"""{Color.CYAN}
THE VIEWBOT IS STARTING
{Color.END}""")             # Print an ASCII title indicating the script is starting
    
    loop_count = 0          # Initialize the loop counter
    while loop_count < loop_count_before_url:  # Run loops before opening the user's URL
        print(f"\n{Color.CYAN}Starting loop {loop_count + 1}{Color.END}")  # Indicate the start of a loop
        for _ in range(view_count):  # Iterate for each view
                            # Create a thread to open an autoplaying window
            view_duration = random.randint(min_duration, max_duration)
            thread = threading.Thread(target=open_autoplaying_window, args=(user_url, view_duration))
            print(f"{Color.CYAN}Thread {thread.name} started for autoplaying video.{Color.END}")
                            # Start the thread to simulate views
            thread.start()

                            # Sleep for a random duration within the specified range
        sleep_duration = random.randint(min_duration, max_duration)
        print(f"{Color.YELLOW}Waiting for {sleep_duration} seconds between loops...{Color.END}")
        for _ in range(sleep_duration):  # Display progress bar
            print(f"{Color.YELLOW}[{'#' * (_ + 1):{sleep_duration + 1}}] {(_ + 1) / sleep_duration * 100:.2f}%\r", end="")
            time.sleep(1)
        print()             # Print a newline to clear progress bar
        loop_count += 1     # Increment the loop counter
        print(f"""{Color.GREEN}
Loop {loop_count} completed.{Color.END}
{Color.CYAN}{'='*50}{Color.END}""")  # Indicate the completion of a loop
        
    print(f"{Color.GREEN}testing {loop_count_before_url} loops: {user_url}{Color.END}")  # Indicate that the user's URL is being opened
                            # Open the user's URL in a new tab
    webbrowser.open_new_tab(user_url)
                            # Sleep for a random duration within the specified range
    sleep_duration = random.randint(min_duration, max_duration)
    print(f"{Color.YELLOW}Waiting for {sleep_duration} seconds before continuous loops...{Color.END}")
    time.sleep(sleep_duration)
    
    while True:             # Infinite loop for continuous execution
        print(f"\n{Color.CYAN}Starting loop {loop_count + 1}{Color.END}")  # Indicate the start of a loop
        for _ in range(view_count):  # Iterate for each view
                            # Create a thread to open an autoplaying window
            thread = threading.Thread(target=open_autoplaying_window, args=(user_url, view_duration))
            print(f"{Color.CYAN}Thread {thread.name} started for autoplaying video.{Color.END}")
                            # Start the thread to simulate views
            thread.start()

                            # Sleep for a random duration within the specified range
        sleep_duration = random.randint(min_duration, max_duration)
        print(f"{Color.YELLOW}Waiting for {sleep_duration} seconds between continuous loops...{Color.END}")
        time.sleep(sleep_duration)
        loop_count += 1     # Increment the loop counter
        print(f"""{Color.GREEN}
Loop {loop_count} completed.{Color.END}
{Color.CYAN}{'='*50}{Color.END}""")  # Indicate the completion of a loop

else:                       # If user inputs do not meet the specified conditions
    print(f"{Color.RED}Invalid inputs. The code will not run.{Color.END}")  # Indicate that the code will not run due to invalid inputs










































































































##############################################################################################
#                                                                                            #
# DISCLAIMER: This script is provided for educational and illustrative purposes only.        #
# The script demonstrates various programming concepts and should not be used for any        #
# unauthorized or unethical activities, including but not limited to artificially            #
# inflating views on videos, violating terms of service, or engaging in any form of          #
# automated behavior that may violate platform guidelines or applicable laws.                 #
#                                                                                            #
# The authors and creators of this script do not condone or promote any unauthorized or      #
# unethical use of this code. The script is distributed in the hope that it will be useful,   #
# but WITHOUT ANY WARRANTY, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED     #
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT.      #
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR    #
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT   #
# OF OR IN CONNECTION WITH THE SCRIPT OR THE USE OR OTHER DEALINGS IN THE SCRIPT.            #
#                                                                                            #
# It is your responsibility to understand and comply with the terms of service of any         #
# platform or service you interact with. Be sure to respect the rights and guidelines of     #
# content creators and platform providers. Use this script responsibly and ethically.        #
#                                                                                            #
##############################################################################################
