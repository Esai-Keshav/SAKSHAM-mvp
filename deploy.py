hook = "https://api.render.com/deploy/srv-d6jcadbuibrs73aifsdg?key=hGMzyQEAPv4"

import urllib.request


def trigger_deploy():
    try:
        with urllib.request.urlopen(hook, timeout=10) as response:
            return response.getcode()
    except Exception as e:
        print(f"Error: {e}")
        return 500


if __name__ == "__main__":
    print(trigger_deploy())
