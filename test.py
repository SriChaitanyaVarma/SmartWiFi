from scanner.wifi_scanner import scan_wifi
from scanner.parser import parse_wifi_data

from analytics.channel_analyzer import analyze_channels
from analytics.recommendation_engine import recommend_channel

raw = scan_wifi()

networks = parse_wifi_data(raw)

analysis = analyze_channels(networks)

recommendation = recommend_channel(analysis)

print("\nCHANNEL ANALYSIS")
print(analysis)

print("\nRECOMMENDATION")
print(recommendation)