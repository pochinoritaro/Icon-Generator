"""RGBGenerator の正常系テストケースを定義するモジュール。"""
# rgb_generator.py

# MIT License
# Copyright (c) 2025 kazuma tunomori
#
# Permission is hereby granted, free of charge, to any person obtaining a copy...

import pytest

from src.icon_generator.generator.git.core.color.rgb_generator import RGBGenerator


class TestRGBGeneratorPositiveCases:
    """RGBGeneratorにおける正常系の動作を検証するテストクラス。"""

    @pytest.fixture
    def hex_string(self) -> str:
        """有効な16進数文字列"""
        return "abcde01"

    @pytest.fixture
    def generator(self, hex_string: str) -> RGBGenerator:
        """RGBGeneratorインスタンス"""
        return RGBGenerator(hex_string)

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_rgb_is_tuple(self, generator: RGBGenerator) -> None:
        """RGB が tuple[int, int, int] となっていること

        Args:
            generator (RGBGenerator): RGBGeneratorインスタンス

        """
        rgb_len = 3
        assert isinstance(generator.rgb, tuple)
        assert len(generator.rgb) == rgb_len
        assert all(isinstance(v, int) for v in generator.rgb)

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_rgb_values_are_within_0_to_255(self, generator: RGBGenerator) -> None:
        """RGB の範囲が0-255に収まっていること

        Args:
            generator (RGBGenerator): RGBGeneratorインスタンス

        """
        max_range = 255
        assert all(0 <= v <= max_range for v in generator.rgb)

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_rgb_equal_red_green_blue(self, generator: RGBGenerator) -> None:
        """RGB が red, green, blue と一致していること

        Args:
            generator (RGBGenerator): RGBGeneratorインスタンス

        """
        red, green, blue = (
            generator.red,
            generator.green,
            generator.blue,
        )
        assert generator.rgb == (red, green, blue)
