# Python - Network Project

## Overview
In this networking project, I utilized `curl` in Bash scripts to interact with a server, gaining insights into various aspects of web communication. The project covered topics such as URL structure, domain names, diverse HTTP request/response header fields, status codes, and the effective use of cookies.

Additionally, an algorithm challenge was tackled in Python as a separate task within the project.

## Tests :

* [tests](./tests): This folder contains test files provided by ALX for validating the project.

## Tasks :

### 0. curl body size
* [0-body_size.sh](./0-body_size.sh): Bash script sending a `GET` request to a specified URL and displaying the size of the response body in bytes.
* Source: [0-body_size.sh](./0-body_size.sh)

### 1. curl to the end
* [1-body.sh](./1-body.sh): Bash script sending a `GET` request to a given URL and displaying the response body for a `200` status code response.
* Source: [1-body.sh](./1-body.sh)

### 2. curl Method
* [2-delete.sh](./2-delete.sh): Bash script sending a `DELETE` request to a specified URL and displaying the response body.
* Source: [2-delete.sh](./2-delete.sh)

### 3. curl only methods
* [3-methods.sh](./3-methods.sh): Bash script displaying all HTTP methods accepted by the server of a given URL.
* Source: [3-methods.sh](./3-methods.sh)

### 4. curl headers
* [4-header.sh](./4-header.sh): Bash script sending a `GET` request to a specified URL with a header variable `X-School-User-Id=98` and displaying the response body.
* Source: [4-header.sh](./4-header.sh)

### 5. curl POST parameters
* [5-post_params.sh](./5-post_params.sh): Bash script sending a `POST` request to a given URL with variables `email=test@gmail.com` and `subject=I will always be here for PLD`, displaying the response body.
* Source: [5-post_params.sh](./5-post_params.sh)

### 6. Find a peak
* [6-peak.py](./6-peak.py): [Technical interview preparation] - Python program finding a peak in a list of unsorted integers.
* [6-peak.txt](./6-peak.txt): Text file containing the complexity of the algorithm.
* Source: [6-peak.py](./6-peak.py), [6-peak.txt](./6-peak.txt)

### 7. Only status code
* [100-status_code.sh](./100-status_code.sh): Bash script sending a `GET` request to a specified URL without using pipes, redirections, `;`, or `&&`, and displaying the status code of the response.
* Source: [100-status_code.sh](./100-status_code.sh)

### 8. curl a JSON file
* [101-post_json.sh](./101-post_json.sh): Bash script sending a JSON `POST` request with the contents of a provided file to a specified URL and displaying the response body.
* Source: [101-post_json.sh](./101-post_json.sh)

### 9. Catch me if you can!
* [102-catch_me.sh](./102-catch_me.sh): Bash script sending a request to `0.0.0.0:5000/catch_me` that triggers the server to respond with a message containing `You got me!` in the response body.
* Source: [102-catch_me.sh](./102-catch_me.sh)
