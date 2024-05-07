import datetime

def main():
    # Print a message to indicate the script is running
    print("Hello from hello.py!")

    # Get the current date
    current_date = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2))).strftime("%Y-%m-%d")

    # Write the current date to date_keeper.txt
    with open("Monitoring_observations/date_keeper.txt", "a") as file:
        file.write(f"Date in Amsterdam: {current_date}\n")
    print("Date Recorded!")

if __name__ == "__main__":
    main()
