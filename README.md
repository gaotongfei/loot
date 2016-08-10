# loot

loot is a command line tool that helps you work with github without pain, all work can be done in terminal — Edit

Now `loot` only supports downloading gist in terminal. More features are working in process

## Install

`pip install loot`

## Usage


use `loot --help` to check supported commands and options

commands
===

* **gist**

`loot gist -u gaotongfei`, it will print all the public gists' information user gaotongfei created

`loot gist -u gaotongfei -k request`

```
[{'files': [{'raw_url': 'https://gist.githubusercontent.com/gaotongfei/2e37d97e93619c07d0b2910e3c4034e5/raw/2bb02fe904e5051189b536391f0bc182562c41df/request_with_proxy.py', 'file_name': 'request_with_proxy.py', 'language': 'Python'}], 'id': '2e37d97e93619c07d0b2910e3c4034e5', 'description': 'request with proxy'}, {'files': [{'raw_url': 'https://gist.githubusercontent.com/gaotongfei/5415382b696d75247c0b/raw/deecf9ac8e20e893487cb33caf3e4875eda645b8/print_cookies.py', 'file_name': 'print_cookies.py', 'language': 'Python'}], 'id': '5415382b696d75247c0b', 'description': 'Using urllib2 and cookielib to print cookies from GET request'}, {'files': [{'raw_url': 'https://gist.githubusercontent.com/gaotongfei/66b754c2688b350d5ed9/raw/7960ace7513cbc4c3ac8979008ff21beb3d71abf/PyTorStemPrivoxy.py', 'file_name': 'PyTorStemPrivoxy.py', 'language': 'Python'}, {'raw_url': 'https://gist.githubusercontent.com/gaotongfei/66b754c2688b350d5ed9/raw/73326a533c451f3ad9b0e0ab689747460f53babc/PyTorStemPrivoxy.md', 'file_name': 'PyTorStemPrivoxy.md', 'language': 'Markdown'}], 'id': '66b754c2688b350d5ed9', 'description': 'Python script to connect to Tor via Stem and Privoxy, requesting a new connection (hence a new IP as well) as desired.'}]
```
It prints all public gists' information whose description or filename contains `request`

`loot gist -u gaotongfei -k request -p` it will pretty print the result showed above

* **clone**

`loot clone 2e37d97e93619c07d0b2910e3c4034e5`, it will download the gist files in current directory by default, you can use `--dir` or `-d` to specify downloading directory
