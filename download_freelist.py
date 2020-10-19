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

import requests
import ipaddress
import pickle

URL = "https://its.pku.edu.cn/oper/liebiao.jsp"

def main():
    response = requests.get(URL)
    response.raise_for_status()
    response = response.text
    beginloc = response.index("<pre>")
    endloc = response.index("</pre>")
    response = response[beginloc+5:endloc]
    
    response = response.split('\n')
    response = iter(response)
    while True:
        if next(response).startswith('-'):
            break

    addrs = set()
    for line in response:
        line = line.strip()
        if not line:
            continue
        line = [x for x in line.split(' ') if x]
        ip, host_mask, network_mask = line
        addr = ipaddress.ip_network(f"{ip}/{network_mask}")
        addrs.add(addr)
    
    with open('addrs.pkl', 'wb') as fout:
        pickle.dump(addrs, fout)

if __name__ == "__main__":
    main()
