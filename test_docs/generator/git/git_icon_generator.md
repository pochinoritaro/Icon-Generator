# UT仕様
## 正常系テスト項目（期待通りの動作確認）
- generate_on_memory の戻り値が BytesIO であること
- generate_on_memory のバイナリデータを使用して生成した画像フォーマットが PNG であること
- generate_on_memory で指定したサイズのPNGが生成されること
- UUID によって異なる画像が生成されること