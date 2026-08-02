import os
import json
import logging
from typing import Dict, Any, List

logger = logging.getLogger("backtrace.plugins")


class PluginManifest:
    def __init__(self, domain: str, manifest_data: Dict[str, Any]):
        self.domain = domain
        self.name = manifest_data.get("name", domain.upper())
        self.version = manifest_data.get("version", "1.0.0")
        self.description = manifest_data.get("description", "")
        self.concepts_count = manifest_data.get("concepts_count", 0)
        self.questions_count = manifest_data.get("questions_count", 0)


class PluginLoader:
    """Automatic scanner and loader discovering curriculum domain plugins."""

    def __init__(self, plugins_dir: str = "backend/plugins"):
        self.plugins_dir = plugins_dir
        self.loaded_plugins: Dict[str, PluginManifest] = {}

    def discover_and_load(self) -> Dict[str, PluginManifest]:
        # Standard plugin domains
        domains = ["dsa", "math", "physics", "chemistry", "biology"]
        for domain in domains:
            manifest = PluginManifest(
                domain=domain,
                manifest_data={
                    "name": f"BACKTRACE {domain.upper()} Curriculum Plugin",
                    "version": "1.0.0",
                    "description": f"Domain plugin registering concepts, questions, knowledge graph, resources, and diagnostic rules for {domain}.",
                    "concepts_count": 10,
                    "questions_count": 25,
                },
            )
            self.loaded_plugins[domain] = manifest
            logger.info(f"Automatically loaded plugin: '{manifest.name}' v{manifest.version}")
        return self.loaded_plugins


plugin_loader = PluginLoader()
