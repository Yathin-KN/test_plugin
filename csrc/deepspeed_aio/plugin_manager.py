import os
import glob

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

check=PluginManager('/home/yathin/plugin/test_trampoline/csrc/plugins')
print(check.detect_plugins())