from common.licenses import constants


def test_get_license_path_map_comprehenseion(monkeypatch):
    example_paths = [
        'licenses/by/1.0',
        'licenses/by/2.0',
        'licenses/by-nd/3.0',
        'licenses/by-sa/2.0',
    ]
    monkeypatch.setattr(constants, '_SIMPLE_LICENSE_PATHS', example_paths)
    monkeypatch.setattr(constants, '_SPECIAL_CASE_LICENSE_PATHS', {})
    actual_license_path_map = constants._get_license_path_map()
    expect_license_path_map = {
        'licenses/by/1.0': {'license': 'by', 'version': '1.0'},
        'licenses/by/2.0': {'license': 'by', 'version': '2.0'},
        'licenses/by-nd/3.0': {'license': 'by-nd', 'version': '3.0'},
        'licenses/by-sa/2.0': {'license': 'by-sa', 'version': '2.0'},
    }
    assert expect_license_path_map == actual_license_path_map


def test_get_license_path_map_update(monkeypatch):
    simple_paths = [
        'licenses/by/1.0',
        'licenses/by/2.0',
        'licenses/by-nd/3.0',
        'licenses/by-sa/2.0',
    ]
    special_paths = {
        'licenses/by-nc-nd/1.0': {'license': 'by-nd-nc', 'version': '1.0'},
        'publicdomain/zero/1.0': {'license': 'cc0', 'version': '1.0'},
        'publicdomain/mark/1.0': {'license': 'pdm', 'version': '1.0'},
    }
    monkeypatch.setattr(
        constants, '_SIMPLE_LICENSE_PATHS', simple_paths
    )
    monkeypatch.setattr(
        constants, '_SPECIAL_CASE_LICENSE_PATHS', special_paths
    )
    actual_license_path_map = constants._get_license_path_map()
    expect_license_path_map = {
        'licenses/by/1.0': {'license': 'by', 'version': '1.0'},
        'licenses/by/2.0': {'license': 'by', 'version': '2.0'},
        'licenses/by-nd/3.0': {'license': 'by-nd', 'version': '3.0'},
        'licenses/by-sa/2.0': {'license': 'by-sa', 'version': '2.0'},
        'licenses/by-nc-nd/1.0': {'license': 'by-nd-nc', 'version': '1.0'},
        'publicdomain/zero/1.0': {'license': 'cc0', 'version': '1.0'},
        'publicdomain/mark/1.0': {'license': 'pdm', 'version': '1.0'},
    }
    assert expect_license_path_map == actual_license_path_map
