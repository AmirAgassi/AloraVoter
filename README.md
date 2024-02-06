# AloraVoter: Automated Voting System

AloraVoter is a sophisticated automated voting tool designed to streamline the voting process for the Alora RSPS across multiple RSPS listing websites. This Python script automates the tedious process of voting, handling captcha challenges, and verifying successful votes, providing a hands-off approach for users looking to support their favorite server.

## Features

- **Automated Voting on Multiple Sites**: Supports automated voting on RuneLocus, RSPSList, MoparScape, and RuneList, covering a broad spectrum of the most popular RSPS listing sites.
- **Captcha Solving Integration**: Integrates with TwoCaptcha for solving both image captchas and reCAPTCHAs, ensuring high success rates in automated voting.
- **Session Management**: Utilizes requests and requests_html sessions for efficient navigation and interaction with voting pages, maintaining session cookies and headers for consistent voting sessions.
- **Dynamic UID Retrieval**: Dynamically retrieves unique identifiers (UIDs) for each voting site, ensuring the correct application of votes to the targeted RSPS.
- **Vote Verification**: After casting votes, the script checks to confirm that each vote is registered, providing feedback on the success of voting operations.
- **Selenium WebDriver Support**: Incorporates Selenium for more complex interactions with web pages that require JavaScript rendering, enhancing the script's compatibility with diverse voting mechanisms.

## How it Works

1. **UID Retrieval**: Initially, the script fetches the unique voting links (UIDs) for the server on each site.
2. **Captcha Handling**: Depending on the site's security measures, the script either solves captchas automatically via TwoCaptcha or simulates user interaction using Selenium.
3. **Vote Submission**: With captchas solved and session cookies managed, votes are submitted to each site.
4. **Vote Confirmation**: Post-vote, the script verifies if the vote was successfully registered on the RSPS listing site.

## Setup Instructions

1. Install required Python packages including `requests`, `requests_html`, `selenium`, and `twocaptcha`.
2. Obtain a TwoCaptcha API key for captcha solving services.
3. Update the script with your specific user details and preferences, such as the targeted RSPS UID and your TwoCaptcha API key.
4. Run the script either as a scheduled task or manually, depending on your voting strategy.

## Dependencies

- Python 3.x
- `requests` and `requests_html` for HTTP requests.
- `selenium` for web automation.
- `twocaptcha` for captcha solving services.
- A valid TwoCaptcha API key.

## Disclaimer

This tool is intended for educational purposes and should be used in accordance with the terms of service of the respective RSPS listing sites and the TwoCaptcha service. Users are responsible for any actions taken by this script under their accounts.

## Contributions

Contributions to AloraVoter are welcome, whether they're for adding support for new sites, improving captcha solving success rates, or enhancing the overall robustness of the script.

## License

AloraVoter is open-sourced under the MIT License. See the LICENSE file for more details.

---

AloraVoter represents a significant leap forward in automating the RSPS voting process, offering users a reliable and efficient method to support their favorite servers with minimal effort.
