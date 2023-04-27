import requests
import threading

def check_proxy(proxy):
    try:
        response = requests.get('https://www.google.com', proxies={'socks5': proxy}, timeout=5)
        if response.status_code == 200:
            print(f'[+] {proxy} is working')
    except:
        pass

def main():
    with open('proxy.txt', 'r') as f:
        proxies = f.read().splitlines()

    threads = []
    for proxy in proxies:
        t = threading.Thread(target=check_proxy, args=(proxy,))
        threads.append(t)
        t.start()

        # limit number of threads to 10
        if len(threads) >= 10:
            for t in threads:
                t.join()
            threads = []

    # join remaining threads
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()

with open('proxy.txt', 'r') as f:
    lines = f.readlines()

with open('proxy.txt', 'w') as f:
    for line in lines:
        if not line.startswith('socks5://'):
            line = 'socks5://' + line
        f.write(line)
