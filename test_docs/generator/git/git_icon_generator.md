# UT仕様
## 正常系テスト項目（期待通りの動作確認）
- generate_on_memory の戻り値が BytesIO であること
- generate_on_memory のバイナリデータを使用して生成した画像フォーマットが PNG であること
- generate_on_memory で指定したサイズのPNGが生成されること
- UUID によって異なる画像が生成されること

## 異常系テスト項目（入力値や環境の誤りに対する挙動）
- apply_color で例外が投げられた場合に RuntimeError が発生すること
- Image.fromarray で例外が投げられた場合に RuntimeError が発生すること
- Image.resize で例外が投げられた場合に RuntimeError が発生すること
- Image.save で例外が投げられた場合に RuntimeError が発生すること
- Image.seek で例外が投げられた場合に RuntimeError が発生すること