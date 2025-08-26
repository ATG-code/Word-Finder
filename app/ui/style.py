MODERN_QSS = """
/* Modern Dark Theme for Word Finder */

/* Main Window */
QMainWindow {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #0f172a, stop:1 #1e293b);
    color: #f1f5f9;
}

/* Toolbar */
QToolBar {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #1e293b, stop:1 #334155);
    border: none;
    border-bottom: 2px solid #475569;
    padding: 12px;
    spacing: 8px;
}

QToolButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #475569, stop:1 #64748b);
    color: #f8fafc;
    border: none;
    border-radius: 12px;
    padding: 10px 16px;
    font-weight: 600;
    font-size: 13px;
    min-width: 80px;
}

QToolButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #64748b, stop:1 #94a3b8);
}

QToolButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #334155, stop:1 #475569);
}

/* Separator */
QToolBar QWidget[class="separator"] {
    background: #475569;
    width: 2px;
    margin: 0 8px;
}

/* Status Bar */
QStatusBar {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #1e293b, stop:1 #334155);
    color: #cbd5e1;
    border-top: 1px solid #475569;
    padding: 8px 16px;
    font-size: 12px;
}

/* Form Controls */
QLineEdit, QSpinBox, QComboBox {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #334155, stop:1 #475569);
    color: #f8fafc;
    border: 2px solid #64748b;
    border-radius: 12px;
    padding: 10px 16px;
    font-size: 13px;
    selection-background-color: #3b82f6;
}

QLineEdit:focus, QSpinBox:focus, QComboBox:focus {
    border: 2px solid #3b82f6;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #1e40af, stop:1 #3b82f6);
}

QLineEdit::placeholder {
    color: #94a3b8;
    font-style: italic;
}

/* Buttons */
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #3b82f6, stop:1 #1d4ed8);
    color: #ffffff;
    border: none;
    border-radius: 12px;
    padding: 12px 20px;
    font-weight: 600;
    font-size: 13px;
    min-width: 80px;
}

QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #60a5fa, stop:1 #3b82f6);
}

QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #1d4ed8, stop:1 #1e3a8a);
}

/* Search Button */
QPushButton#searchBtn {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #10b981, stop:1 #059669);
}

QPushButton#searchBtn:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #34d399, stop:1 #10b981);
}

/* Navigation Buttons */
QPushButton#navBtn {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #8b5cf6, stop:1 #7c3aed);
}

QPushButton#navBtn:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #a78bfa, stop:1 #8b5cf6);
}

/* Thumbnail List */
QListWidget {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #1e293b, stop:1 #334155);
    color: #e2e8f0;
    border: none;
    border-radius: 16px;
    padding: 8px;
    outline: none;
}

QListWidget::item {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #475569, stop:1 #64748b);
    border: 2px solid #64748b;
    border-radius: 12px;
    padding: 12px;
    margin: 4px;
    color: #f8fafc;
    font-weight: 500;
}

QListWidget::item:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #64748b, stop:1 #94a3b8);
    border: 2px solid #94a3b8;
}

QListWidget::item:selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #3b82f6, stop:1 #1d4ed8);
    border: 2px solid #60a5fa;
    color: #ffffff;
}

/* Scrollbars */
QScrollBar:vertical {
    background: #1e293b;
    width: 16px;
    border-radius: 8px;
    margin: 0;
}

QScrollBar::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #64748b, stop:1 #94a3b8);
    border-radius: 8px;
    min-height: 40px;
    margin: 2px;
}

QScrollBar::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #94a3b8, stop:1 #cbd5e1);
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar:horizontal {
    background: #1e293b;
    height: 16px;
    border-radius: 8px;
    margin: 0;
}

QScrollBar::handle:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #64748b, stop:1 #94a3b8);
    border-radius: 8px;
    min-width: 40px;
    margin: 2px;
}

QScrollBar::handle:horizontal:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #94a3b8, stop:1 #cbd5e1);
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0px;
}

/* Page View */
QScrollArea {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #0f172a, stop:1 #1e293b);
    border: none;
}

QLabel {
    color: #f8fafc;
    background: transparent;
}

/* Splitter */
QSplitter::handle {
    background: #475569;
    width: 4px;
}

QSplitter::handle:hover {
    background: #64748b;
}

/* Combo Box Dropdown */
QComboBox::drop-down {
    border: none;
    width: 20px;
}

QComboBox::down-arrow {
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 5px solid #f8fafc;
    margin-right: 8px;
}

QComboBox QAbstractItemView {
    background: #334155;
    border: 2px solid #64748b;
    border-radius: 12px;
    selection-background-color: #3b82f6;
    color: #f8fafc;
}

/* Spin Box */
QSpinBox::up-button, QSpinBox::down-button {
    background: #64748b;
    border: none;
    border-radius: 6px;
    width: 20px;
    height: 20px;
}

QSpinBox::up-button:hover, QSpinBox::down-button:hover {
    background: #94a3b8;
}

QSpinBox::up-arrow {
    image: none;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-bottom: 4px solid #f8fafc;
}

QSpinBox::down-arrow {
    image: none;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 4px solid #f8fafc;
}

/* Focus and Selection */
*:focus {
    outline: none;
}

/* Custom Properties for Dynamic Styling */
QWidget[class="pageView"] {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #0f172a, stop:1 #1e293b);
}

QWidget[class="thumbnailPanel"] {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                               stop:0 #1e293b, stop:1 #334155);
    border-right: 2px solid #475569;
}
"""

# Keep the old style for backward compatibility
DARK_QSS = MODERN_QSS