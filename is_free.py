"""
MIT License

Copyright (c) 2020 ZhangWenjie <https://github.com/myxxxsquared>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import ipaddress
import pickle
import argparse
import socket
import traceback


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("hostname_or_ip", nargs="+")
    args = parser.parse_args()

    free_list = pickle.load(open("addrs.pkl", "rb"))

    hostname_or_ip = args.hostname_or_ip

    for x in hostname_or_ip:
        addr = None
        is_hst = False
        try:
            addr = ipaddress.ip_address(x)
        except ValueError:
            pass

        if not addr:
            try:
                addr = socket.gethostbyname(x)
                addr = ipaddress.ip_address(addr)
                is_hst = True
            except socket.gaierror:
                pass

        if not addr:
            print(f"{x}: FAILED!")
        else:
            in_free = False
            for y in free_list:
                if addr in y:
                    in_free = True
                    break
            print(
                f"{x}: {str(addr) + ' ' if is_hst else ''}{'FREE' if in_free else 'NONFREE'}"
            )


if __name__ == "__main__":
    main()
