# Static Site Generator

This project is a static site generator that converts markdown files into HTML pages using a specified template. It also copies static files to the output directory.

## Project Structure
```
src 
├── pycache 
├── core_functions 
│ ├── init.py 
│ ├── copy_directory.py 
│ ├── extract_functions.py 
│ ├── generate_page.py 
│ ├── htmlnode.py 
│ ├── markdown_functions.py 
│ ├── split_nodes_functions.py 
│ ├── text_to_textnode.py 
│ └── textnode.py 
├── tests 
│ ├── init.py 
│ ├── test_block_to_block_type.py 
│ ├── test_delimiter_split.py 
│ ├── test_extract_functions.py 
│ ├── test_htmlnode.py 
│ ├── test_images_links_split.py 
│ ├── test_leafnode.py 
│ ├── test_markdown_to_blocks.py 
│ ├── test_markdown_to_html.py 
│ ├── test_parentnode.py 
│ ├── test_text_to_textnode.py 
│ └── test_textnode.py 
├── main.py 
└── README.md
```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/gijstemp/static-site-generator.git
    cd static-site-generator
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place your markdown files in the `content` directory.
2. Place your static files (e.g., CSS, JavaScript, images) in the `static` directory.
3. Ensure you have an HTML template file named `template.html` in the root directory.

4. Run the main script to generate the static site:
    ```bash
    python3 src/main.py
    ```

5. Serve the generated site locally:
    ```bash
    cd public
    python3 -m http.server 8888
    ```

## Project Components

### `core_functions`

- **copy_directory.py**: Contains the function to recursively copy directories.
- **extract_functions.py**: Functions to extract images and links from markdown text.
- **generate_page.py**: Functions to generate HTML pages from markdown files.
- **htmlnode.py**: Defines the HTMLNode class and its subclasses for representing HTML elements.
- **markdown_functions.py**: Functions to convert markdown text to HTML nodes.
- **split_nodes_functions.py**: Functions to split text nodes by delimiters, images, and links.
- **text_to_textnode.py**: Converts text to a list of TextNode objects.
- **textnode.py**: Defines the TextNode class and its types.

### `tests`

Contains unit tests for the functions in the `core_functions` package.

## Running Tests

To run the tests, use the following command:

```bash
cd src
PYTHONPATH=. python3 -m unittest discover -s tests
```
## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
