# Python - Network #1

This project focuses on utilizing the `urllib` and `requests` Python libraries to interact with HTTP, sending and receiving messages to and from URLs. The tasks involve practicing the implementation of `GET` and `POST` requests, fetching JSON resources, and interacting with various APIs, including the Star Wars API, GitHub API, and Twitter API.

## Tasks :page_with_curl:

### 0. What's my status? #0
   - **File**: [0-hbtn_status.py](./0-hbtn_status.py)
   - **Description**: Python script that fetches `https://intranet.hbtn.io/status` using `urllib`.

### 1. Response header value #0
   - **File**: [1-hbtn_header.py](./1-hbtn_header.py)
   - **Description**: Python script that displays the `X-Request-Id` response header variable of a request to a given URL using `urllib`.
   - **Usage**: `./1-hbtn_header.py <URL>`

### 2. POST an email #0
   - **File**: [2-post_email.py](./2-post_email.py)
   - **Description**: Python script that sends a `POST` request to a given URL with a given email and displays the response body using `urllib`.
   - **Usage**: `./2-post_email.py <URL> <email>`

### 3. Error code #0
   - **File**: [3-error_code.py](./3-error_code.py)
   - **Description**: Python script that sends a request to a given URL and displays the response body. It handles HTTP errors using `urllib`.

### 4. What's my status? #1
   - **File**: [4-hbtn_status.py](./4-hbtn_status.py)
   - **Description**: Python script that fetches `https://intranet.hbtn.io/status` using `requests`.

### 5. Response header value #1
   - **File**: [5-hbtn_header.py](./5-hbtn_header.py)
   - **Description**: Python script that displays the `X-Request-Id` response header variable of a request to a given URL using `requests`.
   - **Usage**: `./5-hbtn_header.py <URL>`

### 6. POST an email #1
   - **File**: [6-post_email.py](./6-post_email.py)
   - **Description**: Python script that sends a `POST` request to a given URL with a given email and displays the response body using `requests`.
   - **Usage**: `./6-post_email.py <URL> <email>`

### 7. Error code #1
   - **File**: [7-error_code.py](./7-error_code.py)
   - **Description**: Python script that sends a request to a given URL and displays the response body. It handles HTTP errors using `requests`.

### 8. Search API
   - **File**: [8-json_api.py](./8-json_api.py)
   - **Description**: Python script that sends a `POST` request to `http://0.0.0.0:5000/search_user` with a letter passed as a parameter. It uses `requests`.
   - **Usage**: `./8-json_api.py <letter>`

### 9. My Github!
   - **File**: [10-my_github.py](./10-my_github.py)
   - **Description**: Python script that takes GitHub credentials (username and password) and uses the GitHub API to display the corresponding ID using `requests`.
   - **Usage**: `./10-my_github.py <username> <password>`

### 10. Time for an interview!
   - **File**: [100-github_commits.py](./100-github_commits.py)
   - **Description**: Python script that lists the 10 most recent comments of a given GitHub repository using the GitHub API with `requests`.
   - **Usage**: `./100-github_commits.py <repository name> <owner name>`
