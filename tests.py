import pytest

"""
Code Analysis:
-The function 'download_css' downloads a CSS file from a given URL and saves it to a local directory.
- The function takes a single input parameter, 'css_url', which is the URL of the CSS file to be downloaded.
- The function sends a GET request to the specified URL using the requests library.
- If the request is successful, the function creates a new file in the 'example' directory with the same name as the CSS file and writes the contents of the response to the file.
- If the request fails, the function prints an error message indicating the reason for the failure.
- The function is called within the main script to download CSS files referenced in the protected page HTML.
- The function does not return any values, but it saves the downloaded CSS file to the local directory.
"""

"""
Test Plan:
- test_download_css_success(): tests that the function successfully downloads a CSS file from a valid URL and saves it to the 'example' directory.
- test_download_css_failure(): tests that the function prints an error message when it fails to download a CSS file from an invalid URL.
- test_download_css_empty_url(): tests the edge case where an empty URL is passed as input to the function, and verifies that the function prints an error message.
- test_download_css_invalid_url(): tests the edge case where an invalid URL is passed as input to the function, and verifies that the function prints an error message.
- test_download_css_missing_directory(): tests the edge case where the 'example' directory does not exist, and verifies that the function creates the directory and saves the CSS file to it.
- test_download_css_existing_file(): tests the edge case where a file with the same name as the CSS file already exists in the 'example' directory, and verifies that the function overwrites the existing file with the new content.
"""

class TestDownloadCss:

    def test_download_css_success(self):
        # Arrange
        css_url = "https://example.com/style.css"
        expected_content = "body { background-color: red; }"
        # Act
        download_css(css_url)
        with open("example/style.css", "r", encoding="utf-8") as css_file:
            actual_content = css_file.read()
        # Assert
        assert actual_content == expected_content

    def test_download_css_failure(self):
        # Arrange
        css_url = "https://example.com/nonexistent.css"
        expected_output = f"Error downloading CSS: HTTPSConnectionPool(host='example.com', port=443): Max retries exceeded with url: /nonexistent.css (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f9d5c1f7d90>: Failed to establish a new connection: [Errno -2] Name or service not known'))\n"
        # Act
        with pytest.raises(SystemExit) as e:
            download_css(css_url)
        actual_output = str(e.value)
        # Assert
        assert actual_output == expected_output

    def test_download_css_empty_url(self):
        # Arrange
        css_url = ""
        expected_output = "Error: Empty URL\n"
        # Act
        with pytest.raises(SystemExit) as e:
            download_css(css_url)
        actual_output = str(e.value)
        # Assert
        assert actual_output == expected_output

    def test_download_css_invalid_url(self):
        # Arrange
        css_url = "invalid-url"
        expected_output = f"Error downloading CSS: Invalid URL 'invalid-url': No schema supplied. Perhaps you meant http://invalid-url?\n"
        # Act
        with pytest.raises(SystemExit) as e:
            download_css(css_url)
        actual_output = str(e.value)
        # Assert
        assert actual_output == expected_output

    def test_download_css_missing_directory(self):
        # Arrange
        css_url = "https://example.com/style.css"
        expected_content = "body { background-color: red; }"
        if os.path.exists("example"):
            os.rmdir("example")
        # Act
        download_css(css_url)
        with open("example/style.css", "r", encoding="utf-8") as css_file:
            actual_content = css_file.read()
        # Assert
        assert actual_content == expected_content

    def test_download_css_existing_file(self):
        # Arrange
        css_url = "https://example.com/style.css"
        expected_content = "body { background-color: blue; }"
        with open("example/style.css", "w", encoding="utf-8") as css_file:
            css_file.write("body { background-color: red; }")
        # Act
        download_css(css_url)
        with open("example/style.css", "r", encoding="utf-8") as css_file:
            actual_content = css_file.read()
        # Assert
        assert actual_content == expected_content

