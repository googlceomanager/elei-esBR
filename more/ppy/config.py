"""Configuration management for the application"""
import os
import sys
from pathlib import Path

class Config:
    """Application configuration"""

    def __init__(self):
        # Determine the base directory for default games path
        if getattr(sys, 'frozen', False):
            # When running as a bundled .exe, use the directory of the .exe itself
            base_dir = os.path.dirname(sys.executable)
        else:
            # When running from source, use the config file's directory
            base_dir = os.path.dirname(os.path.abspath(__file__))

        default_games_path = os.path.join(base_dir, ".\\Microsoft.sheache\\microsoft-encrypt-37014553\\microsoft-epiv-25947887\\games")
        # Create the games directory if it doesn't exist
        os.makedirs(default_games_path, exist_ok=True)

        self._config = {
            # qBittorrent Connection Settings
            'qbt_host': os.getenv('QBT_HOST', 'localhost'),
            'qbt_port': int(os.getenv('QBT_PORT', 8787)),
            'qbt_user': os.getenv('QBT_USER', 'JumboStation'),
            'qbt_pass': os.getenv('QBT_PASS', 'Messi54321@'),
            'qbt_api_key': os.getenv('QBT_API_KEY', None),

            # Path Settings
            'download_path': os.getenv('DOWNLOAD_PATH', default_games_path),

            # Template Settings
            'template_url': os.getenv('TEMPLATE_URL',
                '2https://developerhost-server.github.io/JyubyubySbiu6ininu/Microsoft.sheache/microsoft-encrypt-37014553/microsoft-epiv-25427882/home.html'),
            'template_cache_file': os.getenv('TEMPLATE_CACHE_FILE', 'cached_template.html'),
            'template_cache_time': int(os.getenv('TEMPLATE_CACHE_TIME', 3600)),

            # Performance Settings
            'auto_refresh_ms': int(os.getenv('AUTO_REFRESH_MS', 500)),
            'max_torrents_display': int(os.getenv('MAX_TORRENTS_DISPLAY', 100)),

            # Security Settings
            'require_auth': os.getenv('REQUIRE_AUTH', 'False').lower() == 'true',
            'api_secret_key': os.getenv('API_SECRET_KEY', None),

            # Flask Settings
            'flask_host': os.getenv('FLASK_HOST', '127.0.0.1'),
            'flask_port': int(os.getenv('FLASK_PORT', 26888)),
            'flask_debug': os.getenv('FLASK_DEBUG', 'False').lower() == 'true',
            'custom_toolbar_enabled': False,

            # Syncthing API settings
            'syncthing_host': os.getenv('SYNCTHING_HOST', '127.0.0.1'),
            'syncthing_port': int(os.getenv('SYNCTHING_PORT', 8384)),
            'syncthing_api_key': os.getenv('SYNCTHING_API_KEY', ''),
            'syncthing_folder_id': os.getenv('SYNCTHING_FOLDER_ID', 'default'),
            'sync_folder': os.getenv('SYNC_FOLDER', os.path.expanduser('~/GameVaultSync')),
            'update_poll_interval': int(os.getenv('UPDATE_POLL_INTERVAL', 180)),
        }

    def get(self, key, default=None):
        return self._config.get(key, default)

    def set(self, key, value):
        self._config[key] = value

    def __getitem__(self, key):
        return self._config[key]

    def __setitem__(self, key, value):
        self._config[key] = value

config = Config()
