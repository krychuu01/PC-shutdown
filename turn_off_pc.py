import subprocess
import msvcrt


def main():
    while True:
        try:
            minutes = int(input("Enter the number of minutes until the computer shuts down: "))
            break
        except ValueError as e:
            error_message = str(e)
            start_index = error_message.find("'") + 1
            end_index = error_message.find("'", start_index)
            invalid_input = error_message[start_index:end_index]
            print(f"Error! Wrong input: \"{invalid_input}\", try one more time.")

    command = f"shutdown -s -t {minutes * 60}"
    print(f"Computer will shut down in {minutes} minutes.")
    print("If you want to decline shutting down, press \"s\".")

    subprocess.Popen(command, shell=True)

    while True:
        if msvcrt.kbhit():
            char = msvcrt.getch().decode('utf-8').lower()
            if char == "s":
                subprocess.run(["shutdown", "/a"])
                print("Shutting down cancelled.")
                break


if __name__ == "__main__":
    main()
