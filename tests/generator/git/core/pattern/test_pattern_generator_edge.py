"""PatternGenerator の異常系テストケースを定義するモジュール。"""
# test_pattern_generator_nomal.py

# MIT License
# Copyright (c) 2025 kazuma tunomori
#
# Permission is hereby granted, free of charge, to any person obtaining a copy...

import numpy as np
import pytest

from src.icon_generator.generator.git.core.pattern import PatternGenerator


class TestPatternGeneratorEdgeCases:
    """PatternGeneratorにおける準異常系の動作を検証するテストクラス。"""

    @pytest.fixture
    def hex_string(self) -> str:
        """有効な16進数文字列"""
        return "abcde0123456789"

    @pytest.fixture
    def generator(self, hex_string: str) -> PatternGenerator:
        """PatternGeneratorインスタンス"""
        return PatternGenerator(hex_string)

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    @pytest.mark.parametrize(
        ("biased_hex", "result"),
        [
            ("2468ace02468ace", 1),
            ("13579bdf13579bd", 0),
        ],
    )
    def test_all_biased_hex_pattern(self, biased_hex: str, result: int) -> None:
        """16進数文字列がすべて偶数or奇数で偏ったパターンになる場合の処理確認

        Args:
            biased_hex (str): 偶数or奇数に偏った16進数パターン
            result (int): 0 or 1

        """
        generator = PatternGenerator(hex_pattern=biased_hex)
        assert np.all(generator.pattern == result)

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_apply_color_with_white_rgb(self, generator: PatternGenerator) -> None:
        """RGB色が白(255,255,255)の場合パターンがすべて白になるかの確認

        Args:
            generator (PatternGenerator): PatternGeneratorインスタンス

        """
        rgb_pattern_white = (255, 255, 255)
        pattern = generator.apply_color(rgb_pattern=rgb_pattern_white)
        assert np.all(pattern == rgb_pattern_white)

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_apply_color_with_black_rgb(self, generator: PatternGenerator) -> None:
        """RGB色が黒(0,0,0)の場合パターンがすべて黒になるかの確認

        Args:
            generator (PatternGenerator): PatternGeneratorインスタンス

        """
        rgb_pattern_black = (0, 0, 0)
        bg_pattern = (255, 255, 255)
        pattern = generator.apply_color(rgb_pattern=rgb_pattern_black)

        # 黒
        colored_pixels = pattern[generator.pattern == 1]
        expected = np.tile(rgb_pattern_black, (colored_pixels.shape[0], 1))
        assert np.array_equal(colored_pixels, expected)

        # 背景色
        bg_colored_pixels = pattern[generator.pattern == 0]
        bg_expected = np.tile(bg_pattern, (bg_colored_pixels.shape[0], 1))
        assert np.array_equal(bg_colored_pixels, bg_expected)

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    @pytest.mark.parametrize(
        ("invalid_rgb_tupple", "expected_exception", "expected_message"),
        [
            (
                None,
                ValueError,
                "rgb_pattern must be a list of 3 integers",
            ),
            (
                [],
                ValueError,
                "rgb_pattern must be a list of 3 integers",
            ),
            (
                (3,),
                ValueError,
                "rgb_pattern must be a list of 3 integers",
            ),
        ],
    )
    def test_apply_color_with_none_or_empty_input(
        self,
        generator: PatternGenerator,
        invalid_rgb_tupple: tuple[int | float, ...],
        expected_exception: type[Exception],
        expected_message: str,
    ) -> None:
        """apply_color に None や空リストが渡された場合の確認

        Args:
            generator (PatternGenerator): PatternGeneratorインスタンス
            invalid_rgb_tupple (tuple[int  |  float, ...]): 誤ったrgbのタプル
            expected_exception (type[Exception]): 発生する例外
            expected_message (str): 例外のメッセージ

        """
        with pytest.raises(
            expected_exception,
            match=expected_message,
        ):
            generator.apply_color(rgb_pattern=invalid_rgb_tupple)  # type: ignore[reportArgumentType]

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_hex_pattern_case_insensitivity(self, generator: PatternGenerator) -> None:
        """16進数文字列の大文字・小文字混在時に正しく処理できることの確認

        Args:
            generator (PatternGenerator): PatternGeneratorインスタンス

        """
        hex_pattern_wth_upper = "AbCde0123456789"
        pattern_wth_upper = PatternGenerator(hex_pattern=hex_pattern_wth_upper)

        assert np.array_equal(generator.pattern, pattern_wth_upper.pattern)

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    @pytest.mark.parametrize(
        "repeated_hex",
        [
            "111111111111111",
            "f1f1f1111111111",
        ],
    )
    def test_mirror_pattern_with_repeated_values(self, repeated_hex: str) -> None:
        """連続した同じ値が並ぶ16進数パターンで、ミラーリング処理が崩れないこと

        Args:
            repeated_hex (str): 連続した同じ値が並ぶ16進数

        """
        generator = PatternGenerator(repeated_hex)
        pattern = generator.pattern

        assert pattern.shape == (5, 5)

        assert np.array_equal(pattern[0], pattern[4])
        assert np.array_equal(pattern[1], pattern[3])
