# AloraVoter: Automated Voting Bot for Alora

AloraVoter is a specialized automated voting bot designed to generate vote codes for Alora RSPS.

## Key Features

- **Multi-Platform Support**: Seamlessly votes for Alora across multiple top-list sites, including RuneLocus, RSPS-List, MoparScape, and RuneList.
- **Automated Captcha Solving**: Integrates with TwoCaptcha to automatically solve captchas, facilitating uninterrupted voting processes.
- **Proxy Rotation System**: Utilizes a dynamic proxy rotation mechanism to simulate votes from rotating proxies, enhancing anonymity and minimizing the risk of bans.
- **Error Recovery and Retry Logic**: Features robust error handling and retry strategies to address issues such as network timeouts, failed captcha solutions, and unexpected website responses.
- **Configurable Voting Intervals**: Allows for the customization of voting intervals with randomization options to simulate genuine user activity and avoid detection.
- **Detailed Logging and Monitoring**: Offers comprehensive logging of all voting activities, including successes, failures, and the status of each vote attempt, for easy monitoring and troubleshooting.
- **Threaded Voting Processes**: Supports concurrent voting through multithreading, significantly speeding up the voting process while efficiently managing resources.

## How It Works

AloraVoter automates the voting process by:

1. **Fetching Vote Sites and UID**: Dynamically retrieves the list of vote sites and corresponding UIDs for Alora.
2. **Handling Captchas**: Automatically solves captchas using TwoCaptcha for sites that require captcha verification.
4. **Logging and Reporting**: Maintains detailed logs for each vote attempt and reports the overall success rate and potential issues encountered during the voting process.

## Setup and Usage

1. Configure your TwoCaptcha API key in the script.
2. Populate the `proxies.txt` file with your proxy list.
3. Run AloraVoter to start the automated voting process.
4. Monitor the voting progress through the generated logs and adjust configurations as needed for optimal performance.

## Disclaimer

AloraVoter is developed to assist in promoting servers on top-list sites within the bounds of their terms of service. Users are responsible for ensuring their use of AloraVoter complies with these terms.

Enjoy a hassle-free voting experience and boost your server's visibility with AloraVoter, your dedicated voting companion for Alora.