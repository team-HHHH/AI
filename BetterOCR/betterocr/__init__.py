from .detect import (
    detect,
    detect_async,
    detect_text,
    detect_text_async,
    detect_boxes,
    detect_boxes_async,
    NoTextDetectedError,
)
from .parsers import extract_json

__all__ = [
    "detect",
    "detect_async",
    "detect_text",
    "detect_text_async",
    "detect_boxes",
    "detect_boxes_async",
    "NoTextDetectedError",
    "extract_json",
]

__author__ = "junhoyeo"
