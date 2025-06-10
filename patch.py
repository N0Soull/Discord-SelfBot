import sys
from pathlib import Path
import discord

def patch_discord():
    def patched_parse_ready(self, data):
        # Ensure required attributes exist and handle None values
        self._ready_data = data.get('_ready_data', {}) or {}
        data['pending_payments'] = data.get('pending_payments', []) or []
        data['required_action'] = data.get('required_action', []) or []

        # Call the original parse_ready function
        original_parse_ready(self, data)

    # Store the original function
    original_parse_ready = discord.state.ConnectionState.parse_ready
    # Replace with the patched version
    discord.state.ConnectionState.parse_ready = patched_parse_ready
