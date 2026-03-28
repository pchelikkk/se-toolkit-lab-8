import json
import os
from pathlib import Path


def main() -> None:
    app_dir = Path("/app/nanobot")
    config_path = app_dir / "config.json"
    resolved_path = app_dir / "config.resolved.json"
    workspace_path = app_dir / "workspace"

    with config_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    agents = data.setdefault("agents", {})
    defaults = agents.setdefault("defaults", {})
    defaults["provider"] = "custom"
    defaults["model"] = os.environ.get("LLM_API_MODEL", "coder-model")
    defaults["workspace"] = str(workspace_path)

    providers = data.setdefault("providers", {})
    custom = providers.setdefault("custom", {})
    custom["apiKey"] = os.environ["LLM_API_KEY"]
    custom["apiBase"] = os.environ["LLM_API_BASE_URL"]

    gateway = data.setdefault("gateway", {})
    gateway["host"] = os.environ["NANOBOT_GATEWAY_CONTAINER_ADDRESS"]
    gateway["port"] = int(os.environ["NANOBOT_GATEWAY_CONTAINER_PORT"])

    tools = data.setdefault("tools", {})
    mcp_servers = tools.setdefault("mcpServers", {})
    lms = mcp_servers.setdefault("lms", {})
    lms["command"] = "python"
    lms["args"] = ["-m", "mcp_lms"]
    lms["env"] = {
        "NANOBOT_LMS_BACKEND_URL": os.environ["NANOBOT_LMS_BACKEND_URL"],
        "NANOBOT_LMS_API_KEY": os.environ["NANOBOT_LMS_API_KEY"],
    }

    channels = data.setdefault("channels", {})

    if "webchat" in channels:
        webchat = channels["webchat"]
        webchat["enabled"] = True
        webchat["host"] = os.environ.get("NANOBOT_WEBCHAT_CONTAINER_ADDRESS", "0.0.0.0")
        webchat["port"] = int(os.environ.get("NANOBOT_WEBCHAT_CONTAINER_PORT", "8765"))
        webchat["access_key"] = os.environ.get("NANOBOT_ACCESS_KEY", "")
        webchat.setdefault("allow_from", ["*"])

    with resolved_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    os.execvp(
        "nanobot",
        [
            "nanobot",
            "gateway",
            "--config",
            str(resolved_path),
            "--workspace",
            str(workspace_path),
        ],
    )


if __name__ == "__main__":
    main()
