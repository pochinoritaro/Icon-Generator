"""PatternGenerator の正常系テストケースを定義するモジュール。"""
# test_pattern_generator_nomal.py

# MIT License
# Copyright (c) 2025 kazuma tunomori
#
# Permission is hereby granted, free of charge, to any person obtaining a copy...

import numpy as np
import pytest

from src.icon_generator.generator.git.core.pattern import PatternGenerator


class TestPatternGeneratorNomalCases:
    """正常系における PatternGenerator の動作を検証するテストクラス。"""

    hex_string = "0123456789abcde"

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_size_from_valid_hex_string(self) -> None:
        """指定した16進数文字列から正しいサイズのパターンが生成されること

        対象メソッド: __init__
        in:  有効な16進数文字列(ex: "0123456789abcde")
        out: 想定された行数・列数を持つ2次元配列(ex: shape=(5, 5))
        """
        generator = PatternGenerator(hex_pattern=self.hex_string)
        assert generator.pattern.shape == (5, 5)

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_pattern_rotation_90_degrees_is_correct(self) -> None:
        """90度回転した最終パターンが期待通りのものになっていること

        対象メソッド: _create_pattern
        in:  有効な16進数文字列(ex: "0123456789abcde")
        out: shape=(5, 5)の多次元配列
        """
        # テスト用のインスタンスを作成
        generator = PatternGenerator(self.hex_string)

        # 元のパターン(3行5列)を用意
        input_pattern = np.array(
            [
                [1, 0, 1, 0, 1],  # 行0
                [0, 1, 0, 1, 0],  # 行1
                [1, 0, 1, 0, 1],  # 行2
            ],
        )

        # 期待されるミラーリング結果(5行5列)
        expected = np.array(
            [
                input_pattern[2],
                input_pattern[1],
                input_pattern[0],
                input_pattern[1],
                input_pattern[2],
            ],
        )

        pattern = generator._create_pattern(self.hex_string)  # type: ignore[attr-defined]

        np.testing.assert_array_equal(pattern, np.rot90(expected, k=3))

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_pattern_is_symmetric(self) -> None:
        """生成されたパターンが左右対称であること

        対象メソッド: _mirror_pattern
        in:  shape=(3, 5)の多次元配列
        out: inがミラーリングされたshape=(5, 5)の多次元配列
        """
        # テスト用のインスタンスを作成
        generator = PatternGenerator(self.hex_string)

        # 元のパターン(3行5列)を用意
        input_pattern = np.array(
            [
                [1, 0, 0, 1, 1],  # 行0
                [0, 1, 1, 0, 0],  # 行1
                [1, 1, 0, 0, 1],  # 行2
            ],
        )

        # 期待されるミラーリング結果(5行5列)
        expected = np.array(
            [
                input_pattern[2],
                input_pattern[1],
                input_pattern[0],
                input_pattern[1],
                input_pattern[2],
            ],
        )

        mirrored = generator._mirror_pattern(input_pattern)  # type: ignore[attr-defined]

        np.testing.assert_array_equal(mirrored, expected)
