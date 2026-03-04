hook = "https://api.render.com/deploy/srv-d6jcadbuibrs73aifsdg?key=hGMzyQEAPv4"

import urllib3


def trigger_deploy():
    http = urllib3.PoolManager()
    try:
        response = http.request("GET", hook, timeout=10.0)
        return response.status
    except Exception as e:
        print(f"Error: {e}")
        return 500


if __name__ == "__main__":
    print(trigger_deploy())
