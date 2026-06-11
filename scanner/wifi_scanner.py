import subprocess


def scan_wifi():

    try:

        output = subprocess.check_output(
            "netsh wlan show networks mode=bssid",
            shell=True,
            text=True
        )

        return output

    except Exception as e:
        print("Error:", e)
        return ""