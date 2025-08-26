from __future__ import annotations
from pathlib import Path
from typing import List, Optional
import fitz  # PyMuPDF
from PyQt5.QtGui import QImage, QPixmap

class PdfEngine():
    """PyMuPDF tabanlı PDF işlemleri: açma, render, arama, thumb üretimi."""
    def __init__(self) -> None:
        self.doc: Optional[fitz.Document] = None
        self.path: Optional[Path] = None

    # ----- Core -----
    def open(self, file_path: str | Path) -> None:
        p = Path(file_path)
        self.doc = fitz.open(p.as_posix())
        self.path = p

    @property
    def page_count(self) -> int:
        return self.doc.page_count if self.doc else 0

    # ----- Rendering -----
    def render_page(self, page_no: int, scale: float) -> QPixmap:
        self._ensure()
        page = self.doc.load_page(page_no)
        pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
        qimg = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
        qimg = qimg.copy()
        return QPixmap.fromImage(qimg)

    def page_size(self, page_no: int) -> tuple[float, float]:
        self._ensure()
        r = self.doc.load_page(page_no).rect
        return (r.width, r.height)

    # ----- Search -----
    def search_in_page(self, page_no: int, text: str) -> List[fitz.Rect]:
        self._ensure()
        page = self.doc.load_page(page_no)
        return page.search_for(text, quads=False)

    def search_all(self, text: str) -> list[tuple[int, List[fitz.Rect]]]:
        self._ensure()
        hits = []
        for pno in range(self.page_count):
            rects = self.search_in_page(pno, text)
            if rects:
                hits.append((pno, rects))
        return hits

    # ----- Utils -----
    def _ensure(self) -> None:
        if not self.doc:
            raise RuntimeError("No document opened!")