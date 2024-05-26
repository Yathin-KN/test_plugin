from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import os
import glob
import subprocess

class CustomBuildExt(build_ext):
    def run(self):
        # Detect and build plugins
        plugin_manager = PluginManager('/home/yathin/plugin/test_trampoline/csrc/plugins')
        plugins = plugin_manager.detect_plugins()
        for plugin_name, metadata in plugins.items():
            self.build_plugin(plugin_name, metadata)
        
        # Build trampoline and pybind11 bindings
        self.build_trampoline()
        
        super().run()

    def build_plugin(self, plugin_name, metadata):
        sources = metadata['sources']
        lib_path = metadata['lib_path']
        cmd = ['g++', '-shared', '-o', lib_path, '-fPIC'] + sources
        subprocess.run(cmd, check=True)

    def build_trampoline(self):
        base_dir = os.path.abspath('csrc')
        sources = [
         os.path.join("csrc", "plugins", "trampoline.cpp"),
         os.path.join("csrc", "plugins", "py_ds_trampoline.cpp"),
         ]
        cmd = ['g++', '-O3', '-Wall', '-shared', '-std=c++14', '-fPIC',
               '`python3 -m pybind11 --includes`', '-I{}'.format(base_dir)] + sources + [
            '-o', os.path.join(base_dir,"plugins",'py_ds_trampoline') + '`python3-config --extension-suffix`'
        ]
        subprocess.run(' '.join(cmd), shell=True, check=True)

class PluginManager:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.plugins = {}

    def detect_plugins(self):
        plugin_dirs = [d for d in os.listdir(self.base_dir) if os.path.isdir(os.path.join(self.base_dir, d))]
        for plugin_dir in plugin_dirs:
            plugin_path = os.path.join(self.base_dir, plugin_dir)
            sources = glob.glob(os.path.join(plugin_path, '*.cpp'))
            headers = glob.glob(os.path.join(plugin_path, '*.h'))
            if sources:
                self.plugins[plugin_dir] = {
                    'sources': sources,
                    'headers': headers,
                    'lib_name': f"lib{plugin_dir}_device.so",
                    'lib_path': os.path.join(plugin_path, f"lib{plugin_dir}_device.so")
                }
        return self.plugins

setup(
    name='test_trampoline',
    version='0.1',
    ext_modules=[
        Extension('py_ds_trampoline', [])
    ],
    cmdclass={
        'build_ext': CustomBuildExt,
    }
)
