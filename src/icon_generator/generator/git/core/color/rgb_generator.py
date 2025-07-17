"""RGBGeneratorモジュール:

HSL形式で表現されたカラーパターン文字列からRGBカラー値を生成するクラスを提供します。
"""
# rgb_generator.py

# MIT License
# Copyright (c) 2025 kazuma tunomori
#
# Permission is hereby granted, free of charge, to any person obtaining a copy...

import colorsys
import math

from src.icon_generator.errors import ErrorMessages

from .hsl_converter import HSLConverter


class RGBGenerator:
    """HSLパターンを元にRGBカラーを生成するクラス。

    Attributes:
        rgb (tuple[int, int, int]): 0-255スケールのRGBカラー値リスト。
        red (int): 赤成分 (0-255)
        green (int): 緑成分 (0-255)
        blue (int): 青成分 (0-255)

    Methods:
        __init__(color_pattern: str):
            カラーパターン文字列からHSLを計算し、RGBに変換して属性に設定する。

    """

    rgb: tuple[int, int, int]
    red: int
    green: int
    blue: int

    def __init__(self, color_pattern: str) -> None:
        """RGBGeneratorのコンストラクタ。

        HSLConverterを用いてcolor_patternからHSLを算出し、
        colorsysでRGBに変換後、0-255スケールで格納する。

        Args:
            color_pattern (str): 16進数形式のカラーパターン文字列。(7文字固定)

        """
        pattern_len = 7
        if len(color_pattern) != pattern_len:
            message = ErrorMessages.INVALID_HEX_LENGTH.format(length=len(color_pattern))
            raise ValueError(message)

        hue, saturation, luminance = HSLConverter.from_pattern(color_pattern)

        # HLS -> RGB変換 (colorsysはHLS順)
        icon_rgb = colorsys.hls_to_rgb(
            h=hue / 360,
            l=luminance / 100,
            s=saturation / 100,
        )

        # 0-1 -> 0-255 スケールに変換し整数化
        self.rgb = (
            math.floor(icon_rgb[0] * 255),
            math.floor(icon_rgb[1] * 255),
            math.floor(icon_rgb[2] * 255),
        )
        self.red, self.green, self.blue = self.rgb
