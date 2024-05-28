# Celebrity detector


## Build and run

  1. git lfs install
  2. git clone https://github.com/serg123e/celebrity-detector.git
  3. cd celebrity-detector
  4. docker build -t celebrity-detector .
  5. docker run -p 5080:80 -e API_TOKEN=your_api_token celebrity-detector

## Authentication

    curl -X POST "http://localhost:5080/upload" -H "Authorization: your_api_token" -F "file=@./path/to/your/file.jpg"

  If the environment variable API_TOKEN is not set, you can simply use:

    curl -X POST "http://localhost:5080/upload" -F "file=@./path/to/your/file.jpg"
    

## Based on

[https://github.com/shobhit9618/celeb_recognition](https://github.com/shobhit9618/celeb_recognition)