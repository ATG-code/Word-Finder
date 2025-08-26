# 📚 Word Finder - Modern PDF Reader

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)](https://www.riverbankcomputing.com/software/pyqt/)
[![PyMuPDF](https://img.shields.io/badge/PyMuPDF-1.24+-orange.svg)](https://pymupdf.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/yourusername/Word-Finder)

> A modern, feature-rich PDF reader with advanced search capabilities and a beautiful dark theme interface.

## ✨ Features

- 🔍 **Advanced Text Search**: Find and highlight text across all pages
- 🖼️ **Thumbnail Navigation**: Quick page preview and navigation
- 📱 **Modern UI**: Beautiful dark theme with gradient backgrounds
- 🔍 **Smart Zoom**: Multiple zoom modes (Actual, Fit Width, Fit Page)
- ⌨️ **Keyboard Shortcuts**: Full keyboard navigation support
- 📄 **Multi-page Support**: Handle large PDF documents efficiently
- 🎨 **Professional Design**: Modern interface with smooth interactions

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- PyQt5
- PyMuPDF

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Word-Finder.git
   cd Word-Finder
   ```

2. **Install dependencies**
   ```bash
   pip install -r Requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 📋 Requirements

```
PyQt5==5.15.9
PyMuPDF>=1.24.0
```

## 🎯 Usage

### Opening PDFs
- Click the **📁 Open** button or use `Ctrl+O`
- Navigate to your PDF file and select it
- The document will load with thumbnails and page view

### Navigation
- **◀ Prev** / **Next ▶**: Navigate between pages
- **Page Spinner**: Jump to specific page numbers
- **Thumbnails**: Click thumbnail to jump to that page

### Search Functionality
1. Type your search term in the search field
2. Click **🔍 Find** or press `Enter`
3. Use **◀ Prev** / **Next ▶** to navigate between matches
4. Search results are highlighted in blue

### Zoom Controls
- **🔍+** / **🔍-**: Zoom in/out
- **Zoom Mode Dropdown**: Choose between Actual, Fit Width, or Fit Page

## 🏗️ Architecture

```
Word-Finder/
├── app/
│   ├── __init__.py
│   ├── main_window.py      # Main application window
│   ├── pdf_engine.py       # PDF processing engine
│   └── ui/
│       ├── __init__.py
│       └── style.py        # Modern styling system
├── main.py                 # Application entry point
├── Requirements.txt        # Python dependencies
└── README.md              # This file
```

### Core Components

- **`ModernPdfReader`**: Main application window with modern UI
- **`PdfEngine`**: PyMuPDF-based PDF processing and rendering
- **`PageView`**: Scrollable PDF page display
- **`MODERN_QSS`**: Comprehensive styling system

## 🎨 UI Features

### Modern Design
- **Gradient Backgrounds**: Beautiful linear gradients throughout
- **Rounded Corners**: Modern 12px border radius on all elements
- **Professional Colors**: Carefully chosen color palette for readability
- **Hover Effects**: Smooth transitions and visual feedback

### Responsive Layout
- **Splitter Panels**: Resizable thumbnail and page view areas
- **Adaptive Sizing**: Automatic zoom and fit modes
- **Minimum Constraints**: Ensures usability on smaller screens

## 🔧 Development

### Project Structure
- **Modular Design**: Separated concerns for maintainability
- **Type Hints**: Full Python type annotation support
- **Error Handling**: Comprehensive error handling and user feedback
- **Clean Code**: Well-documented and organized codebase

### Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style
- Follow PEP 8 guidelines
- Use type hints for all functions
- Add docstrings for classes and methods
- Keep functions focused and single-purpose

## 🐛 Troubleshooting

### Common Issues

**PyMuPDF Import Error**
```bash
pip uninstall PyMuPDF
pip install PyMuPDF>=1.24.0
```

**PyQt5 Installation Issues**
```bash
pip install PyQt5==5.15.9
```

**Missing Dependencies**
```bash
pip install -r Requirements.txt
```

## 📱 Platform Support

- ✅ **Windows 10/11**
- ✅ **macOS 10.14+**
- ✅ **Linux (Ubuntu 18.04+)**

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r Requirements.txt`
5. Run the app: `python main.py`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **PyMuPDF**: For powerful PDF processing capabilities
- **PyQt5**: For the robust GUI framework
- **Open Source Community**: For inspiration and support

## 📞 Support

If you find this project helpful, please consider:

- ⭐ **Starring** the repository
- 🐛 **Reporting** bugs or issues
- 💡 **Suggesting** new features
- 📖 **Improving** the documentation

---

## ☕ Buy Me a Coffee

If you enjoy using Word Finder and would like to support its development, consider buying me a coffee! ☕

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/yourusername)

Your support helps keep this project alive and enables new features and improvements! 🚀

---

**Made with ❤️ by [Your Name]**

*Built for the open-source community*
