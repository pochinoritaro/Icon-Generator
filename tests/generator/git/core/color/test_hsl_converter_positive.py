"""HSLConverter の正常系テストケースを定義するモジュール。"""
# test_hsl_converter_positive.py

# MIT License
# Copyright (c) 2025 kazuma tunomori
#
# Permission is hereby granted, free of charge, to any person obtaining a copy...
import pytest

from src.icon_generator.generator.git.core.color.hsl_converter import HSLConverter


class TestHSLConverterPositiveCases:
    """HSLConverterにおける正常系の動作を検証するテストクラス。"""

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    @pytest.mark.parametrize(
        "color_pattern",
        [
            "0000000",
            "fffffff",
            "8008080",
        ],
    )
    def test_from_pattern(self, color_pattern: str) -> None:
        """from_pattern の戻り値が floatのtupleであること

        Args:
            color_pattern (str): 有効な16進数文字列

        """
        pattern = HSLConverter.from_pattern(color_pattern=color_pattern)

        assert 0 <= pattern[0] <= HSLConverter.MAX_HUE
        assert 0 <= pattern[1] <= HSLConverter.MAX_SATURATION
        assert 0 <= pattern[2] <= HSLConverter.MAX_LUMINANCE

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    @pytest.mark.parametrize(
        "hue_hex",
        [
            "000",
            "fff",
            "800",
        ],
    )
    def test_calculate_hue(self, hue_hex: str) -> None:
        """_calculate_hue の戻り値が 0-360 の範囲であること

        Args:
            hue_hex (str): 有効な16進数文字列

        """
        hue = HSLConverter._calculate_hue(hue_hex=hue_hex)  # type: ignore[arg-type]

        assert 0 <= hue <= HSLConverter.MAX_HUE

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    @pytest.mark.parametrize(
        "saturation_hex",
        [
            "00",
            "ff",
            "80",
        ],
    )
    def test_calculate_saturation(self, saturation_hex: str) -> None:
        """_calculate_saturation の戻り値が 0-100 の範囲であること

        Args:
            saturation_hex (str): 有効な16進数文字列

        """
        saturation = HSLConverter._calculate_hue(hue_hex=saturation_hex)  # type: ignore[arg-type]

        assert 0 <= saturation <= HSLConverter.MAX_SATURATION

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    @pytest.mark.parametrize(
        "luminance_hex",
        [
            "00",
            "ff",
            "80",
        ],
    )
    def test_calculate_luminance(self, luminance_hex: str) -> None:
        """_calculate_luminance の戻り値が 0-100 の範囲であること

        Args:
            luminance_hex (str): 有効な16進数文字列

        """
        luminance = HSLConverter._calculate_hue(hue_hex=luminance_hex)  # type: ignore[arg-type]

        assert 0 <= luminance <= HSLConverter.MAX_LUMINANCE
