"""GitIconGenerator の正常系テストケースを定義するモジュール。"""
# test_git_icon_generator_positive.py

# MIT License
# Copyright (c) 2025 kazuma tunomori
#
# Permission is hereby granted, free of charge, to any person obtaining a copy...
import uuid
from io import BytesIO

import pytest
from PIL import Image

from src.icon_generator.generator.git.git_icon_generator import GitIconGenerator


class TestGitIconGeneratorPositiveCases:
    """GitIconGenerator の正常系テスト"""

    @pytest.fixture
    def hex_uuid(self) -> uuid.UUID:
        """uuid4インスタンス"""
        return uuid.uuid4()

    @pytest.fixture
    def generator(self, unique_uuid: uuid.UUID) -> GitIconGenerator:
        """GitIconGeneratorインスタンス"""
        return GitIconGenerator(unique_uuid)

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_generate_returns_bytesio(self, generator: GitIconGenerator) -> None:
        """戻り値の型が BytesIO であること

        Args:
            generator (GitIconGenerator): GitIconGeneratorインスタンス

        """
        result = generator.generate_on_memory()
        assert isinstance(result, BytesIO)

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_output_is_png_image(self, generator: GitIconGenerator) -> None:
        """生成した画像フォーマットが PNG であること

        Args:
            generator (GitIconGenerator): GitIconGeneratorインスタンス

        """
        result = generator.generate_on_memory()
        img = Image.open(result)
        assert img.format == "PNG"

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_image_size_matches_input(self, generator: GitIconGenerator) -> None:
        """指定したサイズの PNG が生成されること

        Args:
            generator (GitIconGenerator): GitIconGeneratorインスタンス

        """
        size = 128
        result = generator.generate_on_memory(image_size=size)
        img = Image.open(result)
        assert img.size == (size, size)

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_different_uuid_produces_different_image(self) -> None:
        """UUID によって異なる画像が生成されること

        Args:
        generator (GitIconGenerator): GitIconGeneratorインスタンス

        """
        gen1 = GitIconGenerator(uuid.UUID("12345678-1234-5678-1234-567812345678"))
        gen2 = GitIconGenerator(uuid.UUID("87654321-4321-8765-4321-876543218765"))
        img1 = gen1.generate_on_memory().getvalue()
        img2 = gen2.generate_on_memory().getvalue()
        assert img1 != img2
