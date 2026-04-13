# config/

Runtime configuration files. These are loaded at startup and control
detection sensitivity, AGC behaviour, and filter parameters.

> **Do not commit local overrides.** Copy `signal_params.json` to
> `signal_params.local.json` for local tuning — the `.local.json`
> variant is gitignored.
