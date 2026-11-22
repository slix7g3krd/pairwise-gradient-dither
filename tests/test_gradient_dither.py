import pytest
import render.gradient_dither as mod

CASES = [
    ("high_depth", (8, 10)),
    ("temporal_noise", (2, 3)),
    ("pre_composite", (1, 2)),
    ("luminance_adaptive", (0.5, 0.3)),
    ("linear_dither", (1, 2)),
    ("pre_encode", (1, 2)),
    ("ui_skip", (1, 2)),
    ("frame_vary", (1, 2)),
    ("alpha_dither", (0.5, 0.2)),
    ("bitdepth_scale", (8, 10)),
    ("bayer_matrix", (4, 2)),
    ("noise_amplitude", (0.2, 0.1)),
    ("band_detect", (0.1, 0.2)),
    ("quantize_step", (255, 1023)),
    ("output_check", (1, 2)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
