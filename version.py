import logging

logger = logging.getLogger("version")

version_n = "demo"
version_c = "v0.1.0"


def migrate_loaded_save(save):
    current = save.get("version")
    if current != version_c:
        save["version"] = version_c
        logger.info(f"[~] Version migrada: {current} -> {version_c}")
        return True
    return False