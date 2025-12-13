def test_package_import():
    import gaia_hazlab_surface

    assert hasattr(gaia_hazlab_surface, "__all__")
