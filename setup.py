from setuptools import Extension, setup


def get_ext_modules() -> list:
    """获取三方模块"""
    extra_compile_flags = ["-O2", "-MT"]
    extra_link_args = []
    runtime_library_dirs = []

    vnlstartd = Extension(
        "vnpy_lstar.api.vnlstartd",
        [
            "vnpy_lstar/api/vnlstar/vnlstartd/vnlstartd.cpp",
        ],
        include_dirs=["vnpy_lstar/api/include",
                      "vnpy_lstar/api/vnlstar"],
        define_macros=[],
        undef_macros=[],
        library_dirs=["vnpy_lstar/api/libs", "vnpy_lstar/api"],
        libraries=["thosttraderapi_se"],
        extra_compile_args=extra_compile_flags,
        extra_link_args=extra_link_args,
        runtime_library_dirs=runtime_library_dirs,
        depends=[],
        language="cpp",
    )

    return [vnlstartd]


setup(
    ext_modules=get_ext_modules(),
)
