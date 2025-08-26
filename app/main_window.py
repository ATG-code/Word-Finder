from __future__ import annotations
from copyreg import remove_extension
from dataclasses import dataclass
from typing import List, Optional
from PyQt5.QtCore import QFile, Qt, QRectF, QSize
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QColor, QPixmap, QKeySequence
from PyQt5.QtWidgets import (
    QMainWindow, QFileDialog, QToolBar, QAction, QSpinBox, QLineEdit, QPushButton,
    QStatusBar, QWidget, QLabel, QScrollArea, QListWidget, QListWidgetItem,
    QHBoxLayout, QComboBox, QSplitter, QVBoxLayout, QFrame
)
from .pdf_engine import PdfEngine
from .ui.style import MODERN_QSS

@dataclass
class Match:
    page: int
    rects: List

class PageView(QScrollArea):
    def __init__(self):
        super().__init__()
        self.setWidgetResizable(True)
        self.setFrameStyle(QFrame.NoFrame)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        self.label = QLabel(alignment=Qt.AlignCenter)
        self.label.setStyleSheet("""
            QLabel {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                           stop:0 #0f172a, stop:1 #1e293b);
                border: 2px solid #475569;
                border-radius: 16px;
                padding: 20px;
            }
        """)
        self.setWidget(self.label)

    def set_pixmap(self, pm: QPixmap):
        self.label.setPixmap(pm)

class ModernPdfReader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Word Finder - PDF Reader")
        self.resize(1640, 900)
        self.setMinimumSize(1000, 600)

        # Core
        self.engine = PdfEngine()
        self.current_page = 0
        self.zoom = 1.25
        self.zoom_mode = "fitw"     #? actual | fitw | fitp
        
        # Search
        self._matches = []
        self._mi = -1

        # Widgets
        self.page_view = PageView()
        self.thumb_list = QListWidget()
        self.thumb_list.setIconSize(QSize(140, 180))
        self.thumb_list.setSpacing(8)
        self.thumb_list.itemClicked.connect(self._on_thumb_clicked)
        self.thumb_list.setMaximumWidth(200)
        self.thumb_list.setMinimumWidth(160)

        # Main Layout
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self._create_thumbnail_panel())
        splitter.addWidget(self.page_view)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([200, 1200])
        self.setCentralWidget(splitter)

        self._build_toolbar()
        self._build_statusbar()
        self.setStyleSheet(MODERN_QSS)
        self._build_shortcuts()

    def _create_thumbnail_panel(self):
        """Create a styled thumbnail panel with title"""
        panel = QWidget()
        panel.setObjectName("thumbnailPanel")
        panel.setStyleSheet("""
            QWidget#thumbnailPanel {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                           stop:0 #1e293b, stop:1 #334155);
                border-right: 2px solid #475569;
            }
        """)
        
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(12, 16, 12, 12)
        layout.setSpacing(8)
        
        # Title
        title = QLabel("Thumbnails")
        title.setStyleSheet("""
            QLabel {
                color: #f8fafc;
                font-size: 16px;
                font-weight: bold;
                padding: 8px;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                           stop:0 #475569, stop:1 #64748b);
                border-radius: 12px;
                margin-bottom: 8px;
            }
        """)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Thumbnail list
        layout.addWidget(self.thumb_list)
        
        return panel

    # ----- UI -----
    def _build_toolbar(self):
        tb = QToolBar("Main")
        tb.setMovable(False)
        tb.setIconSize(QSize(24, 24))
        tb.setStyleSheet("""
            QToolBar {
                spacing: 12px;
                padding: 16px;
            }
        """)
        self.addToolBar(tb)

        # File Operations
        act_open = QAction("📁 Open", self)
        act_open.setShortcut(QKeySequence.Open)
        act_open.triggered.connect(self.open_pdf)
        tb.addAction(act_open)

        tb.addSeparator()

        # Navigation
        act_prev = QAction("◀ Prev", self)
        act_prev.triggered.connect(self.prev_page)
        tb.addAction(act_prev)

        self.page_spin = QSpinBox()
        self.page_spin.setMinimum(1)
        self.page_spin.setMaximum(1)
        self.page_spin.setFixedWidth(80)
        self.page_spin.valueChanged.connect(self.on_page_spin)
        tb.addWidget(self.page_spin)

        act_next = QAction("Next ▶", self)
        act_next.triggered.connect(self.next_page)
        tb.addAction(act_next)

        tb.addSeparator()

        # Zoom Controls
        act_zoom_out = QAction("🔍-", self)
        act_zoom_out.setShortcut(QKeySequence.ZoomOut)
        act_zoom_out.triggered.connect(lambda: self.change_zoom(-0.1))
        tb.addAction(act_zoom_out)

        self.zoom_mode_combo = QComboBox()
        self.zoom_mode_combo.addItems(["Actual", "Fit Width", "Fit Page"])
        self.zoom_mode_combo.setFixedWidth(120)
        self.zoom_mode_combo.currentIndexChanged.connect(self._on_zoom_mode_changed)
        tb.addWidget(self.zoom_mode_combo)

        act_zoom_in = QAction("🔍+", self)
        act_zoom_in.setShortcut(QKeySequence.ZoomIn)
        act_zoom_in.triggered.connect(lambda: self.change_zoom(+0.1))
        tb.addAction(act_zoom_in)

        tb.addSeparator()

        # Search Section
        search_label = QLabel("Search:")
        search_label.setStyleSheet("color: #f8fafc; font-weight: bold; margin-right: 8px;")
        tb.addWidget(search_label)

        self.search_edit = QLineEdit(placeholderText="Enter text to search...")
        self.search_edit.setFixedWidth(200)
        self.search_edit.returnPressed.connect(self.search_start)
        tb.addWidget(self.search_edit)

        btn_find = QPushButton("🔍 Find")
        btn_find.setObjectName("searchBtn")
        btn_find.clicked.connect(self.search_start)
        tb.addWidget(btn_find)

        btn_prev = QPushButton("◀ Prev")
        btn_prev.setObjectName("navBtn")
        btn_prev.clicked.connect(self.search_prev)
        tb.addWidget(btn_prev)

        btn_next = QPushButton("Next ▶")
        btn_next.setObjectName("navBtn")
        btn_next.clicked.connect(self.search_next)
        tb.addWidget(btn_next)

    def _build_statusbar(self):
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self._update_status()

    def _build_shortcuts(self):
        for seq, slot in [
            (QKeySequence.Find, self._focus_search),
        ]:
            act = QAction(self)
            act.setShortcut(seq)
            act.triggered.connect(slot)
            self.addAction(act)

    # ----- File -----
    def open_pdf(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")
        if not path:
            return
        self.engine.open(path)
        self.current_page = 0
        self.page_spin.setMaximum(self.engine.page_count)
        self.page_spin.setValue(1)
        self._build_thumbnails()
        self._clear_search()
        self.render_page()

    # ----- Render -----
    def _auto_zoom(self) -> float:
        w, h = self.engine.page_size(self.current_page)
        vw = max(100, self.page_view.viewport().width() - 48)
        vh = max(100, self.page_view.viewport().height() - 48)
        if self.zoom_mode == "fitw":
            return vw / w
        if self.zoom_mode == "fitp":
            return min(vw / w, vh / h)
        return self.zoom

    def render_page(self, highlights: Optional[List] = None):
        if self.engine.page_count == 0:
            self.page_view.set_pixmap(QPixmap())
            return
        scale = self._auto_zoom()
        pm = self.engine.render_page(self.current_page, scale)
        if highlights:
            painter = QPainter(pm)
            pen = QPen(QColor(59, 130, 246, 200))  # Blue color
            pen.setWidth(3)
            painter.setPen(pen)
            painter.setBrush(QColor(59, 130, 246, 80))
            for r in highlights:
                x = int(r.x0 * scale)
                y = int(r.y0 * scale)
                w = int(r.width * scale)
                h = int(r.height * scale)
                painter.drawRect(x, y, w, h)
            painter.end()
        self.page_view.set_pixmap(pm)
        self._update_status()

    def resizeEvent(self, e):
        super().resizeEvent(e)
        if self.engine.page_count and self.zoom_mode in ("fitw", "fitp"):
            self.render_page(self._current_highlights())

    # ----- Thumbnails -----
    def _build_thumbnails(self):
        self.thumb_list.clear()
        if self.engine.page_count == 0:
            return
        scale = 0.15
        for pno in range(self.engine.page_count):
            pm = self.engine.render_page(pno, scale)
            it = QListWidgetItem(QIcon(pm), f"Page {pno+1}")
            it.setSizeHint(QSize(140, 180))
            self.thumb_list.addItem(it)

    def _on_thumb_clicked(self, item: QListWidgetItem):
        row = self.thumb_list.row(item)
        if row != self.current_page:
            self.current_page = row
            self.page_spin.blockSignals(True)
            self.page_spin.setValue(self.current_page + 1)
            self.page_spin.blockSignals(False)
            self.render_page(self._current_highlights())

    # ---------- Navigation & Zoom ----------
    def next_page(self):
        if self.current_page < self.engine.page_count - 1:
            self.current_page += 1
            self.page_spin.blockSignals(True)
            self.page_spin.setValue(self.current_page + 1)
            self.page_spin.blockSignals(False)
            self.render_page(self._current_highlights())

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.page_spin.blockSignals(True)
            self.page_spin.setValue(self.current_page + 1)
            self.page_spin.blockSignals(False)
            self.render_page(self._current_highlights())

    def on_page_spin(self, value: int):
        self.current_page = max(0, min(value - 1, self.engine.page_count - 1))
        self.render_page(self._current_highlights())

    def change_zoom(self, delta: float):
        self.zoom_mode = "actual"
        self.zoom = round(max(0.25, min(self.zoom + delta, 6.0)), 2)
        self.render_page(self._current_highlights())

    def _on_zoom_mode_changed(self, idx: int):
        self.zoom_mode = {0: "actual", 1: "fitw", 2: "fitp"}.get(idx, "actual")
        self.render_page(self._current_highlights())

    # ----- Search -----
    def _focus_search(self):
        self.search_edit.setFocus()
        self.search_edit.selectAll()

    def _clear_search(self):
        self._matches: List[Match] = []
        self._mi = -1

    def _current_highlights(self):
        for m in self._matches:
            if m.page == self.current_page:
                return m.rects
        return None

    def search_start(self):
        text = self.search_edit.text().strip()
        if not text or self.engine.page_count == 0:
            self.status.showMessage("No text to search or no document open.", 3000)
            return
        self._matches.clear()
        for p in range(self.engine.page_count):
            rects = self.engine.search_in_page(p, text)
            if rects:
                self._matches.append(Match(page=p, rects=rects))
        if not self._matches:
            self.status.showMessage(f"No matches found for '{text}'", 3000)
            return
        self._mi = 0
        self._jump(self._mi)

    def _jump(self, idx: int):
        m = self._matches[idx]
        self.current_page = m.page
        self.page_spin.blockSignals(True)
        self.page_spin.setValue(self.current_page + 1)
        self.page_spin.blockSignals(False)
        self.render_page(highlights=m.rects)
        self.status.showMessage(f"Match {idx+1}/{len(self._matches)} on page {m.page+1}", 4000)

    def search_next(self):
        if not self._matches:
            self.search_start()
            return
        self._mi = (self._mi + 1) % len(self._matches)
        self._jump(self._mi)

    def search_prev(self):
        if not self._matches:
            self.search_start()
            return
        self._mi = (self._mi - 1) % len(self._matches)
        self._jump(self._mi)

    # ----- Status -----
    def _update_status(self):
        if self.engine.page_count == 0:
            self.status.showMessage("No document opened. Use File → Open to load a PDF.")
            return
        self.status.showMessage(
            f"Page {self.current_page+1}/{self.engine.page_count} | "
            f"Zoom: {self.zoom_mode.upper()} | "
            f"Scale: {self._auto_zoom():.2f}x"
        )