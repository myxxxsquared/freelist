# freelist
Check whether a host is in the free list of CERNET

## Usage

### Update free list from its.pku.edu.cn

```sh
python download_freelist.py
```

### Query a hostname or IP address

```sh
> python is_free.py www.baidu.com github.com 162.105.78.56
www.baidu.com: 182.61.200.6 FREE
github.com: 192.30.255.112 NONFREE
162.105.78.56: FREE
```
