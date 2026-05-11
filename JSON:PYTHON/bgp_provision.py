import argparse
import requests
import sys


def main():
    parser = argparse.ArgumentParser(description="A tool to update network configs")

    parser.add_argument('--gurl', required=True, help="Destination API get url")
    parser.add_argument('--peer', required=True, help="IP of the BGP neighbor")
    parser.add_argument('--status', choices=['up','down'], default='down', \
                    required=True, help="The desired administrative state ")
    #In an actual radio env, url/ip would be the same potentially, as you'd pull/push to the same
    # added additional arg just for ability to test myself as i have no radios :(
    parser.add_argument('--purl', required=False, default='https://httpbin.org/post', \
                         help="Destination API post url" )

    args = parser.parse_args()

    print(f"[*] Initiating BGP Provisioning for Peer: {args.peer}")
    print(f"[*] Target State: {args.status.upper()}")

    try:
        print("[*] Fetching current configuration from controller...")

        current_config = requests.get(args.gurl, timeout=5).json()

        print("[*] Applying local modifications")

        current_config['headers']['bgp_target_peer'] = (f'{args.peer}')
        current_config['headers']['bgp_target_status'] = (f'{args.status}')

        print(f"[*] Pushing updated configuration to {args.purl}...")

        push_response= requests.post(args.purl, json=current_config, timeout=5)
        push_response.raise_for_status()

        print("\n[+] SUCCESS: Configuration successfully deployed!")
        print(f"    Server confirmed status for {args.peer} is now '{args.status}'")

    except requests.exceptions.Timeout:
        print("\n[-] FATAL: Connection to the API timed out. Is the controller down?")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"\n[-] FATAL: A network error occurred: {e}")
        sys.exit(1)
if __name__ == "__main__":
    main()