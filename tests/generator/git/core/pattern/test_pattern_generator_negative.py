"""PatternGenerator の準異常系テストケースを定義するモジュール。"""
# test_pattern_generator_nomal.py

# MIT License
# Copyright (c) 2025 kazuma tunomori
#
# Permission is hereby granted, free of charge, to any person obtaining a copy...

import pytest

from src.icon_generator.generator.git.core.pattern import PatternGenerator


class TestPatternGeneratorNegativeCases:
    """PatternGeneratorにおける異常系の動作を検証するテストクラス。"""

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
        "invalid_hex",
        [
            "",  # 空文字列
            "123",  # 短すぎる
            "0123456789abcdef1",  # 長すぎる(16文字以上)
        ],
    )
    def test_invalid_hex_length_raises_value_error(self, invalid_hex: str) -> None:
        """16進数文字列の長さが正しくない場合に ValueError が発生すること

        Args:
            invalid_hex (str): 無効な長さの16進数文字列

        """
        with pytest.raises(ValueError, match="hex_pattern must be exactly"):
            PatternGenerator(invalid_hex)

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    @pytest.mark.parametrize(
        "invalid_hex",
        [
            "0123456789abcdG",
            "0123456789abcdg",
        ],
    )
    def test_wrong_hex_raises_value_error(self, invalid_hex: str) -> None:
        """16進数以外の文字(例: GやZなど)が含まれている場合に ValueError が発生すること

        Args:
            invalid_hex (str): 無効な文字が含まれている16進数文字列

        """
        with pytest.raises(
            ValueError,
            match="hex_pattern must only contain hexadecimal characters",
        ):
            PatternGenerator(invalid_hex)

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    @pytest.mark.parametrize(
        ("invalid_rgb_tupple", "expected_exception", "expected_message"),
        [
            (
                (10, 255, 10, 80),
                ValueError,
                "rgb_pattern must be a list of 3 integers",
            ),
            (
                (10, 255, 256),
                ValueError,
                "Each RGB value must be an integer between 0 and 255",
            ),
            (
                (3.14, 255, 10),
                ValueError,
                "Each RGB value must be an integer between 0 and 255",
            ),
        ],
    )
    def test_invalid_rgb_tuple_len_raises_value_error(
        self,
        generator: PatternGenerator,
        invalid_rgb_tupple: tuple[int | float, ...],
        expected_exception: type[Exception],
        expected_message: str,
    ) -> None:
        """apply_color に渡す RGBリストのバリデーションテスト

        RGB リストの長さが3でない場合に ValueError が発生すること
        RGB の各要素が 0〜255 の整数範囲外の場合に ValueError が発生すること
        RGB の要素が整数でない場合に ValueError が発生すること

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
            generator.apply_color(rgb_pattern=invalid_rgb_tupple)  # type: ignore[arg-type]
