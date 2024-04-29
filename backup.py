# # # import subprocess
# # # import webbrowser
# # # import pyautogui
# # # import time
# # #
# # # while True:
# # #     print("""
# # # ********options available:-********\n
# # #         ns - for network speed test
# # #         pg - for password generator
# # #         yt - for opening youtube
# # #         gn - for guess the numbergame
# # #         rps - for rock paper sissors game
# # #         wg - for weight converter
# # #         exit - to exit
# # #         secured_commands - to see some special commands\n""")
# # #
# # #     command = input("Enter your input: ")
# # #
# # #     if command == "pg":
# # #         subprocess.run(['python', 'pass_gen.py'])
# # #
# # #     elif command == "secured commands":
# # #         passwd = input("pls enter password to see secured commands: ")
# # #         pass_correct = "terminate"
# # #         if passwd == pass_correct:
# # #             print("terminate by 5007")
# # #         else:
# # #             print("wrong password!!")
# # #
# # #     elif command == "gn":
# # #         subprocess.run(['python', 'guess_the_number.py'])
# # #
# # #     elif command == "rps":
# # #         subprocess.run(['python', 'rps_game.py'])
# # #
# # #     elif command == "yt":
# # #         url = "https://www.youtube.com/"
# # #         webbrowser.open(url)
# # #         print("opening youtube")
# # #
# # #     elif command == "wg":
# # #         subprocess.run(['python', 'Weight_(LLB _to_Kg)convertor.py'])
# # #
# # #     elif command == "ns":
# # #         subprocess.run(['python', 'internet speed test.py'])
# # #
# # #     elif command == "terminate by 5007":
# # #         correct_password = "mayank007511"
# # #         password = input("please enter password to terminate the code: ")
# # #         if password == correct_password:
# # #             print("Position the cursor on the code...")
# # #             time.sleep(5)
# # #
# # #             print("code will be deleted in:")
# # #
# # #             seconds = 10
# # #
# # #             for i in range(seconds, 0, -1):
# # #                 print(i)
# # #                 time.sleep(1)
# # #
# # #             # simulate Ctrl + A
# # #             pyautogui.hotkey('ctrl', 'a')
# # #
# # #             # simulate Delete key
# # #             pyautogui.press('delete')
# # #
# # #             print("!!code deleted successfully!!")
# # #
# # #         else:
# # #             print("!!incorrect password!!\n")
# # #
# # #     elif command == "exit":
# # #         break
# # #
# # #     else:
# # #         print("""Invalid command
# # #         Try again""")
# # #
# # #     next_command = input("\nPress Enter to continue ")
# # #
# # # print("!!Thank You!!")
#
import subprocess
import webbrowser
import time
import os

while True:
    print("""
********options available:-********\n
        ns - for network speed test
        pg - for password generator
        yt - for opening youtube
        gn - for guess the numbergame
        rps - for rock paper sissors game
        wg - for weight converter
        exit - to exit
        secured_commands - to see some special commands\n""")

    command = input("Enter your input: ")

    if command == "pg":
        subprocess.run(['python', 'pass_gen.py'])

    elif command == "secured commands":
        passwd = input("pls enter password to see secured commands: ")
        pass_correct = "mayank059"
        if passwd == pass_correct:
            print("terminate by 5007")
        else:
            print("wrong password!!")

    elif command == "gn":
        subprocess.run(['python', 'guess_the_number.py'])

    elif command == "rps":
        subprocess.run(['python', 'rps_game.py'])

    elif command == "yt":
        url = "https://www.youtube.com/"
        webbrowser.open(url)
        print("opening youtube")

    elif command == "wg":
        subprocess.run(['python', 'Weight_(LLB _to_Kg)convertor.py'])

    elif command == "ns":
        subprocess.run(['python', 'internet speed test.py'])

    elif command == "terminate by 5007":
        correct_password = "mayank007511"
        password = input("please enter password to terminate the code: ")
        if password == correct_password:
            time.sleep(3)

            print("The file will be deleted in:")

            seconds = 10

            for i in range(seconds, 0, -1):
                print(i)
                time.sleep(1)

            file_path = "K:\mayank\coding\Mayank's Python programming folder\mayank_python_projects\my_file.py"

            try:

                os.remove(file_path)
                print(f"{file_path} has been deleted successfully.")
            except FileNotFoundError:
                print(f"{file_path} does not exist.")
            except PermissionError:
                print(f"You do not have permission to delete {file_path}.")
            except Exception as e:
                print(f"An error occurred while deleting {file_path}: {e}")

            print("!!code deleted successfully!!")

        else:
            print("!!incorrect password!!\n")

    elif command == "exit":
        break

    else:
        print("""Invalid command
        Try again""")

    next_command = input("\nPress Enter to continue ")

print("!!Thank You!!")
