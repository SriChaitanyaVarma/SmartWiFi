def parse_wifi_data(raw_data):

    networks = []
    current = {}

    for line in raw_data.split("\n"):

        line = line.strip()

        if line.startswith("SSID") and ":" in line:

            if current:
                networks.append(current)

            ssid = line.split(":", 1)[1].strip()

            current = {
                "ssid": ssid
            }

        elif line.startswith("BSSID"):

            current["bssid"] = line.split(":", 1)[1].strip()

        elif line.startswith("Signal"):

            signal = (
                line.split(":", 1)[1]
                .replace("%", "")
                .strip()
            )

            current["signal"] = int(signal)

        elif line.startswith("Channel"):

            print("RAW CHANNEL:", line)

            channel_text = line.split(":", 1)[1].strip()

            current["channel"] = int(
                channel_text.split()[0]
        )

        elif line.startswith("Band"):

            current["band"] = line.split(":", 1)[1].strip()

        elif line.startswith("Radio type"):

            current["radio_type"] = (
                line.split(":", 1)[1].strip()
            )

    required_fields = [
    "ssid",
    "signal",
    "channel",
    "radio_type"
    ]

    if all(field in current for field in required_fields):
        networks.append(current)

    return networks