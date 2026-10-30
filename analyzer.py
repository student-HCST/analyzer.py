def analyze_log_file(filename):

    total = 0
    info = 0
    warning = 0
    error = 0

    errors = []

    try:
        file = open(filename, "r")

        for line in file:
            total += 1

            if "INFO" in line:
                info += 1

            elif "WARNING" in line:
                warning += 1

            elif "ERROR" in line:
                error += 1
                errors.append(line.strip())

        file.close()

        print("\n===== LOG FILE ANALYSIS =====")
        print("Total Logs:", total)
        print("INFO Messages:", info)
        print("WARNING Messages:", warning)
        print("ERROR Messages:", error)

        print("\n===== ERROR DETAILS =====")

        for e in errors:
            print(e)

        # Save report
        report = open("report.txt", "w")

        report.write("LOG FILE ANALYSIS REPORT\n")
        report.write("------------------------\n")
        report.write("Total Logs: " + str(total) + "\n")
        report.write("INFO: " + str(info) + "\n")
        report.write("WARNING: " + str(warning) + "\n")
        report.write("ERROR: " + str(error) + "\n")

        report.write("\nERROR DETAILS:\n")

        for e in errors:
            report.write(e + "\n")

        report.close()

        print("\nReport saved successfully!")

    except FileNotFoundError:
        print("File not found!")


# Main Program
filename = input("Enter log file name: ")

analyze_log_file(filename)