"""PatternGenerator の正常系テストケースを定義するモジュール。"""
# test_pattern_generator_nomal.py

# MIT License
# Copyright (c) 2025 kazuma tunomori
#
# Permission is hereby granted, free of charge, to any person obtaining a copy...

import numpy as np
import pytest
from numpy.typing import NDArray

from src.icon_generator.generator.git.core.pattern import PatternGenerator


class TestPatternGeneratorNomalCases:
    """正常系における PatternGenerator の動作を検証するテストクラス。"""

    @pytest.fixture
    def hex_string(self) -> str:
        """有効な16進数文字列"""
        return "abcde0123456789"

    @pytest.fixture
    def generator(self, hex_string: str) -> PatternGenerator:
        """PatternGeneratorインスタンス"""
        return PatternGenerator(hex_string)

    @pytest.fixture
    def symmetric_input_pattern(self) -> NDArray[np.int_]:
        """INPUTパターン"""
        return np.array(
            [
                [1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0],
            ],
        )

    @pytest.fixture
    def symmetric_output_pattern(
        self,
        symmetric_input_pattern: NDArray[np.int_],
    ) -> NDArray[np.int_]:
        """OUTPUTパターン"""
        return np.array(
            [
                symmetric_input_pattern[2],
                symmetric_input_pattern[1],
                symmetric_input_pattern[0],
                symmetric_input_pattern[1],
                symmetric_input_pattern[2],
            ],
        )

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_size_from_valid_hex_string(self, generator: PatternGenerator) -> None:
        """指定した16進数文字列から正しいサイズのパターンが生成されること

        対象メソッド: __init__
        in:  有効な16進数文字列(ex: "0123456789abcde")
        out: 想定された行数・列数を持つ2次元配列(ex: shape=(5, 5))
        """
        assert generator.pattern.shape == (5, 5)

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_pattern_rotation_90_degrees_is_correct(
        self,
        hex_string: str,
        generator: PatternGenerator,
        symmetric_output_pattern: NDArray[np.int_],
    ) -> None:
        """90度回転した最終パターンが期待通りのものになっていること

        対象メソッド: _create_pattern
        in:  有効な16進数文字列(ex: "0123456789abcde")
        out: shape=(5, 5)の多次元配列
        """
        pattern = generator._create_pattern(hex_string)  # type: ignore[attr-defined]

        np.testing.assert_array_equal(pattern, np.rot90(symmetric_output_pattern, k=3))

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_pattern_is_symmetric(
        self,
        generator: PatternGenerator,
        symmetric_input_pattern: NDArray[np.int_],
        symmetric_output_pattern: NDArray[np.int_],
    ) -> None:
        """生成されたパターンが左右対称であること

        対象メソッド: _mirror_pattern
        in:  shape=(3, 5)の多次元配列
        out: inがミラーリングされたshape=(5, 5)の多次元配列
        """
        mirrored = generator._mirror_pattern(symmetric_input_pattern)  # type: ignore[attr-defined]

        np.testing.assert_array_equal(mirrored, symmetric_output_pattern)

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_apply_color_shape(
        self,
        generator: PatternGenerator,
    ) -> None:
        """apply_color が返す配列の形状が (5, 5, 3) になっていること

        対象メソッド: apply_color
        in:  0>=x=>255のtuple
        out: shape=(5, 5, 3)の多次元配列
        """
        test_rgb_pattern = (1, 0, 0)
        result = generator.apply_color(rgb_pattern=test_rgb_pattern)

        assert result.shape == (5, 5, 3)

    def test_apply_color_assigns_rgb_to_colored_area(
        self,
        generator: PatternGenerator,
    ) -> None:
        """apply_color メソッドで指定したRGB色が正しくパターンに適用されること

        対象メソッド: apply_color
        in:  0 <= x <= 255 の3要素 tuple(RGBカラー)
        out: パターン内の1の位置に指定した RGB 色が適用されている配列
        """
        # 準備: 特定のRGB 色
        rgb_color = (100, 150, 200)

        color_pattern = generator.apply_color(rgb_color)

        # 検証: パターンの1の位置が指定色になっている
        mask = generator.pattern == 1
        colored_pixels = color_pattern[mask]

        # すべての対象ピクセルが rgb_color と一致しているか
        expected = np.tile(rgb_color, (colored_pixels.shape[0], 1))
        assert np.array_equal(colored_pixels, expected)

    def test_apply_color_assigns_white_to_background(
        self,
        generator: PatternGenerator,
    ) -> None:
        """apply_color がパターンの白部分に白(255,255,255)を適用していること

        対象メソッド: apply_color
        in:  0 <= x <= 255 の3要素 tuple(RGBカラー)
        out: パターン内の0の位置に白色が適用されている配列
        """
        # 準備: 特定のRGB 色
        rgb_color = (10, 20, 30)

        color_pattern = generator.apply_color(rgb_color)

        # 検証: パターンの0の位置が白 (255, 255, 255) になっている
        mask = generator.pattern == 0
        white_pixels = color_pattern[mask]

        expected = np.tile((255, 255, 255), (white_pixels.shape[0], 1))
        assert np.array_equal(white_pixels, expected)
