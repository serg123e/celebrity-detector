# Celebrity detector


## Installation

  1. git clone https://github.com/serg123e/celebrity-detector.git
  2. cd celebrity-detector
  3. docker build -t celebrity-detector .
  4. docker run -p 5080:80 -e API_TOKEN=your_api_token celebrity-detector

## Authentication

    curl -X POST "http://localhost:5080/upload" -H "Authorization: Bearer your_api_token" -F "file=@path_to_your_file"

  If the environment variable API_TOKEN is not set, you can simply use:

    curl -X POST "http://localhost:5080/upload" -F "file=@path_to_your_file"
    

## Based on

[https://github.com/shobhit9618/celeb_recognition](https://github.com/shobhit9618/celeb_recognition)