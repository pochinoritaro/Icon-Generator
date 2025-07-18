"""GitIconGenerator の異常系テストケースを定義するモジュール。"""
# test_git_icon_generator_negative.py

# MIT License
# Copyright (c) 2025 kazuma tunomori
#
# Permission is hereby granted, free of charge, to any person obtaining a copy...
import uuid
from typing import Any, Self
from unittest.mock import MagicMock

import numpy as np
import PIL
import PIL.Image
import pytest
from numpy.typing import NDArray
from PIL import Image, UnidentifiedImageError

from icon_generator.errors.error_message import ErrorMessages
from icon_generator.generator.git.core.pattern.pattern_generator import (
    PatternGenerator,
)
from icon_generator.generator.git.git_icon_generator import GitIconGenerator


class TestGitIconGeneratorNegativeCases:
    """GitIconGenerator の異常系テスト"""

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_apply_color_raise_runtime_error(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """apply_color で例外が投げられた場合に RuntimeError が発生すること

        Args:
            monkeypatch (pytest.MonkeyPatch): MonkeyPatchインスタンス

        """

        def apply_color(self: Self, rgb_pattern: tuple[int, int, int]) -> None:
            raise ValueError

        monkeypatch.setattr(
            PatternGenerator,
            PatternGenerator.apply_color.__name__,
            apply_color,
        )

        gennerator = GitIconGenerator(uuid.uuid4())

        with pytest.raises(
            RuntimeError,
            match=ErrorMessages.APPLY_COLOR_FAILED.value,
        ):
            gennerator.generate_on_memory()

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_image_fromarray_raise_runtime_error(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Image.fromarray で例外が投げられた場合に RuntimeError が発生すること

        Args:
            monkeypatch (pytest.MonkeyPatch): MonkeyPatchインスタンス

        """

        def fromarray(obj: NDArray[np.int_], mode: str | None = None) -> None:
            raise ValueError

        monkeypatch.setattr(
            Image,
            Image.fromarray.__name__,
            fromarray,
        )

        gennerator = GitIconGenerator(uuid.uuid4())

        with pytest.raises(
            RuntimeError,
            match=ErrorMessages.IDENTICON_GENERATION_FAILED.value,
        ):
            gennerator.generate_on_memory()

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_image_resize_raise_runtime_error(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Image.resize で例外が投げられた場合に RuntimeError が発生すること

        Args:
            monkeypatch (pytest.MonkeyPatch): MonkeyPatchインスタンス

        """

        def fromarray(obj: NDArray[np.int_], mode: str | None = None) -> None:
            raise ValueError

        monkeypatch.setattr(
            PIL.Image,
            PIL.Image.fromarray.__name__,
            fromarray,
        )

        gennerator = GitIconGenerator(uuid.uuid4())

        with pytest.raises(
            RuntimeError,
            match=ErrorMessages.IDENTICON_GENERATION_FAILED.value,
        ):
            gennerator.generate_on_memory()

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    @pytest.mark.parametrize(
        ("expected_exception"),
        [ValueError, OSError, UnidentifiedImageError],
    )
    def test_image_save_raise_runtime_error(
        self,
        monkeypatch: pytest.MonkeyPatch,
        expected_exception: type[Exception],
    ) -> None:
        """Image.save で例外が投げられた場合に RuntimeError が発生すること

        Args:
            monkeypatch (pytest.MonkeyPatch): MonkeyPatchインスタンス
            expected_exception (type[Exception]): 発生する例外

        """

        def save(self: Self, *args: list[Any], **kwargs: dict[Any, Any]) -> None:
            raise expected_exception

        monkeypatch.setattr(
            PIL.Image,
            PIL.Image.fromarray.__name__,
            save,
        )

        gennerator = GitIconGenerator(uuid.uuid4())

        with pytest.raises(
            RuntimeError,
            match=ErrorMessages.IDENTICON_GENERATION_FAILED.value,
        ):
            gennerator.generate_on_memory()

    @pytest.mark.reg
    @pytest.mark.v1_0_0
    def test_image_seek_raise_runtime_error(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Image.seek で例外が投げられた場合に RuntimeError が発生すること

        Args:
            monkeypatch (pytest.MonkeyPatch): MonkeyPatchインスタンス

        """
        dummy_bytesio = MagicMock()
        dummy_bytesio.seek.side_effect = ValueError("seek error")
        dummy_image = MagicMock()
        dummy_image.save.return_value = None

        def fake_bytesio(*args: list[Any], **kwargs: dict[Any, Any]) -> MagicMock:
            return dummy_bytesio

        def fake_fromarray(obj: NDArray[np.int_], mode: str | None = None) -> MagicMock:
            return dummy_image

        monkeypatch.setattr(
            "icon_generator.generator.git.git_icon_generator.BytesIO",
            fake_bytesio,
        )

        monkeypatch.setattr(
            "PIL.Image.fromarray",
            fake_fromarray,
        )

        gennerator = GitIconGenerator(uuid.uuid4())

        with pytest.raises(
            RuntimeError,
            match=ErrorMessages.IDENTICON_GENERATION_FAILED.value,
        ):
            gennerator.generate_on_memory()
