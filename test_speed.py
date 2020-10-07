import speedtest
from datetime import datetime
import sys
import os


def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"], datetime.now()


def main():
    num_tests = 1

    # Get path to where this script sits. Access log file in same folder for use with VBscript that doesn't use relative paths.
    base_path = os.path.normpath(sys.argv[0]).rsplit("\\")[0]

    # write to csv
    with open(os.path.join(base_path, "log.csv"), "a") as f:
        # f.write("download,upload,ping\n")
        for i in range(num_tests):
            print("Running test #{}".format(i + 1))
            d, u, p, t = test()
            f.write("{},{},{},{}\n".format(d, u, p, t))


if __name__ == "__main__":
    main()
