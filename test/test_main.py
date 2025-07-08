import os
from main import load_config, process_inputs

def test_load_config():
    config = load_config("config.yaml")
    assert 'input_path' in config
    assert 'output_path' in config

def test_process_inputs(tmp_path):
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    input_dir.mkdir()
    output_dir.mkdir()

    dummy_file = input_dir / "test.jpg"
    dummy_file.write_text("test image content")

    process_inputs(str(input_dir), str(output_dir))
    output_files = list(output_dir.iterdir())
    assert len(output_files) == 1
    assert output_files[0].name.startswith("processed_")